from app.models import UserPreference, Event, Skill, Topic, UserSkill, \
    TopicEvent
from django.contrib.auth.models import Group
from social_auth.models import UserSocialAuth
import json



def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """Create user. Depends on get_username pipeline."""
    if user:
        return {'user': user}
    if not username:
        return None

    # Customization 
    email = details.get('email')
    new_user = UserSocialAuth.create_user(username=email, email=email)
    default_group = Group.objects.get(name__exact = 'NORMAL_USER')
    new_user.groups = (default_group,)
    new_user.is_staff = True

    if email == 'sivasubramaniam.a@gmail.com':
        new_user.is_superuser = True        

    try:
        from settings import SOCIAL_AUTH_CREATE_USERS_AS_SUPER_ADMIN
        if SOCIAL_AUTH_CREATE_USERS_AS_SUPER_ADMIN:
            new_user.is_superuser = True        
    except:
        pass    
    
    return {
        'user': new_user,         
        'is_new': True
    }


def load_extra_data(backend, details, response, uid, user, social_user=None,
                    *args, **kwargs):
    """Load extra data from provider and store it on current UserSocialAuth
    extra_data field.
    """
    social_user = social_user or \
                  UserSocialAuth.get_social_auth(backend.name, uid)
    if social_user:
        extra_data = backend.extra_data(user, uid, response, details)
        if extra_data and social_user.extra_data != extra_data:
            if social_user.extra_data:
                social_user.extra_data.update(extra_data)
            else:
                social_user.extra_data = extra_data
            social_user.save()
            update_user_skill(social_user)
        return {'social_user': social_user}


def update_user_skill(social_user):
    data  = social_user.extra_data
    print social_user.user.id
    
    print data
    
    mobile = ''
    try:
        if data['phone-numbers']['phone-number']['phone-type'] == 'mobile':
            mobile = data['phone-numbers']['phone-number']['phone-number'] 
    except:
        print "Phone # Not found"
            
    UserPreference.objects.create(
                                  user    =   social_user.user,
                                  weekly  =   True,
                                  email   =   True,
                                  city    =   data['location']['name'].split(',')[0].replace('Area', ''),
                                  country =   data['location']['country']['code'],
                                  mobile  =   mobile,
                                  )
    
    try:
        for skill in data['skills']['skill']:
            skill_obj = None
            try:
                skill_obj = Skill.objects.get(name = skill['skill']['name']) # Already Exists             
            except:
                skill_obj = Skill.objects.create( name = skill['skill']['name'])
            try:
                UserSkill.objects.create(user = social_user.user, skill = skill_obj)
            except:
                pass # Already Exists
    except:
        pass # No Skill exists