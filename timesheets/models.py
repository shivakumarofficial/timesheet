from django.db import models
from accounts.models import Employee
from projects.models import Project


class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    billable_hours = models.FloatField(default=0)
    non_billable_hours = models.FloatField(default=0)
    status = models.CharField(max_length=20, default="Filled")

    def __str__(self):
        return f"{self.employee} - {self.date}"
