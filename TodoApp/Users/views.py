from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(response):
    if response.method == "POST":
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(response, 'Your account has been created! You are now able to log in.')
            return redirect("/home")
    else:
        form = UserRegisterForm()
    return render(response, "Users/register.html", {"form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account Info has been Updated")
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(instance=profile)
    context = {"u_form": u_form,
               'p_form': p_form}
    return render(request, "Users/profile.html", context)


def home(request):
    return render(request, 'home.html')

