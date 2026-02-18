from django.urls import path
from .views import employee_login, employee_logout, dashboard, admin_dashboard

urlpatterns = [
    path("login/", employee_login, name="login"),
    path("logout/", employee_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
]
