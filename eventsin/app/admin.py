from django.contrib import admin
from app.models import Event, Skill, Topic, TopicEvent, UserPreference, UserSkill

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily', 'weekly', 'email', 'sms', 'city', 'country', 'mobile', 'user_email')
    list_editable = ('daily', 'weekly', 'email', 'sms',)

    change_list_template = 'admin/custom_change_list.html'

    fieldsets = [
        (None, {'fields':()}), 
        ]

    def __init__(self, *args, **kwargs):
        super(UserPreferenceAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

    
    def queryset(self, request):
        qs = self.model._default_manager.get_query_set()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        
        if not request.user.is_superuser:
            return qs.filter(user__email__exact = request.user.email)
#        self.list_editable = ()
#        self.list_display_links = ( )
#
#        self.fieldsets = []

        return qs
    
    
    def has_change_permission(self, request, obj=None):
        return True
    
    
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

admin.site.disable_action('delete_selected')