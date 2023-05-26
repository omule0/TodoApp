from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Task, List
from .forms import TaskForm,ListForm
from datetime import datetime, timedelta, timezone
from django.contrib import messages
from django.utils import timezone
# Create your views here.
@login_required
def sticky_notes(request):
    return render(request, 'sticky_notes.html')

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home(request):
    today = timezone.now().date()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    total_tasks = Task.objects.filter(user=request.user).count()
    upcoming_tasks = Task.objects.filter(due_date=today).count()
    return render(request, 'home.html', {'tasks': tasks, 'form': form, 'total_tasks': total_tasks,'upcoming_tasks':upcoming_tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

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
    return render(request, 'update_task.html', {'form': form,})

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

@login_required
def delete_old_tasks(request):
    current_time = datetime.now(timezone.utc)
    tasks = Task.objects.all()
    for task in tasks:
        time_difference = current_time - task.created_at.replace(tzinfo=timezone.utc)
        if time_difference.days > 7:
            task.delete()
    return redirect('home')

@login_required
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



from django.db.models import Q

@login_required
def weekly(request):
    now = datetime.now().date()  # Get the current date

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
    else:
        form = ListForm()

    # Calculate the start and end dates for the current week
    start_date = now - timedelta(days=now.weekday())  # Get the start of the week (Monday)
    end_date = start_date + timedelta(days=6)  # Get the end of the week (Sunday)

    # Retrieve all weekly tasks for the current day of the week or tasks that have due dates within the current week
    current_day = now.strftime('%A')
    weekly_tasks = List.objects.filter(Q(week_of=current_day) | Q(due_week__range=[start_date, end_date]), user=request.user)

    total_weekly_tasks = weekly_tasks.count()

    return render(request, 'weekly.html', {'lists': weekly_tasks, 'form': form, 'total_weekly_tasks': total_weekly_tasks})

@login_required
def deleteList(request, item_id):
    task = List.objects.get(pk=item_id)
    task.delete()
    return redirect('weekly')

@login_required
def week_cross_off(request, item_id):
    task = List.objects.get(pk=item_id)
    task.completed = True
    task.save()
    return redirect('weekly')

@login_required
def weekuncross(request,item_id):
    task = List.objects.get(pk=item_id)
    task.completed = False
    task.save()
    return redirect('weekly')

@login_required
def tasks_today(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(due_date=today)
    upcoming_tasks = Task.objects.filter(due_date=today).count()
    return render(request, 'upcoming.html', {'tasks': tasks,'upcoming_tasks':upcoming_tasks})