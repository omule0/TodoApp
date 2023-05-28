
            send_mail(
                'New Task Created',
                'A new task has been created in your to-do list.',
                'dopio8081@gmail.com',  
                [request.user.email],  
                fail_silently=False,
            )