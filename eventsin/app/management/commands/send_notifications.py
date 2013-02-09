from django.core.management.base import BaseCommand, CommandError
from app.models import Topic, Skill, UserPreference, UserSkill, Event,\
    TopicEvent
from app.parser import parse_events_for_topic, parse_topics_for_skill

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Send Notifications'

    def handle(self, *args, **options):        
        print "============ STARTED ==================="
        user_preference_list = UserPreference.objects.all()
        
        for user_preference in user_preference_list:
            body = ''
            print "USER : " + user_preference.user.username 
            user_skill_list = UserSkill.objects.filter(user = user_preference.user)
            
            for user_skill in user_skill_list:
                topic_list = Topic.objects.filter(name = user_skill.skill.name)

                for topic in topic_list:
                    topic_event_list = TopicEvent.objects.filter(topic = topic, 
                                                                  event__city__exact = 'Bangalore', 
                                                                  event__country_code__exact = user_preference.country)

                    for topic_event in topic_event_list:
                        print topic.name + " =====>>>>> " +     topic_event.event.name
                        body += topic.name + " =====>>>>> " +     topic_event.event.name + '\n' 
                        print '----------------------------------------------------'
            
            from django.core.mail import send_mail
            send_mail('Eventsin', body, 'siva@sivaa.in', [user_preference.user.email], fail_silently=False)
            
        print "=============== COMPLETED ======================"
