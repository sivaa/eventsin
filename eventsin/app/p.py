import json
import urllib2
import datetime

MEETUP_URL      =   "https://api.meetup.com"
MEETUP_API_KEY  =   "7b723e2142c4459214969b2a517670"
DEFAULT_PARAM   =   "?key=" + MEETUP_API_KEY + "&sign=true"
FETCH_EVENTS    =   MEETUP_URL + "/2/open_events" + DEFAULT_PARAM
FETCH_TOPICS    =   MEETUP_URL + "/topics" + DEFAULT_PARAM

url         = FETCH_TOPICS + "&search=cloud"
#json_data   = urllib.urlopen(url).read()
#parsed_data = json.loads(json_data)

json_data = urllib2.urlopen(url).read()

print type(json_data)

json_data = u'%s' % (json_data)

parsed_data = json.loads(json_data)

    
print parsed_data    
    
for x in parsed_data['results']:
    name = x['name'] #check for db presence to avoid deplicate entry
    print name
        


