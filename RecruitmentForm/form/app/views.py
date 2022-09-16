from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
def homepage(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Your movie was successfully added!')
            return redirect("app:database")
        else:
            messages.error(request, 'Error saving form')
            return render(request=request, template_name="build.html", context={'registration_form': registration_form})

    registration_form = RegistrationForm()
    return render(request=request, template_name="build.html", context={'registration_form': registration_form})


def database(request):
    registrations = Registration.objects.all()
    return render(request=request, template_name="dashboard.html", context={'registration': registrations})
