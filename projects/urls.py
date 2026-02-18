from django.urls import path
from . import views

urlpatterns = [
    path('allocation/', views.my_allocation, name='my_allocation'),
]