from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from accounts.models import Employee
from timesheets.models import Timesheet
from projects.models import Project, Allocation


# ================= EMPLOYEE LOGIN =================
def employee_login(request):
    # If already logged in → go to dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # If admin → go to admin dashboard
            if user.is_staff:
                return redirect("admin_dashboard")

            # Normal employee → employee dashboard
            return redirect("dashboard")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


# ================= LOGOUT =================
def employee_logout(request):
    logout(request)
    return redirect("login")


# ================= EMPLOYEE DASHBOARD =================
@login_required
def dashboard(request):
    try:
        employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        # If employee record missing → logout
        logout(request)
        return redirect("login")

    timesheets = Timesheet.objects.filter(employee=employee)

    total_billable = sum(t.billable_hours for t in timesheets)
    total_non_billable = sum(t.non_billable_hours for t in timesheets)

    context = {
        "employee": employee,
        "total_billable": total_billable,
        "total_non_billable": total_non_billable,
    }

    return render(request, "dashboard.html", context)


# ================= ADMIN DASHBOARD =================
@staff_member_required
def admin_dashboard(request):
    employees = Employee.objects.all()
    allocations = Allocation.objects.select_related("employee", "project")
    timesheets = Timesheet.objects.select_related("employee", "project").order_by("-date")

    context = {
        "total_employees": employees.count(),
        "total_projects": Project.objects.count(),
        "total_allocations": allocations.count(),
        "total_timesheets": timesheets.count(),
        "employees": employees,
        "allocations": allocations,
        "timesheets": timesheets,
    }

    return render(request, "admin_dashboard.html", context)
