from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #

admin.site.register(Project, ProjectAdmin)