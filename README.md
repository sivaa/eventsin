django-social-auth-linkedin
===========================

Linkedin integration for Django Admin Interface using django-social-auth 

Installation
------------

- $ virtualenv django-social-auth-linkedin
- activate the virtual environment (Source/activate.bat (or)  source bin/activate) 
- $ pip install -r requirements.txt (uncomment the MySQL-python if you are using mysql)

- Create a linkedin app in https://www.linkedin.com/secure/developer and update LINKEDIN_CONSUMER_KEY & LINKEDIN_CONSUMER_SECRET settings


Configuration
------------

The new users can be given the super user permissions using

SOCIAL_AUTH_CREATE_USERS_AS_SUPER_ADMIN = True