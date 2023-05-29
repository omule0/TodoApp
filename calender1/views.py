from django.shortcuts import render
from .forms import EventForm
from .models import Event

def index(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    events = Event.objects.all()
    context = {'form': form, 'events': events}
    return render(request, 'index.html', context)


def index(request):
    return render(request, 'index.html')
