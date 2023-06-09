from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse, HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task, List
from .forms import TaskForm,ListForm
from datetime import datetime, timedelta, timezone
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime
from django.utils.safestring import mark_safe
from django.utils import timezone
import calendar
import datetime
from django.db.models import Q

@login_required
def sticky_notes(request):
    messages.success(request, (' Welcome to your sticky notes'))
    return render(request, 'sticky_notes.html')

def landing_page(request):
    return render(request, 'Landing_page.html')

@login_required
def home(request):
    today = timezone.now().date()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, ('The task has been added to list successfully!'))
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    total_tasks = Task.objects.filter(user=request.user).count()
    upcoming_tasks = Task.objects.filter(due_date=today,completed=False, is_skipped=False).count()
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
    messages.success(request, ('The task has been deleted successfully!'))
    return redirect('/home')

@login_required
def updateTask(request, name_id):
    task = Task.objects.get(pk=name_id)
    form = TaskForm(request.POST, instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ('The task has been edited successfully!'))
            return redirect('/home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'task': task, 'form': form})

@login_required
def cross_off(request, name_id):
    task = Task.objects.get(pk=name_id)
    task.completed = True
    task.save()
    messages.success(request, ('The task has been marked completed successfully!'))
    return redirect('home')

@login_required
def uncross(request, name_id):
    task = Task.objects.get(pk=name_id)
    task.completed = False
    task.save()
    messages.success(request, ('The task has been marked incomplete successfully!'))
    return redirect('home')

@login_required
def delete_old_tasks(request):
    current_time = datetime.datetime.now(timezone.utc)
    tasks = Task.objects.all()
    for task in tasks:
        time_difference = current_time - task.created_at.replace(tzinfo=timezone.utc)
        if time_difference.days > 7:
            task.delete()
            messages.success(request, ('Old tasks have been deleted successfully!'))
        else:
            messages.error(request, ('There are no old tasks to delete!'))
    return redirect('home')

'''@login_required
def mark_skipped_tasks(request):
        current_datetime = datetime.now(timezone.utc)
        tasks = Task.objects.all()
        for task in tasks:
            if not task.completed and task.due_date and task.due_time:
                due_datetime = datetime.combine(task.due_date, task.due_time)
                if due_datetime < current_datetime:
                    task.is_skipped = True
                    task.save() 
                    messages.success(request, (' Tasks have been marked as skipped successfully!'))
                else:
                    messages.error(request, ('There are no tasks to be marked as skipped!'))
        return redirect('home')'''



@login_required
def weekly(request):
    now = timezone.now().date()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, ('The task has been added to list successfully!'))
        else:
            messages.error(request, ('The task has not been added.'))
    else:
        form = ListForm()

    # Get the start and end of the week range for the current week
    start_date = now - timedelta(days=now.weekday())
    end_date = start_date + timedelta(days=6)

    # Retrieve all weekly tasks for the current week
    weekly_tasks = List.objects.filter(week_of__range=[start_date, end_date], user=request.user)

    total_weekly_tasks = weekly_tasks.count()

    return render(request, 'weekly.html', {'lists': weekly_tasks, 
                                           'form': form, 
                                           'total_weekly_tasks': total_weekly_tasks,
                                           'start_date': start_date,
                                           'end_date': end_date})
def delete_old_weekly_tasks(request):
    # Calculate the date threshold for deleting old weekly tasks
    threshold_date = timezone.now().date() - timedelta(days=7)
    old_weekly_tasks = List.objects.filter(week_of__lt=threshold_date)
    old_weekly_tasks.delete()
    messages.success(request, ('Old Weekly tasks have been deleted successfully!'))
    return redirect('weekly')

@login_required
def deleteList(request, item_id):
    task = List.objects.get(pk=item_id)
    task.delete()
    messages.success(request, ('The task has been deleted successfully!'))
    return redirect('weekly')

@login_required
def week_cross_off(request, item_id):
    task = List.objects.get(pk=item_id)
    task.completed = True
    task.save()
    messages.success(request, ('The task has been marked as completed successfully!'))
    return redirect('weekly')

@login_required
def weekuncross(request,item_id):
    task = List.objects.get(pk=item_id)
    task.completed = False
    task.save()
    messages.success(request, ('The task has been marked as incomplete successfully!'))
    return redirect('weekly')

@login_required
def tasks_today(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(due_date=today,completed=False, is_skipped=False )
    upcoming_tasks = tasks.count()
    messages.success(request, (' Here are the tasks you have today'))
    return render(request, 'upcoming.html', {'tasks': tasks,'upcoming_tasks':upcoming_tasks})

@login_required
def profile_pic(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile_pic.html', {'user': user})
    else:
        return render(request, 'profile_pic.html')

@login_required
def send_task_reminder(request):
    tasks = Task.objects.filter(completed=False, is_skipped=False)
    for task in tasks:
        time_delta = timezone.now() - task.created_at
        if task.remind_minutes and time_delta.total_seconds() >= task.remind_minutes * 60:
            task.save()
        else:
            messages.error(request, ('There are no tasks to send reminders for!'))
    return render(request,'messages.html' )

@login_required
def calendars(request, year=None, month=None):
    if not year and not month: #checks if both year and month are not provided
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
    else:
        year = int(year)
        month = int(month)

    cal = calendar.monthcalendar(year, month)
    tasks = Task.objects.filter(user=request.user, due_date__year=year, due_date__month=month)

    month_name = calendar.month_name[month]
    return render(request, 'calendar.html', {'tasks': tasks, 'cal': mark_safe(cal), 'month_name': month_name, 'next_month': month+1, 'prev_month': month-1})
