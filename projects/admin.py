from django.contrib import admin
from .models import Project, ProjectLink


class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ("__str__", "type")


admin.site.register(Project)
admin.site.register(ProjectLink, ProjectLinkAdmin)
