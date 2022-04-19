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

def createTask(request):
    return render(request, 'frontend/create-task.html')

def managerEvaluation(request):
    return render(request, 'frontend/manager-evaluation.html')

def ownerEvaluation(request):
    return render(request, 'frontend/owner-evaluation.html')

def salaryReport(request):
    return render(request, 'frontend/salary-report.html')

def internalProjects(request):
    return render(request, 'frontend/internal-projects.html')

def strategicGoals(request):
    return render(request, 'frontend/strategic-goals.html')

def mission(request):
    return render(request, 'frontend/mission.html')

def organizationChart(request):
    return render(request, 'frontend/organization-chart.html')

def createStrategy(request):
    return render(request, 'frontend/create-strategy.html')

def createInternalProject(request):
    return render(request, 'frontend/create-internal-project.html')

def employees(request):
    return render(request, 'frontend/employees.html')

def departments(request):
    return render(request, 'frontend/departments.html')

def createNewDepartment(request):
    return render(request, 'frontend/create-new-department.html')

def roles(request):
    return render(request, 'frontend/roles.html')

def createNewRole(request):
    return render(request, 'frontend/create-new-role.html')

def jobRequirementsKRA(request):
    return render(request, 'frontend/job-requirements-kra.html')

def createNewJobRequirement(request):
    return render(request, 'frontend/create-new-job-requirement.html')

def grades(request):
    return render(request, 'frontend/grades.html')

def createNewGrade(request):
    return render(request, 'frontend/create-new-grade.html')   

def appraisalCycle(request):
    return render(request, 'frontend/appraisal-cycle.html')

def createNewAppraisalCycle(request):
    return render(request, 'frontend/create-new-appraisal-cycle.html')

def kpi(request):
    return render(request, 'frontend/kpi.html')

def createNewKPI(request):
    return render(request, 'frontend/create-new-kpi.html')    

def trainingAdmin(request):
    return render(request, 'frontend/training-admin.html') 

def createNewTraining(request):
    return render(request, 'frontend/create-new-training.html') 

def trainers(request):
    return render(request, 'frontend/trainers.html') 

def createNewTrainer(request):
    return render(request, 'frontend/create-new-trainer.html')

def topics(request):
    return render(request, 'frontend/topics.html')

def createNewTopic(request):
    return render(request, 'frontend/create-new-topic.html')

def personWiseReport(request):
    return render(request, 'frontend/person-wise-report.html')

