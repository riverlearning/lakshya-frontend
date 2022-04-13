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
