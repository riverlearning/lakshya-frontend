from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('task', views.task, name="task"),
    path('task-allocated', views.taskAllocated, name="taskAllocated"),
    path('task-closed', views.taskClosed, name="taskClosed"),
    path('task-assess', views.taskAssess, name="taskAssess"),
]