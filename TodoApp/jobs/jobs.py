from django.conf import settings
import json
from todo.models import Task
from django.utils import timezone
from todo.models import Task
from django.core.mail import send_mail
from datetime import datetime, timedelta, timezone
from django.contrib import messages


def send_reminder():
    print('okay')
    tasks = Task.objects.filter(completed=False, is_skipped=False)
    for task in tasks:
        time_delta = timezone.now() - task.created_at
        if task.remind_minutes and time_delta.total_seconds() > task.remind_minutes * 60:
            send_mail(
                'Reminder: {} is due soon!'.format(task.name),
                'This is a reminder that your task "{}" is due in {} minute.'.format(
                    task.name, task.remind_minutes
                ),
                'melvinmichael348@gmail.com',
                [task.user.email],
                fail_silently=False,
            )
            task.is_skipped = True  # Set to true so we don't send another reminder
            task.save()

def mark_skipped_tasks():
    print('yes')
    current_datetime = datetime.now()
    tasks = Task.objects.all()
    for task in tasks:
        if not task.completed and task.due_date and task.due_time:
            due_datetime = datetime.combine(task.due_date, task.due_time)
            if due_datetime < current_datetime:
                task.is_skipped = True
                task.save() 
                   
def delete_old_tasks():
    print('delete')
    current_time = datetime.now(timezone.utc)
    tasks = Task.objects.all()
    for task in tasks:
        time_difference = current_time - task.created_at.replace(tzinfo=timezone.utc)
        if time_difference.days > 7:
            task.delete()    