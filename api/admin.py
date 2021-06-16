from django.contrib import admin
from .models import Project, ProjectLink, Message


class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ("__str__", "type")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "created_at")


admin.site.register(Project)
admin.site.register(ProjectLink, ProjectLinkAdmin)
admin.site.register(Message, MessageAdmin)
