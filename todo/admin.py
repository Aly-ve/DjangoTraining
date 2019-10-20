from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'done')
    fieldsets = [
        ('Task', { 'fields': ['task', 'done'] })
    ]

# admin.site.register(Todo, TodoAdmin)