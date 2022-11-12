from rest_framework import serializers
from healthApp.models import *
# from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'username', 'password', 'level', 'loggedOn', 'createdAt', 'updatedAt']
        read_only_field = ['createdAt', 'updatedAt']


# class RegisterSerializer(UserSerializer):
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
#     username = serializers.CharField(required=True, write_only=True, max_length=128)

#     class Meta:
#         model = User
#         fields = ['id', 'firstName', 'lastName', 'level', 'loggedOn','username', 'email', 'password', 'createdAt', 'updatedAt']

#     def create(self, validated_data):
#         try:
#             user = User.objects.get(username=validated_data['username'])
#         except ObjectDoesNotExist:
#             user = User.objects.create_user(**validated_data)
#         return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'diabetic']

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'symptom', 'info']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'freq', 'createdAt', 'updatedAt']

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['id', 'medication', 'image']

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

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'patient', 'provider', 'createdAt', 'updatedAt']