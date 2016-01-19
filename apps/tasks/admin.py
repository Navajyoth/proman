from django.contrib import admin

from .models import Task, StatusLog


class StatusLogInline(admin.StackedInline):
    model = StatusLog


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    list_filter = ('status', 'project', 'user')
    search_fields = ('title', )
    inlines = [StatusLogInline]

admin.site.register(Task, TaskAdmin)
