from django.shortcuts import render, get_object_or_404
from .models import Task
# Create your views here.
from django.shortcuts import render, redirect
from .models import Task


def home(request):
    if request.method == 'POST':
        # Handle task creation when the form is submitted
        task_text = request.POST.get('new_task_text')
        if task_text:
            task = Task(title=task_text)
            task.save()
            return redirect('home')  # Redirect to the home page to display updated task list

    # Retrieve all tasks from the database
    tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks': tasks})
def remove_task(request, task_id):
    # Retrieve the task by ID or return a 404 error if it doesn't exist
    task = get_object_or_404(Task, id=task_id)

    # Delete the task from the database
    task.delete()

    return redirect('home')

