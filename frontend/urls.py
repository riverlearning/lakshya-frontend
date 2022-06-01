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
    path('create-task', views.createTask, name="createTask"),
    path('manager-evaluation', views.managerEvaluation, name="managerEvaluation"),
    path('owner-evaluation', views.ownerEvaluation, name="ownerEvaluation"),
    path('salary-report', views.salaryReport, name="salaryReport"),
    path('internal-projects', views.internalProjects, name="internalProjects"),
    path('strategic-goals', views.strategicGoals, name="strategicGoals"),
    path('mission', views.mission, name="mission"),
    path('organization-chart', views.organizationChart, name="organizationChart"),
    path('create-strategy', views.createStrategy, name="createStrategy"),
    path('create-internal-project', views.createInternalProject, name="createInternalProject"),
    path('employees', views.employees, name="employees"),
    path('departments', views.departments, name="departments"),
    path('create-new-department', views.createNewDepartment, name="createNewDepartment"),
    path('roles', views.roles, name="roles"),
    path('create-new-role', views.createNewRole, name="createNewRole"),
    path('job-requirements-kra', views.jobRequirementsKRA, name="jobRequirementsKRA"),
    path('create-new-job-requirement', views.createNewJobRequirement, name="createNewJobRequirement"),
    path('grades', views.grades, name="grades"),
    path('create-new-grade', views.createNewGrade, name="createNewGrade"),
    path('appraisal-cycle', views.appraisalCycle, name="appraisalCycle"),
    path('create-new-appraisal-cycle', views.createNewAppraisalCycle, name="createNewAppraisalCycle"),
    path('kpi', views.kpi, name="kpi"),
    path('create-new-kpi', views.createNewKPI, name="createNewKPI"),
    path('training-admin', views.trainingAdmin, name="trainingAdmin"),
    path('create-new-training', views.createNewTraining, name="createNewTraining"),
    path('trainers', views.trainers, name="trainers"),
    path('create-new-trainer', views.createNewTrainer, name="createNewTrainer"),
    path('topics', views.topics, name="topics"),
    path('create-new-topic', views.createNewTopic, name="createNewTopic"),
    path('person-wise-report', views.personWiseReport, name="personWiseReport"),
    path('role-jr-mapping', views.roleJRMapping, name="roleJRMapping"),
    path('employee-jr-mapping', views.employeeJRMapping, name="employeeJRMapping"),
    path('monthly-training-report', views.monthlyTrainingReport, name="monthlyTrainingReport"),
    path('edit-my-tasks', views.editMyTasks, name="editMyTasks"),
    path('add-comment', views.addComment, name="addComment"),
    path('edit-tasks-allocated', views.editTasksAllocated, name="editTasksAllocated"),
    path('assess-closed-tasks', views.assessClosedTasks, name="assessClosedTasks"),
    path('manager-evaluate-now', views.managerEvaluateNow, name="managerEvaluateNow"),
    path('owner-evaluate-now', views.ownerEvaluateNow, name="ownerEvaluateNow"),
    path('update-employee', views.updateEmployee, name="updateEmployee"),
    path('update-department', views.updateDepartment, name="updateDepartment"),
    path('update-role', views.updateRole, name="updateRole"),
    path('update-job-requirement', views.updateJobRequirement, name="updateJobRequirement"),
    path('update-grade', views.updateGrade, name="updateGrade"),
    path('update-appraisal-cycle', views.updateAppraisalCycle, name="updateAppraisalCycle"),
    path('appraisal-report', views.appraisalReport, name="appraisalReport"),
    path('task-details', views.taskDetails, name="taskDetails"),
    path('update-kpi', views.updateKPI, name="updateKPI"),
    path('kpi-data', views.kpiData, name="kpiData"),
    path('appraisal-details', views.appraisalDetails, name="appraisalDetails"),
    path('edit-job-requirement', views.editJobRequirement, name="editJobRequirement"),
    path('add-job-requirement', views.addJobRequirement, name="addJobRequirement"),
]