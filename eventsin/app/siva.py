#data = {
#        'first_name': 'Yogesha', 
#        'last_name': 'K S', 
#        'access_token': 'oauth_token_secret=ffb06f96-2fd7-4f62-b229-91ad2228eeb5&oauth_token=fbabc4bf-a51b-4fad-9f2d-26600c874fb8', 
#        'phone-numbers': None, 
#        'skills': {'skill': [
#                              {'skill': {'name': 'Eclipse'}, 'id': '3'}, 
#                              {'skill': {'name': 'JSP'}, 'id': '4'}, 
#                              {'skill': {'name': 'C'}, 'id': '5'}, 
#                              {'skill': {'name': 'C++'}, 'id': '6'}
#                              ]}, 
#        'location': {'country': {'code': 'in'}, 'name': 'Bengaluru Area, India'}, 
#        'email_address': 'yogeshks1990@gmail.com', 
#        'id': '_iRXhCU-VD'}
#
#print data['first_name']
#
#if data['phone-numbers']['phone-number']['phone-type'] == 'mobile':
#    print data['phone-numbers']['phone-number']['phone-number'] 
#
#print data['location']['country']['code']
#print data['location']['name'].split(',')[0].replace('Area', '')
#
#for skill in data['skills']['skill']:
#    print skill['skill']['name']


import parser

parser.parse_topics_for_skill('cloud')