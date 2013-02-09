from django.db import models
from django.contrib.auth.models import User

class UserPreference(models.Model):
    user    =   models.OneToOneField(User)
    daily   =   models.BooleanField()
    weekly  =   models.BooleanField()
    email   =   models.BooleanField()
    sms     =   models.BooleanField()
    city    =   models.CharField(max_length = 255)
    country  =   models.CharField(max_length = 255)
    mobile  =   models.CharField(max_length = 255, blank = True, null = True)
    
    def __unicode__(self):
        return u' %s %s' % (self.user.first_name, self.user.last_name)

    def name(self):
        return u' %s %s' % (self.user.first_name, self.user.last_name)

    def user_email(self):
        return u' %s' % (self.user.email)


class Skill(models.Model):
    name    =   models.CharField(max_length = 255, primary_key=True)

    def __unicode__(self):
        return u' %s' % (self.name)

class UserSkill(models.Model):
    user    =   models.ForeignKey(User)
    skill   =   models.ForeignKey(Skill)

    class Meta:
        #verbose_name            = 'ClientTest'
        #verbose_name_plural     = 'ClientTests'
        unique_together = ("user", "skill")

    
    def __unicode__(self):
        return u' %s %s -> %s' % (self.user.first_name, self.user.last_name, self.skill.name)

    def name(self):
        return u' %s %s' % (self.user.first_name, self.user.last_name)

    
class Topic(models.Model):
    name    =   models.CharField(max_length = 255, primary_key=True)

    def __unicode__(self):
        return u' %s' % (self.name)

class Event(models.Model):
    event_id        =   models.CharField(max_length = 255, primary_key=True)
    name            =   models.CharField(max_length = 255)
    city            =   models.CharField(max_length = 255)
    country_code    =   models.CharField(max_length = 255)
    url             =   models.URLField()
    date            =   models.DateField()
    description     =   models.TextField()
    cost            =   models.CharField(max_length = 255)
    
    def __unicode__(self):
        return u' %s' % (self.name)
    
class TopicEvent(models.Model):
    topic   =   models.ForeignKey(Topic)
    event   =   models.ForeignKey(Event)

    class Meta:
        #verbose_name            = 'ClientTest'
        #verbose_name_plural     = 'ClientTests'
        unique_together = ("topic", "event")

    def __unicode__(self):
        return u' %s %s' % (self.topic.name, self.event.name)

