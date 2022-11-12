from core.healthLog.serializers import *
from core.user.models import *
from core.healthLog.models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class SymptomViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer

    def get_queryset(self):
        return Symptom.objects.all()

class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        return Medication.objects.all()

class WeekViewSet(viewsets.ModelViewSet):
    serializer_class = WeekSerializer

    def get_queryset(self):
        return Week.objects.all()

class LogViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer

    def get_queryset(self):
        return Log.objects.all()

class MoodViewSet(viewsets.ModelViewSet):
    serializer_class = MoodSerializer

    def get_queryset(self):
        return Mood.objects.all()

class TakenViewSet(viewsets.ModelViewSet):
    serializer_class = TakenSerializer

    def get_queryset(self):
        return Taken.objects.all()

class SugarViewSet(viewsets.ModelViewSet):
    serializer_class = SugarSerializer

    def get_queryset(self):
        return Sugar.objects.all()

class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Patient.objects.all()