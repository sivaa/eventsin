from django.contrib import admin
from app.models import Event, Skill, Topic, TopicEvent, UserPreference, UserSkill

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily', 'weekly', 'email', 'sms', 'city', 'country', 'mobile', 'user_email')
    list_editable = ('daily', 'weekly', 'email', 'sms',)
    
    def queryset(self, request):
        qs = self.model._default_manager.get_query_set()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        if not request.user.is_superuser:
            return qs.filter(user__email__exact = request.user.email)
        self.list_editable = ()
        return qs
    
    
    def has_change_permission(self, request, obj=None):
        return True
        """
        Returns True if the given request has permission to change the given
        Django model instance, the default implementation doesn't examine the
        `obj` parameter.

        Can be overriden by the user in subclasses. In such case it should
        return True if the given request has permission to change the `obj`
        model instance. If `obj` is None, this should return True if the given
        request has permission to change *any* object of the given type.
        """
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())

    
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
