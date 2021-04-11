from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Users.forms import CustomUserCreationForm


def dashboard(request):
    return render(request, "users/dashboard.html")

def registration(request):
    if request.method == "GET":
        return render(request, "users/registration.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))