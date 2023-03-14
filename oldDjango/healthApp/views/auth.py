from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *
import bcrypt

def logReg(request):
    if 'user_id'  not in request.session:
        return render(request, 'logReg.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        logs = Log.objects.all().order_by('-updatedAt')
        context = {
            'user': user,
            'logs': logs,
        }
        return render(request, 'index.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/logReg/')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/logReg/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/logReg/')

def register(request):
    if request.method == 'GET':
        return redirect('/logReg/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    if newUser.id == 1:
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.level=24
        toUpdate.save()
        messages.error(request, "Welcome Admin Member")
        return redirect('/')
    if newUser.firstName == "Example":
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.level=3
        toUpdate.save()
        messages.error(request, "Welcome Example Account Member")
        return redirect('/')
    if newUser.firstName == "Diabetic":
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.level=5
        toUpdate.save()
        messages.error(request, "Welcome Diabetic Account Member")
    else:
        messages.error(request, "Welcome New Member")
        return redirect('/')

def profileDash(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else: 
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values()
        providers = Patient.objects.all().values()
        context = {
            'user': user,
            'users': users,
            'providers': providers,
        }
        return render(request, 'profile/profile.html', context)

def editProfile(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'profile/editProfile.html', context)

def updateName(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    toUpdate.firstName=request.POST['firstName']
    toUpdate.lastName=request.POST['lastName']
    toUpdate.save()
    messages.error(request, "Name has been updated")
    return redirect('/user/dashboard/')

def updateUsername(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    errors = User.objects.updateUsername(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect(f'/user/{user_id}/edit/')
    toUpdate.username=request.POST['username']
    toUpdate.save()
    messages.error(request, "Username updated")
    return redirect('/user/dashboard/')

def updateEmail(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    errors = User.objects.updateEmail(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect(f'/user/{user_id}/edit/')
    toUpdate.email=request.POST['email']
    toUpdate.save()
    messages.error(request, 'Email updated')
    return redirect('/user/dashboard/')

def updatePassword(request, user_id):
    pass

def updateImage(request, user_id):
    pass

def updateDiabetic(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    toUpdate.profile.diabetic=request.POST['diabetic']
    toUpdate.save()
    messages.error(request, 'Updated Diabetic Question')
    return redirect('/user/dashboard/')

def generatePrint(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'profile/generatePrint.html', context)

def profileData(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        weeks = Week.objects.all().values()
        logs = Log.objects.all().values()
        meds = Medication.objects.all().values()
        symptoms = Symptom.objects.all().values()
        moods = Mood.objects.all().values()
        taken = Taken.objects.all().values()
        sugars = Sugar.objects.all().values()
        context = {
            'user': user,
            'weeks': weeks,
            'logs': logs,
            'meds': meds,
            'symptoms': symptoms,
            'moods': moods,
            'taken': taken,
            'sugars': sugars,
        }
        return render(request, 'profile/profileData.html', context)

def messagePortal(request):
    pass

def addDoctor(request):
    Patient.objects.create(
        patient_id = request.POST['patient'],
        provider_id = request.POST['provider'],
    )
    messages.error(request, "You have added your Provider")
    return redirect('/user/dashboard/')

def updateToProvider(request, user_id):
    toUpdate=User.objects.get(id=user_id)
    errors = User.objects.updateProvider(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect(f'/user/{user_id}/edit/')
    toUpdate.level=8
    toUpdate.save()
    messages.error(request, "Thank you for registering as a Provider")
    return redirect('/user/dashboard/')

