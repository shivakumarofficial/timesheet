from django.db import models
from accounts.models import Employee


class Project(models.Model):
    name = models.CharField(max_length=200)
    project_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Allocation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee} → {self.project}"
