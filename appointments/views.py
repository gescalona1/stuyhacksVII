from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


@login_required
def index(request):
    user = request.user
    return render(request, 'appointmentindex.html', {user: user})


# Create appointment
@login_required
def create(request):
    user = request.user
    print(settings.GOOGLE_MAPS_API_KEY)
    if request.method == 'POST':
        print(request.POST)
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            appointment = Appointment.objects.create(request.POST)
            return redirect("appointments_view")
            # do something.
    else:
        form = AppointmentCreationForm()
    return render(request, 'appointmentform.html', {'form': form})


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
