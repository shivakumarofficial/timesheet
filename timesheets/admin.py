from django.contrib import admin
from .models import Timesheet


@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "project",
        "date",
        "billable_hours",
        "non_billable_hours",
        "status",
    )
    list_filter = ("project", "date")
    search_fields = ("employee__user__username", "project__name")
