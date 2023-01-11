from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, "accounts/home.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            messages.success(request, f"Hi {email}, your account has been successfully created")
            return redirect("home")
    else:
        form = UserRegisterForm()
    
    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)