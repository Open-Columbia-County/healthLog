from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *

def symptoms(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        symptoms = Symptom.objects.all().values()
        context = {
            'user': user,
            'symptoms': symptoms,
        }
        return render(request, 'admin/symptoms.html', context)

def createSymptom(request):
    Symptom.objects.create(
        symptom=request.POST['symptom'],
        info=request.POST['info'],
    )
    messages.error(request, 'Symptom Created')
    return redirect('/symptom/')

def updateSymptom(request, symptom_id):
    toUpdate=Symptom.objects.get(id=symptom_id)
    toUpdate.symptom = request.POST['symptom']
    toUpdate.info = request.POST['info']
    toUpdate.save()
    messages.error(request, 'Symptom Updated')
    return redirect('/symptom/')

def deleteSymptom(request, symptom_id):
    toDelete=Symptom.objects.get(id=symptom_id)
    toDelete.delete()
    messages.error(request, 'Symptom Removed')
    return redirect('/symptom/')

def deleteUser(request, user_id):
    toDelete=User.objects.get(id=user_id)
    toDelete.delete()
    messages.error(request, 'User Removed')
    return redirect('/theAdmin/')

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        if user.level == 9:
            logCount = Log.objects.all().count()
            moodCount = Mood.objects.all().count()
            symptomCount = Symptom.objects.all().count()
            userCount = User.objects.all().count()
            context = {
                'user': user,
                'logCount': logCount,
                'moodCount': moodCount,
                'symptomCount': symptomCount,
                'userCount': userCount,
            }
            print("log count: ", logCount, "mood count: ", moodCount, "symptom count: ", symptomCount)
            return render(request, 'admin/theAdmin.html', context)
        else:
            messages.error(request, "Please log in with an admin account")
            return redirect('/')

def adminUsers(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values()
        if user.level == 9:
            context = {
                'user': user,
                'users': users,
            }
            return render(request, 'admin/allUsers.html', context)
        else:
            messages.error(request, "Please log in with an admin account")
            return redirect('/')

def makeAdmin(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    errors= User.objects.updateAdmin(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request,err)
            return redirect('/theAdmin/user/')
    toUpdate.level=9
    toUpdate.save()
    messages.error(request, "User was give admin rights")
    return redirect('/theAdmin/user/')

def makeSuperAdmin(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    errors= User.objects.updateAdmin(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request,err)
            return redirect('/theAdmin/user/')
    toUpdate.level=24
    toUpdate.save()
    messages.error(request, "User was give super admin rights")
    return redirect('/theAdmin/user/')

def makeProvider(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    toUpdate.level=8
    toUpdate.save()
    messages.error(request, "User updated to Provider")
    return redirect('/theAdmin/user/')

def editMedication(request, medication_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        med = Medication.objects.get(id=medication_id)
        if user.level == 9:
            context = {
                'user': user,
                'med': med,
            }
            return render(request, 'admin/editMedication.html', context)
        else:
            messages.error(request, "Please log in with an admin account")
            return redirect('/')
    
def updateMedication(request, medication_id):
    toUpdate=Medication.objects.get(id=medication_id)
    toUpdate.name = request.POST['name']
    toUpdate.dose = request.POST['dose']
    toUpdate.freq = request.POST['freq']
    toUpdate.save()
    messages.error(request, "Medication Updated")

