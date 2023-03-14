from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *
from datetime import datetime


status = {
    "Api Status": "Running"
}

def apiBase(request):
    return JsonResponse(status, content_type="application/json")

def jsonAllData(request):
    users = list(User.objects.all().values())
    symptoms = list(Symptom.objects.all().values())
    medications = list(Medication.objects.all().values())
    weeks = list(Week.objects.all().values())
    logs = list(Log.objects.all().values())
    moods = list(Mood.objects.all().values())
    takens = list(Taken.objects.all().values())
    sugars = list(Sugar.objects.all().values())
    patients = list(Patient.objects.all().values())
    comments = list(Comment.objects.all().values())
    replies = list(Reply.objects.all().values())
    notes = list(Note.objects.all().values())
    context = {
        'users': users,
        'symptoms': symptoms,
        'medications': medications,
        'weeks': weeks,
        'logs': logs,
        'moods': moods,
        'takens': takens,
        'sugars': sugars,
        'patients': patients,
        'comments': comments,
        'replies': replies,
        'notes': notes,
    }
    return JsonResponse(context, content_type='application/json')

def jsonPcpData(request, user_id):
    users = list(User.objects.all().values())
    symptoms = list(Symptom.objects.all().values())
    medications = list(Medication.objects.all().values())
    theWeeks = list(Week.objects.all().order_by('-updatedAt').values())
    theLogs = list(Log.objects.all().values())
    theMoods = list(Mood.objects.all().values())
    theTaken = list(Taken.objects.all().values())
    theSugars = list(Sugar.objects.all().values())
    user = []
    for row in users:
        if row['id'] == user_id:
            user.append(row)
    weeks = []
    for row in theWeeks:
        if row['writer_id'] == user_id:
            weeks.append(row)
    logs = []
    for row in theLogs:
        if row['author_id'] == user_id:
            logs.append(row)
    moods = []
    for row in theMoods:
        if row['user_id'] == user_id:
            moods.append(row)
    takens = []
    for row in theTaken:
        if row['member_id'] == user_id:
            takens.append(row)
    sugars = []
    for row in theSugars:
        if row['owner_id'] == user_id:
            sugars.append(row)
    context = {
        'user': user,
        'symptoms': symptoms,
        'medications': medications,
        'weeks': weeks,
        'logs': logs,
        'moods': moods,
        'takens': takens,
        'sugars': sugars,
    }
    return JsonResponse(context, safe = False, content_type='application/json')

def jsonMentalData(request, user_id):
    users = list(User.objects.all().values())
    symptoms = list(Symptom.objects.all().values())
    theWeeks = list(Week.objects.all().order_by('-updatedAt').values())
    theLogs = list(Log.objects.all().values())
    theMoods = list(Mood.objects.all().values())
    user = []
    for row in users:
        if row['id'] == user_id:
            user.append(row)
    weeks = []
    for row in theWeeks:
        if row['writer_id'] == user_id:
            weeks.append(row)
    logs = []
    for row in theLogs:
        if row['author_id'] == user_id:
            logs.append(row)
    moods = []
    for row in theMoods:
        if row['user_id'] == user_id:
            moods.append(row)
    context = {
        'user': user,
        'symptoms': symptoms,
        'weeks': weeks,
        'logs': logs,
        'moods': moods,
    }
    return JsonResponse(context, safe = False, content_type='application/json')