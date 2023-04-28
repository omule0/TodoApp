@login_required
def task_skip(request, pk):
    task = get_object_or_404(Tasking, pk=pk)
    task.skipped = True
    task.save()
    return redirect('task_list')