from django.conf import settings
import json
from todo.models import Task
from django.utils import timezone
from todo.models import Task
from django.core.mail import send_mail



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