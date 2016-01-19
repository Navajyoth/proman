from django.contrib import admin

from .models import Project, WorkItem, Milestone


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'is_active',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkItem)
admin.site.register(Milestone)
