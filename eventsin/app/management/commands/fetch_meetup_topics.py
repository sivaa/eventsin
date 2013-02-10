from app.models import Topic, Skill
from app.parser import  parse_topics_for_skill
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = ''
    help = 'Get MeetUp Topics By Skill'

    def handle(self, *args, **options):        
        print "============ JOB STARTED (Get MeetUp Topics By Skill) ==================="
        skill_list = Skill.objects.all()
        #print skill_list
        for skill in skill_list:
            print "Looking for " + skill.name
            topic_list = []
            try:
                topic_list = parse_topics_for_skill(skill.name)
            except:
                print "ERROR 400"
            #print topic_list
            for topic in topic_list:
                try:
                    Topic.objects.create(name = topic)
                    print "Adding Topic : " + topic
                except:
                    pass
                    #print "Topic Already Exists"
        print "=============== COMPLETED ======================"
