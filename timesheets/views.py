from django.shortcuts import render, redirect
from .models import Timesheet
from projects.models import Project
from accounts.models import Employee
from django.contrib.auth.decorators import login_required


@login_required
def timesheet_view(request):
    employee = Employee.objects.get(user=request.user)

    if request.method == "POST":
        project_id = request.POST.get("project")
        date = request.POST.get("date")
        billable = request.POST.get("billable")
        non_billable = request.POST.get("non_billable")

        project = Project.objects.get(id=project_id)

        Timesheet.objects.create(
            employee=employee,
            project=project,
            date=date,
            billable_hours=billable,
            non_billable_hours=non_billable,
        )
        return redirect("timesheet")

    timesheets = Timesheet.objects.filter(employee=employee)
    projects = Project.objects.all()

    return render(request, "timesheet.html", {
        "timesheets": timesheets,
        "projects": projects
    })