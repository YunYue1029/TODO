from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task
from django.utils import timezone
from django.utils.dateparse import parse_datetime

def index(request):
    tasks = Task.objects.all()
    return render(request, "todolist/index.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task = Task.objects.create(title=title)
        return JsonResponse({"id": task.id, "title": task.title, "completed": task.completed})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({"id": task.id, "completed": task.completed})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({"id": task_id})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        time = request.POST.get("time")
        
        deadline_str = f"{date}T{time}" if date and time else None
        deadline = parse_datetime(deadline_str) if deadline_str else None

        if deadline and timezone.is_naive(deadline):
            deadline = timezone.make_aware(deadline)

        task = Task.objects.create(title=title, deadline=deadline)

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": timezone.localtime(task.created_at).strftime("%Y-%m-%d %H:%M"),
            "deadline": timezone.localtime(task.deadline).strftime("%Y-%m-%d %H:%M") if task.deadline else None
        })