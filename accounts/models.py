from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=20)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} ({self.emp_id})"
