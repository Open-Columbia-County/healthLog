from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *


def index(request):
    if 'user_id'  not in request.session:
        return render(request, 'welcome.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        weeks = Week.objects.all().order_by('-updatedAt')
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'weeks': weeks,
            'logs': logs,
        }
        print(user)
        return render(request, 'index.html', context)

def exampleOne(request):
    user = User.objects.filter(level=3).values()
    profiles = Profile.objects.all().values()
    weeks = Week.objects.all().order_by('-updatedAt')
    logs = Log.objects.all().order_by('-updatedAt')
    context = {
        'user': user,
        'weeks': weeks,
        'logs': logs,
    }
    print(user)
    return render(request, 'exampleOneIndex.html', context)

def exampleTwo(request):
    user = User.objects.filter(level=5).values()
    profiles = Profile.objects.all().values()
    weeks = Week.objects.all().order_by('-updatedAt')
    logs = Log.objects.all().order_by('-updatedAt')
    context = {
        'user': user,
        'weeks': weeks,
        'logs': logs,
    }
    print(user)
    return render(request, 'exampleTwoIndex.html', context)

def exampleOneMood(request):
        user = User.objects.filter(level=3).values()
        symptoms = Symptom.objects.all().values()
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'symptoms': symptoms,
            'logs': logs
        }
        return render(request, 'exampleMood.html', context)

def exampleTwoMood(request):
        user = User.objects.filter(level=5).values()
        symptoms = Symptom.objects.all().values()
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'symptoms': symptoms,
            'logs': logs
        }
        return render(request, 'exampleMood.html', context)
        return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
