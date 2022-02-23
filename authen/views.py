
from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.urls import reverse


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect(reverse("home:index"))


def sigup_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            return redirect(reverse("login"))
        messages.error(request, form.errors)
    form = NewUserForm()
    return render (request=request, template_name="authen/sigup.html", context={"register_form":form})