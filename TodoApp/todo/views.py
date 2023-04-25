from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({
                'name': task.name,
                'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
                'due_time': task.due_time.strftime('%H:%M:%S') if task.due_time else '',
            })
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

@login_required
def sticky_notes(request):
    return render(request, 'sticky_notes.html')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({
                'name': task.name,
                'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
                'due_time': task.due_time.strftime('%H:%M:%S') if task.due_time else '',
            })
    return JsonResponse({'error': 'Invalid request'})
