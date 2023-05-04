from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(response):
    if response.method == "POST":
	    form = UserRegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/home")
    else:
	    form = UserRegisterForm()
    return render(response, "Users/register.html", {"form":form})


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