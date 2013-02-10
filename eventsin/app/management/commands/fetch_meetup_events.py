from django.core.management.base import BaseCommand, CommandError
from app.models import Topic, Skill, Event, TopicEvent
from app.parser import parse_events_for_topic, parse_topics_for_skill

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Get MeetUp Events By Topics'

    def handle(self, *args, **options):        
        print "============ JOB STARTED (Get MeetUp Events By Topics) ==================="
        topic_list = Topic.objects.all()
        for topic in topic_list:
            print "Looking for " + topic.name
            event_list = parse_events_for_topic(topic.name)
            for event in event_list:
                event_obj = None
                try:
                    event_obj = Event.objects.get(event_id = event.event_id)
                    #print "Event Already Exists"
                except:
                    try:
                        event_obj = Event.objects.create(
                                                    event_id    = event.event_id,
                                                    name        = event.name,
                                                    city        = event.city,
                                                    country_code    =   event.country_code,
                                                    url             =   event.url,
                                                    date            =   event.date,
                                                    description     =   event.description,
                                                    cost            =   event.cost
                                                    )
                        print "Adding Event : " + event.name + "(" + event.city + ")" 
                    except:
                        pass

                if event_obj:
                    try:
                        TopicEvent.objects.create (event = event_obj, topic = topic)
                    except:
                        pass
                    
        print "=============== COMPLETED ======================"




#                    if event.name.lower().index(topic.name.lower() + ' ') or \
#                       event.name.lower().index(' '+ topic.name.lower()) or \
#                       event.description.lower().index(topic.name.lower() + ' ') or \
#                       event.description.lower().index(' '+ topic.name.lower()):
#                        print event.name
