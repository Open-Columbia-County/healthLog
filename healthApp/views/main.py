from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *


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

def addDay(request):
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
        return render(request, 'day/createDay.html', context)

def addFeeling(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Day.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'logs': logs
        }
        return render(request, 'feeling/createFeeling.html', context)

def addSymptom(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        symptoms = SymptomList.objects.all().values()
        logs = Day.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'symptoms': symptoms,
            'logs': logs
        }
        return render(request, 'feeling/createSymptom.html', context)

def addNewMedication(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        meds = Medication.objects.all().values()
        context = {
            'user': user,
            'meds': meds,
        }
        return render(request, 'createNewMed.html', context)

def addMedication(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        meds = Medication.objects.all().values()
        logs = Day.objects.all().values()
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
        logs = Day.objects.all().values()
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'logs/createSugar.html', context)

def addFood(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Day.objects.all().values()
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'logs/createFood.html', context)

def addSleep(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Day.objects.all().values()
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'logs/createSleep.html', context)

def addTracker(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Day.objects.all().values()
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'logs/createTracker.html', context)

def addMessage():
    pass

def createWeek(request):
    Week.objects.create(
        title=request.POST['title'],
        user=User.objects.get(id=request.session['user_id']),
    )
    messages.error(request, 'Week Created')
    return redirect('/log/')

def createDay(request):
    Day.objects.create(
        day = request.POST['day'],
        title=request.POST['title'],
        content=request.POST['content'],
        week_id = request.POST['week'],
        author=User.objects.get(id=request.session['user_id']),
    )
    messages.error(request, 'Log Created')
    return redirect('/')

def createFeeling(request):
    Feeling.objects.create(
        date=request.POST['date'],
        feeling=request.POST['feeling'],
        content=request.POST['content'],
        log_id=request.POST['log'],
        writer_id=request.POST['user_id']
    )
    messages.error(request, 'Entry Created')
    return redirect('/')

def createSymptom(request):
    Symptom.objects.create(
        date=request.POST['date'],
        content=request.POST['content'],
        symptom_id=request.POST['symptom'],
        post_id=request.POST['post'],
        poster_id=request.POST['poster']
    )
    messages.error(request, 'Entry Created')
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
        blog_id=request.POST['blog'],
        member_id=request.POST['member'],
    )
    messages.error(request, 'Medication added to log')
    return redirect('/')

def createSugar(request):
    Sugar.objects.create(
        time=request.POST['time'],
        level=request.POST['level'],
        entry_id=request.POST['entry'],
        owner_id=request.POST['owner'],
    )
    messages.error(request, 'Entry saved to log')
    return redirect('/')

def createFood(request):
    Food.objects.create(
        food=request.POST['food'],
        calories=request.POST['calories'],
        date=request.POST['date'],
        meal=request.POST['meal'],
        record_id=request.POST['record'],
        person_id=request.POST['person']
    )
    messages.error(request, 'Entry saved to log')
    return redirect('/')

def createSleep(request):
    Sleep.objects.create(
        date=request.POST['date'],
        sleep=request.POST['sleep'],
        wake=request.POST['wake'],
        content=request.POST['content'],
        sleeper_id=request.POST['sleeper'],
        journal_id=request.POST['journal']
    )
    message.error(request, 'Entry saved to log')
    return redirect('/')

def createTracker(request):
    Tracker.objects.create(
        date=request.POST['date'],
        content=request.POST['content'],
        image=request.POST['images'],
        entry_id=request.POST['entry'],
        human_id=request.POST['human']
    )
    message.error(request, 'Entry saved to Log')
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
        logs = Day.objects.all().values()
        moods = Feeling.objects.all().values()
        symptoms = Symptom.objects.all().values()
        symptomLists = SymptomList.objects.all().values()
        meds = Taken.objects.all().values()
        sugars = Sugar.objects.all().values()
        foods = Food.objects.all().values()
        sleeps = Sleep.objects.all().values()
        trackers = Trackers.objects.all().values()
        theMeds = Medication.objects.all().values()
        context = {
                'user': user,
                'week': week,
                'logs': logs,
                'moods': moods,
                'symptoms': symptoms,
                'symptomLists': symptomLists,
                'foods': foods,
                'sleeps': sleeps,
                'trackers': trackers,
                'meds': meds,
                'sugars': sugars,
                'theMeds': theMeds,
            }
        return render(request, 'logs/viewWeek.html', context)

def viewDay(request, day_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        log = Day.objects.get(id=day_id)
        moods = Feeling.objects.all().values()
        symptoms = Symptom.objects.all().values()
        symptomLists = SymptomList.objects.all().values()
        meds = Taken.objects.all().values()
        sugars = Sugar.objects.all().values()
        foods = Food.objects.all().values()
        sleeps = Sleep.objects.all().values()
        trackers = Trackers.objects.all().values()
        theMeds = Medication.objects.all().values()
        context = {
            'user': user,
            'log': log,
            'moods': moods,
            'symptoms': symptoms,
            'symptomLists': symptomLists,
            'foods': foods,
            'sleeps': sleeps,
            'trackers': trackers,
            'meds': meds,
            'sugars': sugars,
            'theMeds': theMeds,
        }
        # print('moods: ', moods)
        # print("symptoms: ", symptoms)
        return render(request, 'logs/viewLog.html', context)

def viewAllMessages(request):
    pass

def viewMessage(request, message_id):
    pass

def updateMood(request, mood_id):
    pass

def updateLog(request, log_id):
    pass

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
    pass

def deleteMood(request, mood_id):
    pass

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