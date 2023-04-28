from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from todo.models import Owner
from django.contrib.auth import login
from django.db import IntegrityError
from django.db.models import F
from .models import Owner

def register(request):
    """SignUp page view that signs up new user to the system, according to given information."""

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Instantiate UserRegisterForm with request.POST data
        if form.is_valid():  # Check if form data is valid
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Owner.objects.create_user(username, email, password)
                login(request, user)
                return redirect('login')
            except IntegrityError:
                appStatus = "Oops! It seems like this username is taken, please choose another username."
                return render(request, 'Users/register.html', {'form': form, 'status': appStatus})
    else:
        form = UserRegisterForm()  # Instantiate an empty UserRegisterForm
    return render(request, 'Users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account Info has been Updated")
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {"u_form": u_form}
    return render(request, "Users/profile.html", context)


def home(request):
    return render(request, 'home.html')