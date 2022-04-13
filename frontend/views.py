from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'frontend/index.html')

def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def task(request):
    return render(request, 'frontend/task.html')

def taskAllocated(request):
    return render(request, 'frontend/task-allocated.html')

def taskClosed(request):
    return render(request, 'frontend/task-closed.html')

def taskAssess(request):
    return render(request, 'frontend/task-assess.html')

def myAppraisal(request):
    return render(request, 'frontend/my-appraisal.html')

def myEvaluation(request):
    return render(request, 'frontend/my-evaluation.html')

def reportKPIData(request):
    return render(request, 'frontend/report-kpi-data.html')

def performanceReport(request):
    return render(request, 'frontend/performance-report.html')

def kpiReport(request):
    return render(request, 'frontend/kpi-report.html')    

def iFeel(request):
    return render(request, 'frontend/ifeel.html')

def developmentGoals(request):
    return render(request, 'frontend/development-goals.html')

def myTrainings(request):
    return render(request, 'frontend/my-trainings.html')

