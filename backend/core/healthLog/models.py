from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE
from core.user.models import User
from core.healthLog.key import *
import datetime

class Symptom(models.Model):
    symptom = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    def __str__(self):
        return self.symptom

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
    writer = models.ForeignKey(User, related_name='theWriter', on_delete=CASCADE)
    def __str__(self):
        return self.title

class Log(models.Model):
    day = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    week = models.ForeignKey(Week, related_name='theWeek', on_delete=CASCADE)
    author = models.ForeignKey(User, related_name='theAuthor', on_delete=CASCADE)

    def __str__(self):
        return f'{self.day} - {self.title}'

class Mood(models.Model):
    tag = models.CharField(max_length=255)
    date = models.DateTimeField()
    mood = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    symptom = models.ForeignKey(Symptom, related_name='theSymptom', on_delete=CASCADE)
    log = models.ForeignKey(Log, related_name='theLog',on_delete=CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='UserMood', on_delete=CASCADE)

class Taken(models.Model):
    when = models.DateTimeField()
    dose = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    medication = models.ForeignKey(Medication, related_name='theMed', on_delete=CASCADE)
    day = models.ForeignKey(Log, related_name='theDay',on_delete=CASCADE, blank=True)
    member = models.ForeignKey(User, related_name='UserTaken', on_delete=CASCADE)

class Sugar(models.Model):
    time = models.DateTimeField()
    level = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    note = models.ForeignKey(Log, related_name='theNote',on_delete=CASCADE, blank=True)
    owner = models.ForeignKey(User, related_name='theOwner', on_delete=CASCADE)

class Patient(models.Model):
    patient = models.ForeignKey(User, related_name='thePatient', on_delete=CASCADE)
    provider = models.ForeignKey(User, related_name='theDr', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Food(models.Model):
    food = models.CharField(max_length=255)
    calories = models.CharField(max_length=255, default=0)
    date = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    theDay = models.ForeignKey(Log, related_name='toTheLog', on_delete=CASCADE)
    person = models.ForeignKey(User, related_name='thePerson', on_delete=CASCADE)