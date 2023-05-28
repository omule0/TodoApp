from django.core.mail import send_mail
from django.conf import Settings
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskingForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

# send email to user
            send_mail(
                'New Task Created',#message header/subject
                'A new task has been created in your to-do list.',# body message
                'dopio8081@gmail.com', # replace with your email address 
                [request.user.email],   # send email to logged-in user
                fail_silently=False,
            )
                    return redirect('task_list')
    else:
        form = TaskingForm()
    return render(request, 'task_form.html', {'form': form, 'form_title': 'form_title'})
