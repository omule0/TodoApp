from django.core.mail import send_mail
from django.conf import Settings








# send email to user
            send_mail(
                'New Task Created',#message header/subject
                'A new task has been created in your to-do list.',# body message
                'dopio8081@gmail.com', # replace with your email address 
                [request.user.email],   # send email to logged-in user
                fail_silently=False,
            )