from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


@login_required
def index(request):
    user = request.user
    return HttpResponse(f"Hello {user} {request}")


# Create appointment
@login_required
def create(request):
    user = request.user
    return HttpResponse(f"Hello {user.username} {request}")


# View specific appointment
@login_required
def view(appointment_id, request):
    user = request.user
    return HttpResponse(f"Hello {user.username} {appointment_id} {request}")


# Remove Appointment
@login_required
def remove(appointment_id, request):
    user = request.user
    return HttpResponse(f"Hello {user.username} {appointment_id} {request}")
