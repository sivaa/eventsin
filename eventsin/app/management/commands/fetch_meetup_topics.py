from django.core.management.base import BaseCommand, CommandError
from app.models import Topic, Skill
from app.parser import parse_events_for_topic, parse_topics_for_skill

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Get MeetUp Topics By Skills'

    def handle(self, *args, **options):        
        print "============ STARTED ==================="
        skill_list = Skill.objects.all()
        #print skill_list
        for skill in skill_list:
            topic_list = parse_topics_for_skill(skill.name)
            #print topic_list
            for topic in topic_list:
                try:
                    Topic.objects.create(name = topic)
                except:
                    print "Topic Already Exists"
        print "=============== COMPLETED ======================"
