from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def view_tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    context = {
        "tasks": tasks,
    }
    return render(request, 'todo/view_tasks.html', context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('view_tasks')
    else:
        form = TaskForm()
        context = {
            "form": form,
        }
        return render(request, 'todo/create_task.html', context)


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('view_tasks')