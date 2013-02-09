import json
import urllib
import datetime

MEETUP_URL = "https://api.meetup.com"
MEETUP_API_KEY = ""
DEFAULT_PARAM = "?key=" + MEETUP_API_KEY + "&sign=true"
FETCH_EVENTS = MEETUP_URL + "/2/open_events" + DEFAULT_PARAM
FETCH_TOPICS = MEETUP_URL + "/topics" + DEFAULT_PARAM

def parse_events_for_topic(topic):
  url = FETCH_EVENTS + "&topic=" + topic
  json_data = urllib.urlopen(url).read()
  parsed_data = json.loads(json_data)
  for x in parsed_data['results']:
    event_id = x['id'] #check for db presence to avoid deplicate entry
    event_name = x['name']
    city = x['venue']['city']
    country = x['venue']['country']
    event_url = x['event_url']
    event_date = datetime.datetime.utcfromtimestamp(int(x['time'])).strftime('%Y-%m-%d %H:%M:%S'))
    description = x['description']
    if x['fee']: event_fee = x['fee']['currency'] + " " + str(x['fee']['amount']) else: "free"


def parse_topics_for_skill(skill)
  url = FETCH_TOPICS + "&search=" + skill
  json_data = urllib.urlopen(url).read()
  parsed_data = json.loads(json_data)
  for x in parsed_data['results']
    name = x['name'] #check for db presence to avoid deplicate entry
