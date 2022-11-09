from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *
# import tools for react data serialization
from rest_framework.views import APIView
from healthApp.models import *
from rest_framework.response import Response
from healthApp.serializer import *


def addWeek(request):
    if 'user_id' not in request.session:
        message.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        weeks = Week.objects.all().values()
        context = {
            'user': user,
            'weeks': weeks,
        }
        return render(request, 'logs/createWeek.html', context)

def addLog(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        weeks = Week.objects.all().values()
        context = {
            'user': user,
            'weeks': weeks,
        }
        return render(request, 'logs/createLog.html', context)

def addMood(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        symptoms = Symptom.objects.all().values()
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'symptoms': symptoms,
            'logs': logs
        }
        return render(request, 'logs/createMood.html', context)

def addNewMedication(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        meds = Medication.objects.all().values()
        uploads = Upload.objects.all().values()
        context = {
            'user': user,
            'meds': meds,
            'uploads': uploads,
        }
        return render(request, 'createNewMed.html', context)

def addMedication(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        meds = Medication.objects.all().values()
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'meds': meds,
            'logs': logs,
        }
        return render(request, 'logs/createMed.html', context)

def addSugar(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'logs/createSugar.html', context)

def addMessage():
    pass

def createWeek(request):
    Week.objects.create(
        title=request.POST['title'],
        writer=User.objects.get(id=request.session['user_id']),
    )
    messages.error(request, 'Week Created')
    return redirect('/log/')

def createLog(request):
    Log.objects.create(
        day = request.POST['day'],
        title=request.POST['title'],
        content=request.POST['content'],
        week_id = request.POST['week'],
        author=User.objects.get(id=request.session['user_id']),
    )
    messages.error(request, 'Log Created')
    return redirect('/')

def createMood(request):
    Mood.objects.create(
        tag=request.POST['tag'],
        date=request.POST['date'],
        mood=request.POST['mood'],
        symptom_id=request.POST['symptom'],
        log_id=request.POST['log'],
        user_id=request.POST['user_id']
    )
    messages.error(request, 'Symptom Entry Created')
    return redirect('/')

def createMed(request):
    Medication.objects.create(
        name=request.POST['name'],
        freq=request.POST['freq'],
    )
    messages.error(request, 'Medication Added to list')
    return redirect('/add/medication/')

def createTaken(request):
    Taken.objects.create(
        when=request.POST['when'],
        dose=request.POST['dose'],
        medication_id=request.POST['medication'],
        day_id=request.POST['day'],
        member_id=request.POST['member'],
    )
    messages.error(request, 'Medication added to log')
    return redirect('/')

def createSugar(request):
    Sugar.objects.create(
        time=request.POST['time'],
        level=request.POST['level'],
        note_id=request.POST['note'],
        owner_id=request.POST['owner'],
    )
    messages.error(request, 'Entry saved to log')
    return redirect('/')

def createMessage(request):
    pass

def createReply(request, message_id):
    pass

def viewWeek(request, week_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        week = Week.objects.get(id=week_id)
        logs = Log.objects.all().values()
        moods = Mood.objects.all().values()
        symptoms = Symptom.objects.all().values()
        meds = Taken.objects.all().values()
        sugars = Sugar.objects.all().values()
        theMeds = Medication.objects.all().values()
        context = {
                'user': user,
                'week': week,
                'logs': logs,
                'moods': moods,
                'symptoms': symptoms,
                'meds': meds,
                'sugars': sugars,
                'theMeds': theMeds,
            }
        return render(request, 'logs/viewWeek.html', context)

def viewLog(request, log_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        log = Log.objects.get(id=log_id)
        moods = Mood.objects.all().values()
        symptoms = Symptom.objects.all().values()
        meds = Medication.objects.all().values()
        taken = Taken.objects.all().values()
        sugars = Sugar.objects.all().values()
        context = {
            'user': user,
            'log': log,
            'moods': moods,
            'symptoms': symptoms,
            'meds': meds,
            'taken': taken,
            'sugars': sugars,
        }
        # print('moods: ', moods)
        # print("symptoms: ", symptoms)
        return render(request, 'logs/viewLog.html', context)

def viewAllMessages(request):
    pass

def viewMessage(request, message_id):
    pass

def updateMood(request, mood_id):
    toUpdate=Mood.objects.get(id=mood_id)
    toUpdate.tag = request.POST['tag']
    toUpdate.date = request.POST['date']
    toUpdate.mood = request.POST['mood']
    toUpdate.symptom = request.POST['symptom']
    toUpdate.log_id = request.POST['log']
    toUpdate.user_id = request.POST['user_id']
    toUpdate.save()
    messages.error(request, 'Symptom Entry Updated')
    return redirect('/')

def updateLog(request, log_id):
    toUpdate=Log.objects.get(id=log_id)
    toUpdate.title = request.POST['title']
    toUpdate.content = request.POST['content']
    toUpdate.save()
    messages.error(request, 'Log Updated')
    return redirect(f'/log/{toUpdate.id}/view/')

def updateWeek(request, week_id):
    pass

def updateTaken(request, taken_id):
    pass

def updateSugar(request, sugar_id):
    pass

def updateMessage(request, message_id):
    pass

def updateReply(request, reply_id):
    pass

def deleteLog(request, log_id):
    toDelete=Log.objects.get(id=log_id)
    toDelete.delete()
    messages.error(request, 'Log Removed')
    return redirect('/')

def deleteMood(request, mood_id):
    toDelete=Mood.objects.get(id=mood_id)
    toDelete.delete()
    messages.error(request, 'Symptom Entry Removed')
    return redirect('/')

class ReactView(APIView):
    serializer_class = ReactSerializer
    # data is not being output in the browser, needs fixing - JH 07Nov22
    def get(self, request):
        data = [
            {'foodsLogged': data.foodsLogged,
            'totalCalories': data.totalCalories,
            'date': data.date
            }
            for data in Food.objects.all()
        ]
        return Response(data)



def deleteWeek(request, week_id):
    pass

def deleteTaken(request, taken_id):
    pass

def deleteSugar(request, sugar_id):
    pass

def removeProvider(request, user_id):
    pass

def deleteMessage(request, message_id):
    pass

def deleteReply(request, reply_id):
    pass
