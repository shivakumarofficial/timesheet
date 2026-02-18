from django.contrib import admin
from .models import Project, Allocation


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "project_code")
    search_fields = ("name", "project_code")


@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ("employee", "project", "start_date", "end_date")
    list_filter = ("project", "start_date", "end_date")
