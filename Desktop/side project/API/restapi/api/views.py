from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serislizers import TaskSerializers
from .models import Task

@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'List':'list'
    }
    return Response(api_url)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    s = TaskSerializers(tasks, many=True)
    return Response(s.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id = pk)
    s = TaskSerializers(tasks, many=False)
    return Response(s.data)

@api_view(['POST'])
def taskCreate(request):
    new = TaskSerializers(data=request.data)

    if new.is_valid():
        new.save()
    return Response(new.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id = pk)
    s = TaskSerializers(instance=task,data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item succesfully deleted")