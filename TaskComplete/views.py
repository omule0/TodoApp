@login_required
def task_complete(request, pk):
    task = get_object_or_404(Tasking, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')