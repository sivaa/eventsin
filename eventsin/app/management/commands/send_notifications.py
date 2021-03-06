from app.models import Topic, Skill, UserPreference, UserSkill, Event, \
    TopicEvent, alternate_location_names
from app.parser import parse_events_for_topic, parse_topics_for_skill
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import get_template
from django.template import Context

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Send Notifications'

    def handle(self, *args, **options):        
        print "============ STARTED ==================="
        user_preference_list = UserPreference.objects.all()
        
        for user_preference in user_preference_list:
            city = user_preference.city
            if str(user_preference.city).strip() in alternate_location_names:
                city = alternate_location_names[str(user_preference.city).strip()]

            event_dict = {}
            #print "USER : " + user_preference.user.username 
            user_skill_list = UserSkill.objects.filter(user = user_preference.user)
            
            for user_skill in user_skill_list:
                topic_list = Topic.objects.filter(name = user_skill.skill.name)

                for topic in topic_list:
                    topic_event_list = TopicEvent.objects.filter(topic = topic, 
                                                                  event__city__exact = city, 
                                                                  event__country_code__exact = user_preference.country)

                    for topic_event in topic_event_list:
                        if topic_event.event in event_dict:
#                            print "=== type ==="
#                            print type(event_dict[topic_event.event])
                            list = event_dict[topic_event.event]
                            list.append(topic.name)
                            
                            event_dict[topic_event.event] = list# event_dict[topic_event.event].append(topic.name)
#                            print event_dict[topic_event.event]
#                            print "=== updated  ====" 

                        else:
                            event_dict[topic_event.event] = [topic.name]
#                            print event_dict[topic_event.event]
#                            print "=== added ====" 
                        #print topic.name + " =====>>>>> " +     topic_event.event.name

            # Send Mail
            format_and_send_email(event_dict, user_preference.user, user_preference.mobile)
            
        print "=============== COMPLETED ======================"


def format_and_send_email(event_dict, user, mobile):
    #print event_dict
    
    recommend_tr_list = ''
    related_tr_list = ''
    
    recommend_list = []
    
    for event in event_dict:
        #print event_dict[event]
        is_related = True
        for topic in event_dict[event]:
            try:
                if event.name.lower().index(topic.lower()) == 0:
                    is_related = False
            except:
                try:
                    if event.description.lower().index(topic.lower()) == 0:
                        is_related = False
                except:
                    pass
        if is_related:
            related_tr_list += get_template('admin/tr.html').render(
            Context({
                'url': event.url,
                'name': event.name,
                'date_time': event.date,
                'location' : event.city + ", " + event.country_code.upper(),
                'cost': event.cost,
                'topics' : ', '.join(event_dict[event])
            })
            )
        else:
            recommend_list.append(event)
            recommend_tr_list += get_template('admin/tr.html').render(
            Context({
                'url': event.url,
                'name': event.name,
                'date_time': event.date,
                'location' : event.city + ", " + event.country_code.upper(),
                'cost': event.cost,
                'topics' : ', '.join(event_dict[event])
            })
            )
        
#    print recommend_tr_list
#    print related_tr_list 
    
    html_text =  get_template('admin/email.html').render(
            Context({
                'full_name': user.first_name + " " + user.last_name,
                'recommend_tr_list' : recommend_tr_list,
                'related_tr_list' : related_tr_list
                })
            )


#    print html_text
#    f = open('myfile.html','w')
#    f.write(html_text) # python will convert \n to os.linesep

                   
    #send_mail('Eventsin', html_text, 'siva@sivaa.in', [user.email], fail_silently=False)
#    
    import sendgrid
    
    # make a secure connection to SendGrid
    s = sendgrid.Sendgrid('eventsin', 'netapp', secure=True)
    
    # make a message object
    message = sendgrid.Message("notifications@eventsin.com", "EventsIN Notifications", '', html_text)
        
    # add a recipient
    message.add_to(user.email, user.first_name + " " + user.last_name)

    if recommend_tr_list == '' and related_tr_list == '':
        print "No Notifications found for " + user.first_name + " " + user.last_name
    else:
        print "Sending to " + user.first_name + " " + user.last_name
        # use the Web API to send your message
        s.web.send(message)

    #print str(event_dict)
    try:
        if not mobile.index('+'):
            pass
    except:
        mobile = None
    
    if recommend_tr_list == '' and related_tr_list == '':
        mobile = None

    from twilio.rest import TwilioRestClient
    # Find these values at https://twilio.com/user/account
    account_sid = "ACac3a53d62660c39d1cf4126a56f67a0b"
    auth_token = "81024aa8cbebd2bb0e75614b42c106d7"
    client = TwilioRestClient(account_sid, auth_token)
    
    
    if mobile and len(recommend_list)> 0 :
        try:
            message_str = ''
            for recommend_event in recommend_list:
                message_str += " "+ recommend_event.name + " on " + str(recommend_event.date)
            #print message_str
            message = client.sms.messages.create(to=mobile, from_="+18607994838", body=message_str[0:150])
        except:
            pass
