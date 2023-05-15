from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Task
from .forms import TaskForm
from datetime import datetime, timedelta, timezone
# Create your views here.
@login_required
def sticky_notes(request):
    return render(request, 'sticky_notes.html')
def landing_page(request):
    return render(request, 'landing_page.html')
@login_required
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return JsonResponse({
                'name': task.name,
                'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
                'due_time': task.due_time.strftime('%H:%M:%S') if task.due_time else '',
            })
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return JsonResponse({
                'name': task.name,
                'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
                'due_time': task.due_time.strftime('%H:%M:%S') if task.due_time else '',
            })
        else:
            return JsonResponse({'error': 'Invalid form data'})
    else:
        return JsonResponse({'error': 'Invalid request'})


@login_required
def deleteTask(request, name_id):
    task = Task.objects.get(pk=name_id)
    task.delete()
    return redirect('/home')

@login_required
def updateTask(request, name_id):
    task = Task.objects.get(pk=name_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})

@login_required
def cross_off(request, name_id):
    task = Task.objects.get(pk=name_id)
    task.completed = True
    task.save()
    return redirect('home')

@login_required
def uncross(request, name_id):
    task = Task.objects.get(pk=name_id)
    task.completed = False
    task.save()
    return redirect('home')

def delete_old_tasks(request):
    current_time = datetime.now(timezone.utc)
    tasks = Task.objects.all()
    for task in tasks:
        time_difference = current_time - task.created_at.replace(tzinfo=timezone.utc)
        if time_difference.days > 7:
            task.delete()
    return redirect('home')

def mark_skipped_tasks(request):
        current_datetime = datetime.now()
        tasks = Task.objects.all()
        for task in tasks:
            if not task.completed and task.due_date and task.due_time:
                due_datetime = datetime.combine(task.due_date, task.due_time)
                if due_datetime < current_datetime:
                    task.is_skipped = True
                    task.save() 
        return redirect('home')