import json
import urllib2, urllib
import datetime
import sys
from app.models import EventMaster

MEETUP_URL      =   "https://api.meetup.com"
MEETUP_API_KEY  =   "7b723e2142c4459214969b2a517670"
#DEFAULT_PARAM   =   "?key=" + MEETUP_API_KEY + "&sign=true"
FETCH_EVENTS    =   MEETUP_URL + "/2/open_events" #+ DEFAULT_PARAM
FETCH_TOPICS    =   MEETUP_URL + "/topics" #+ DEFAULT_PARAM

def parse_events_for_topic(topic):
    url = FETCH_EVENTS
    enc = urllib.urlencode({'topic': topic + ',', 'key': MEETUP_API_KEY, 'sign': 'true'})
    print topic
    
    req = urllib2.urlopen(url + "/?" + enc)
    json_data = req.read()
    
    encoding=req.headers['content-type'].split('charset=')[-1]
    json_data = unicode(json_data, encoding)

    parsed_data = json.loads(json_data)

    event_list = []
    for x in parsed_data['results']:
        event_id    = x['id'] #check for db presence to avoid deplicate entry
        event_name  = x['name']
        city        = ''
        country     = ''
        try:        
            city = x['venue']['city']
        except:
            pass
        try:
            country = x['venue']['country']
        except:
            pass
        event_url   = x['event_url']
        
        event_date = None
        try:
            event_date  = datetime.datetime.fromtimestamp(int(x['time'])//1000).strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
        description = ''
        try:
            description = x['description']
        except:
            pass
        
        cost = ''
        try:
            if x['fee']: 
                cost = x['fee']['currency'] + " " + str(x['fee']['amount']) 
        except: 
            pass
        
        event = EventMaster(event_id, event_name, city, country, event_url, event_date, description, cost)
        event_list.append(event)
    return event_list
 
def parse_topics_for_skill(skill):
    url = FETCH_TOPICS

    enc = urllib.urlencode({'name': skill, 'key': MEETUP_API_KEY, 'sign': 'true'})
    req = urllib2.urlopen(url + "/?" + enc)
    print skill
    json_data = req.read()
    
    encoding=req.headers['content-type'].split('charset=')[-1]
    json_data = unicode(json_data, encoding)

    parsed_data = json.loads(json_data)
 
    topic_list = []
    for x in parsed_data['results']:
        name = x['name'] #check for db presence to avoid deplicate entry
        #print name
        topic_list.append(name)
    return topic_list
