from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Public
    path('', views.index),
    # path('exampleOne/dashboard/', views.exampleOne),
    # path('exampleTwo/dashboard/', views.exampleTwo),
    # path('exampleOne/mood/', views.exampleOneMood),
    # path('exampleTwo/mood/', views.exampleTwoMood),
    path('about/', views.about),
    # Auth
    path('logReg/', views.logReg),
    path('login/', views.login),
    path('reg/', views.register),
    path('logout/', views.logout),
    # path('user/dashboard/', views.profileDash),
    # path('user/<int:user_id>/generatePrint/', views.generatePrint),
    # path('user/<int:user_id>/data/', views.profileData),
    # path('user/<int:user_id>/edit/', views.editProfile),
    # path('user/<int:user_id>/updateEmail/', views.updateEmail),
    # path('user/<int:user_id>/updateUsername/', views.updateUsername),
    # path('user/<int:user_id>/updateDiabetic/', views.updateDiabetic),
    # path('user/<int:user_id>/updateFood/', views.updateFood),
    # path('user/<int:user_id>/updateSleep/', views.updateSleep),
    # path('user/<int:user_id>/updateSleepApp/', views.updateSleepApp),
    # path('user/<int:user_id>/updatePassword/', views.updatePassword),
    # path('user/addDoctor/', views.addDoctor),
    # path('user/<int:user_id>/updateProvider/', views.updateToProvider),
    # SymptomList
    # path('symptom-list/', views.symptomList),
    # path('symptom-list/create/', views.createSymptomList),
    # path('symptom-list/<int:symptomList_id>/update/', views.updateSymptomList),
    # path('symptom-list/<int:symptomList_id>/delete/', views.deleteSymptomList),
    # Week
    path('week/', views.addWeek),
    path('week/create/', views.createWeek),
    path('week/<int:week_id>/view/', views.viewWeek),
    path('week/<int:week_id>/delete/', views.deleteWeek),
    # Day
    path('day/', views.addDay),
    path('day/create/', views.createDay),
    # path('day/<int:day_id>/view/', views.viewDay),
    # path('day/<int:day_id>/update/', views.updateDay),
    # path('day/<int:day_id>/delete/', views.deleteDay),
    # Feeling
    # path('feeling/', views.addFeeling),
    # path('feeling/create/', views.createFeeling),
    # path('feeling/<int:feeling_id>/update/', views.updateFeeling),
    # path('feeling/<int:feeling_id>/delete/', views.deleteFeeling),
    # Symptom
    # path('symptom/', views.symptom),
    # path('symptom/create/', views.createSymptom),
    # path('symptom/<int:symptom_id>/update/', views.updateSymptom),
    # path('symptom/<int:symptom_id>/delete/', views.deleteSymptom),
    # Medication
    # path('medication-list/', views.addNewMedication),
    # path('medication/', views.addMedication),
    # path('medication-list/create/', views.createMed),
    # path('medication/create/', views.createTaken),
    # path('medication/<int:medication_id>/edit/', views.editMedication),
    # path('medication/<int:medication_id>/update/', views.updateMedication),
    # path('medication/<int:medication_id>/delete/', views.deleteMedication),
    # Sugar
    # path('sugar/', views.addSugar),
    # path('sugar/create/', views.createSugar),
    # path('sugar/<int:sugar_id>/edit/', views.editSugar),
    # path('sugar/<int:sugar_id>/update/', views.updateSugar),
    # path('sugar/<int:sugar_id>/delete/', views.deleteSugar),
    # Food
    # path('food/', views.addFood),
    # path('food/create/', views.createFood),
    # path('food/<int:food_id>/edit/', views.editFood),
    # path('food/<int:food_id>/update/', views.updateFood),
    # path('food/<int:food_id>/delete/', views.deleteFood),
    # Sleep
    # path('sleep/', views.addSleep),
    # path('sleep/create/', views.createSleep),
    # path('sleep/<int:sleep_id>/edit/', views.editSleep),
    # path('sleep/<int:sleep_id>/update/', views.updateSleep),
    # path('sleep/<int:sleep_id>/delete/', views.deleteSleep),
    # Tracker
    # path('tracker/', views.addTracker),
    # path('tracker/create/', views.createTracker),
    # path('tracker/<int:tracker_id>/edit/', views.editTracker),
    # path('tracker/<int:tracker_id>/update/', views.updateTracker),
    # path('tracker/<int:tracker_id>/delete/', views.deleteTracker),
    # Provider
    # path('provider/dashboard/', views.providerDash),
    # path('provider/notes/', views.providerNotes),
    # path('provider/notes/<int:note_id>/view/', views.viewNote),
    # path('provider/patient/<int:user_id>/view/', views.viewPatient),
    # path('provider/patient/<int:user_id>/addNote/', views.addNote),
    # path('provider/patient/<int:user_id>/createNote/', views.createNote),
    # path('provider/notes/<int:note_id>/update/', views.updateNote),
    # path('provider/notes/<int:note_id>/delete/', views.deleteNote),
    # Messages
    # path('user/messages/', views.viewAllMessages),
    # path('user/portal/', views.messagePortal),
    # path('user/messages/<int:message_id>/view/', views.viewMessage),
    # path('user/messages/add/', views.addMessage),
    # path('user/messages/create/', views.createMessage),
    # path('user/messages/<int:message_id>/addReply/', views.createReply),
    # path('user/messages/<int:message_id>/update/', views.updateMessage),
    # path('user/messages/<int:reply_id>/updateReply/', views.updateReply),
    # path('user/messages/<int:message_id>/delete/', views.deleteMessage),
    # path('user/messages/<int:reply_id>/delete/', views.deleteReply),
    # Admin
    # path('theAdmin/', views.theAdmin),
    # path('theAdmin/user/', views.adminUsers),
    # path('theAdmin/user/<int:user_id>/delete/', views.deleteUser),
    # path('theAdmin/user/<int:user_id>/makeAdmin/', views.makeAdmin),
    # path('theAdmin/user/<int:user_id>/makeProvider/', views.makeProvider),
    # path('theAdmin/user/<int:user_id>/makeSuperAdmin/', views.makeSuperAdmin),
    # JSON
    # path('json/', views.apiBase),
    # path('json/data/', views.jsonAllData),
    # path('json/<int:user_id>/pcpData/', views.jsonPcpData),
    # path('json/<int:user_id>/mentalData/', views.jsonMentalData),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)