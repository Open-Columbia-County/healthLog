from rest_framework import serializers
from core.healthLog.models import *

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'symptom', 'info']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'freq', 'createdAt', 'updatedAt']

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ['id', 'title', 'createdAt', 'updatedAt', 'writer']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'day', 'title', 'content', 'createdAt', 'updatedAt', 'week', 'author']

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['id', 'tag', 'date', 'mood', 'createdAt', 'updatedAt', 'symptom', 'log', 'user']

class TakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taken
        fields = ['id', 'when', 'dose', 'createdAt', 'updatedAt', 'medication', 'day', 'member']

class SugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugar
        fields = ['id', 'time', 'level', 'createdAt', 'updatedAt', 'note', 'owner']

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient', 'provider', 'createdAt', 'updatedAt']