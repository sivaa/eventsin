from django.contrib import admin
from app.models import Event, Skill, Topic, TopicEvent, UserPreference, UserSkill

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily', 'weekly', 'email', 'sms', 'city', 'country', 'mobile', 'user_email')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill',)

    
admin.site.register(UserPreference, UserPreferenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(UserSkill, UserSkillAdmin)

admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(TopicEvent)




#*****  AUTOMATIC SUPER USER CREATION *******************

# From http://stackoverflow.com/questions/1466827/ --

# Create our own test user automatically.

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals


def create_testuser(app, created_models, verbosity, **kwargs):
#    if not settings.DEBUG:
#        return
    try:
        auth_models.User.objects.using('default').get(username=settings.SUPER_USER_USERNAME)
    except auth_models.User.DoesNotExist:
        print '*' * 80
        print 'Creating Super User -- Username: %s, Password: %s' % (settings.SUPER_USER_USERNAME, settings.SUPER_USER_PASSWORD)
        print '*' * 80
        assert auth_models.User.objects.db_manager('default').create_superuser(settings.SUPER_USER_USERNAME, settings.SUPER_USER_EMAIL, settings.SUPER_USER_PASSWORD)
    else:
        print 'Given user already exists.'


# Prevent interactive question about wanting a superuser created.  (This code
# has to go in this otherwise empty "models" module so that it gets processed by
# the "syncdb" command during database creation.)

if settings.AUTO_SUPER_USER_CREATION:
    signals.post_syncdb.disconnect( create_superuser, sender=auth_models, dispatch_uid='django.contrib.auth.management.create_superuser')
    signals.post_syncdb.connect(    create_testuser,  sender=auth_models, dispatch_uid='util.models.create_testuser')
