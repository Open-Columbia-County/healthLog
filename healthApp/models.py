from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from healthApp.key import *
import datetime

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email is already registered'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

    def updatePassword(self, form):
        errors = {}
        if form['password'] != form['confirm']:
            errors['password'] = "Passwords do not match"
        return errors

    def updateUsername(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'
        return errors
    
    def updateEmail(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email is already registered'
        return errors

    def updateProvider(self, form):
        errors = {}
        if form['REGCODE'] != PROVIDERKEY:
            errors['REGCODE'] = 'Invalid Provider Registration Code'
        return errors
    
    def updateNurse(self, form):
        errors = {}
        if form['REGCODE'] != CAREGIVERKEY:
            errors['REGCODE'] = 'Invalid CareGiver or Nurse Code'
        return errors

    def updateAdmin(self, form):
        errors = {}
        if form['REGCODE'] != ADMINKEY:
            errors['REGCODE'] = 'Invalid Admin Registration Code'
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=0)

    objects = UserManager()

    loggedOn = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    medication = models.BooleanField(default=0)
    diabetic = models.BooleanField(default=0)
    food = models.BooleanField(default=0)
    sleep = models.BooleanField(default=0)
    sleepApp = models.BooleanField(default=0)
    def __str__(self):
        return f'{self.user.username} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class SymptomList(models.Model):
    symptom = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    def __str__(self):
        return self.symptom
        
class FoodList(models.Model):
    food = models.CharField(max_length=255)
    def __str__(self):
        return self.food

class Medication(models.Model):
    name = models.CharField(max_length=255)
    freq = models.CharField(max_length=255, default='daily')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Week(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='theUser', on_delete=CASCADE)
    def __str__(self):
        return self.title

class Day(models.Model):
    day = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    week = models.ForeignKey(Week, related_name='theWeek', on_delete=CASCADE)
    author = models.ForeignKey(User, related_name='theAuthor', on_delete=CASCADE)

    def __str__(self):
        return f'{self.day} - {self.title}'
    def dayHeading(self):
        return f'{self.day} - {self.title}'

class Feeling(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    feeling = models.IntegerField()
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    log = models.ForeignKey(Day, related_name='theLog',on_delete=CASCADE, blank=True)
    writer = models.ForeignKey(User, related_name='theWriter', on_delete=CASCADE)

class Symptom(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    symptom = models.ForeignKey(SymptomList, related_name='theSymptom',on_delete=CASCADE)
    post = models.ForeignKey(Day, related_name='thePost', on_delete=CASCADE)
    poster = models.ForeignKey(User, related_name='thePoster', on_delete=CASCADE)

class Taken(models.Model):
    date = models.DateTimeField()
    dose = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    medication = models.ForeignKey(Medication, related_name='theMed', on_delete=CASCADE)
    blog = models.ForeignKey(Day, related_name='theBlog',on_delete=CASCADE, blank=True)
    member = models.ForeignKey(User, related_name='theMember', on_delete=CASCADE)

class Sugar(models.Model):
    time = models.DateTimeField()
    level = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    entry = models.ForeignKey(Day, related_name='theEntry',on_delete=CASCADE, blank=True)
    owner = models.ForeignKey(User, related_name='theOwner', on_delete=CASCADE)

class Food(models.Model):
    food = models.ForeignKey(FoodList, related_name='theFood', on_delete=CASCADE)
    calories = models.IntegerField()
    date = models.DateTimeField()
    meal = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    record = models.ForeignKey(Day, related_name='theRecord', on_delete=CASCADE)
    person = models.ForeignKey(User, related_name='thePerson', on_delete=CASCADE)

class Sleep(models.Model):
    date = models.DateField()
    sleep = models.TimeField()
    wake = models.TimeField()
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    sleeper = models.ForeignKey(User, related_name='theSleeper', on_delete=CASCADE)
    journal = models.ForeignKey(Day, related_name='theJournal', on_delete=CASCADE)

class Tracker(models.Model):
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='TrackerImgs', default='med.jpg')
    entry = models.ForeignKey(Sleep, related_name='theEntry', on_delete=CASCADE)
    human = models.ForeignKey(User, related_name='theHuman', on_delete=CASCADE)

class Provider(models.Model):
    patient = models.ForeignKey(User, related_name='thePatient', on_delete=CASCADE)
    provider = models.ForeignKey(User, related_name='theDr', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    read = models.DateTimeField(auto_now=True)
    toUser = models.ForeignKey(User, related_name='userTo', on_delete=CASCADE)
    fromUser = models.ForeignKey(User, related_name='userFrom', on_delete=CASCADE)
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    replyToUser = models.ForeignKey(User, related_name='userToReply', on_delete=CASCADE)
    replyFromUser = models.ForeignKey(User, related_name='userFromReply', on_delete=CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey(Comment, related_name='theReply', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    about = models.ForeignKey(User, related_name='aboutUser', on_delete=CASCADE)
    dr = models.ForeignKey(User, related_name='drNote', on_delete=CASCADE)
    note = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)