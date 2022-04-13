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
    path('my-appraisal', views.myAppraisal, name="myAppraisal"),
    path('my-evaluation', views.myEvaluation, name="myEvaluation"),
    path('report-kpi-data', views.reportKPIData, name="reportKPIData"),
    path('performance-report', views.performanceReport, name="performanceReport"),
    path('kpi-report', views.kpiReport, name="kpiReport"),
    path('ifeel', views.iFeel, name="iFeel"),
    path('development-goals', views.developmentGoals, name="developmentGoals"),
    path('my-trainings', views.myTrainings, name="myTrainings"),
]