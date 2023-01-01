from django.shortcuts import render, redirect
from django.contrib import messages
from healthApp.models import *


def index(request):
    if 'user_id'  not in request.session:
        return render(request, 'welcome.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        weeks = Week.objects.all().order_by('-updatedAt')
        logs = Day.objects.all().values()
        theId = request.session['user_id']
        print('userlogs', weeks, 'theId', theId)
        userLogs = False
        if weeks:
            print('hey there')
            for w in weeks:
                if w.user_id == theId:
                    userLogs=True
        else:
            userLogs = False
            print('sorry')
        context = {
            'user': user,
            'weeks': weeks,
            'logs': logs,
            'userLogs': userLogs,
        }
        print(user)
        return render(request, 'index.html', context)

# def exampleOne(request):
#     user = User.objects.filter(level=3).values()
#     weeks = Week.objects.all().order_by('-updatedAt')
#     logs = Day.objects.all().order_by('-updatedAt')
#     context = {
#         'user': user,
#         'weeks': weeks,
#         'logs': logs,
#     }
#     print(user)
#     return render(request, 'exampleOneIndex.html', context)

# def exampleTwo(request):
#     user = User.objects.filter(level=5).values()
#     weeks = Week.objects.all().order_by('-updatedAt')
#     logs = Day.objects.all().order_by('-updatedAt')
#     context = {
#         'user': user,
#         'weeks': weeks,
#         'logs': logs,
#     }
#     print(user)
#     return render(request, 'exampleTwoIndex.html', context)

# def exampleOneMood(request):
#         user = User.objects.filter(level=3).values()
#         symptoms = SymptomList.objects.all().values()
#         logs = Day.objects.all().order_by('-updatedAt')
#         context = {
#             'user': user,
#             'symptoms': symptoms,
#             'logs': logs
#         }
#         return render(request, 'exampleMood.html', context)

# def exampleTwoMood(request):
#         user = User.objects.filter(level=5).values()
#         symptoms = SymptomList.objects.all().values()
#         logs = Log.objects.all().order_by('-updatedAt')
#         context = {
#             'user': user,
#             'symptoms': symptoms,
#             'logs': logs
#         }
#         return render(request, 'exampleMood.html', context)

def about(request):
    if 'user_id' not in request.session:
        return render(request, 'about.html')
    else:
        return render(request, 'loggedAbout.html')
