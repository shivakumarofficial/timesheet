from django.shortcuts import render
from .models import Allocation
from django.contrib.auth.decorators import login_required


@login_required
def my_allocation(request):
    allocations = Allocation.objects.filter(employee__user=request.user)
    return render(request, "my_allocation.html", {"allocations": allocations})
