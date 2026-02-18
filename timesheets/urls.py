from django.urls import path
from .views import timesheet_view

urlpatterns = [
    path('', timesheet_view, name='timesheet'),
]