from django.db import models



class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)



    