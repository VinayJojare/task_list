from django.contrib import admin
from django.urls import path
from class_based_app.views import *
from . import views


urlpatterns = [

    path('', views.TaskList.as_view(), name = 'task'),
    path('taskcompleted/<int:task_id>', views.TaskCompleted.as_view(), name='updated' ),
    path('taskdelete/<int:task_id>', views.TaskDelete.as_view(), name='delete'),
    path('deleteall/', views.DeleteAll.as_view(), name='reset'),
    ]