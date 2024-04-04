from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task


class TaskList(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_page.html', {'tasks':tasks})
    
    def post(self, request):
        task_name = request.POST.get('task_name')
        description = request.POST.get('description')

        task = Task.objects.create(task_name=task_name, description=description)
        task.save()
        return redirect('task')
    

class TaskCompleted(View):

    def post(self, request, task_id):
        complete = get_object_or_404(Task, pk=task_id)
        complete.completed = True
        complete.save()
        return redirect('task')
    


class TaskDelete(View):

    def post(self, request, task_id):
        delete = get_object_or_404(Task, pk=task_id)
        delete.delete()
        return redirect('task')
    



class DeleteAll(View):
    def post(self, request):
        Task.objects.all().delete()
        return redirect('task')

