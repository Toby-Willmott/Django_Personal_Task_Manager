from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.decorators.http import require_POST

@login_required
def index(request):
    user_tasks = Task.objects.filter(owner=request.user)
    return render(request, "taskManager/index.html", {"user_tasks": user_tasks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'taskManager/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'taskManager/login.html')

@require_POST
@login_required
def update_tasks(request):
    completed_ids = request.POST.getlist('completed_tasks')
    user_tasks = Task.objects.filter(owner=request.user)

    for task in user_tasks:
        task.completed = str(task.id) in completed_ids
        task.save()

    return redirect('index')

@require_POST
@login_required
def add_task(request):
    title = request.POST.get('title')
    description = request.POST.get('description', '')

    if title:
        Task.objects.create(
            title=title,
            description=description,
            owner=request.user
        )
    return redirect('index')
