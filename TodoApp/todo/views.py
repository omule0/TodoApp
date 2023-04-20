from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def sticky_notes(request):
    if request.is_ajax():
        return render(request, "sticky_notes.html")