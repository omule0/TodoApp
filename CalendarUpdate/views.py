from django.utils.safestring import mark_safe
from django.utils import timezone
import calendar #imports Python's built-in calendar module
import datetime
@login_required
def task_list(request, year=None, month=None):
    if not year and not month: #checks if both year and month are not provided
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
    else:
        year = int(year)
        month = int(month)

    cal = calendar.monthcalendar(year, month)
    tasks = Tasking.objects.filter(user=request.user, due_date__year=year, due_date__month=month)

    month_name = calendar.month_name[month]
    return render(request, 'task_list.html', {'tasks': tasks, 'cal': mark_safe(cal), 'month_name': month_name, 'next_month': month+1, 'prev_month': month-1})
