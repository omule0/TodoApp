from django.conf import settings
import json
from django.utils import timezone
from todo.models import Task ,List
from django.core.mail import send_mail
from datetime import datetime, timedelta, timezone


def send_reminder():
    tasks = Task.objects.filter(completed=False, is_skipped=False,email_sent=False)
    sent_tasks = {}
    
    for task in tasks:
        time_delta = datetime.now(timezone.utc) - task.created_at
        if task.remind_minutes and time_delta.total_seconds() > task.remind_minutes * 60:
            task_url = 'https://sdp-l45pybnoqq-uc.a.run.app/home/upcoming/'
            send_mail(
                'Reminder: {} is due soon!'.format(task.name),
                'This is a reminder that your task "{}" is due in {} minute. Click here to view the task: {}'.format(
                    task.name, task.remind_minutes,task_url
                ),
                'melvinmichael348@gmail.com',
                [task.user.email],
                fail_silently=False,
            )
            task.email_sent = True
            sent_tasks[task.user.email] = True
            task.save()

def mark_skipped_tasks():
    current_datetime = datetime.now()
    tasks = Task.objects.all()
    for task in tasks:
        if not task.completed and task.due_date and task.due_time:
            due_datetime = datetime.combine(task.due_date, task.due_time)
            if due_datetime < current_datetime:
                task.is_skipped = True
                task.save() 
                   
def delete_old_tasks():
    current_time = datetime.now(timezone.utc)
    tasks = Task.objects.all()
    for task in tasks:
        time_difference = current_time - task.created_at.replace(tzinfo=timezone.utc)
        if time_difference.days > 7:
            task.delete()    



def delete_old_weekly_tasks():
    # Calculate the date threshold for deleting old weekly tasks
    threshold_date = datetime.now().date() - timedelta(days=7)  # Delete tasks older than 7 days

    # Retrieve and delete the old weekly tasks
    old_weekly_tasks = List.objects.filter(week_of__lt=threshold_date)
    old_weekly_tasks.delete() 