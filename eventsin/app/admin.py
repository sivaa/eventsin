from django.contrib import admin
from app.models import Event, Skill, Topic, TopicEvent, UserPreference, UserSkill

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily', 'weekly', 'email', 'sms', 'city', 'country', 'mobile', 'user_email')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'name', 'city', 'country_code', 'cost', 'date',)
    search_fields = ('event_id', 'name', 'city', 'country_code', 'cost', 'description', 'url',)
    list_filter = ('country_code',)

class TopicEventAdmin(admin.ModelAdmin):
    list_display = ('topic', 'event',)
    list_filter = ('topic',)

    
admin.site.register(UserPreference, UserPreferenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(UserSkill, UserSkillAdmin)

admin.site.register(Topic)
admin.site.register(Event, EventAdmin)
admin.site.register(TopicEvent, TopicEventAdmin)
