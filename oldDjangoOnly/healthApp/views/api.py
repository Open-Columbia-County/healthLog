from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from healthApp.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from healthApp.serializers import *

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status



status = {
    "API Status": "API Running"
}
badStatus = {
    "Failed": "Failed"
}

def api(request):
    return JsonResponse(status, content_type='application/json')


@csrf_exempt
def apiLogin(request):
    pass
    

@csrf_exempt
def apiRegister(request):
    pass

class UserViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get']
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['updatedAt']
    # ordering = ['-updatedAt']

    def get_queryset(self):
        return User.objects.all()

    # def get_object(self):
    #     lookup_field_value = self.kwargs[self.lookup_field]

    #     obj = User.objects.get(lookup_field_value)
    #     self.check_object_permissions(self.request, obj)

    #     return obj

# class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
#     serializer_class = RegisterSerializer
#     permission_classes = (AllowAny,)
#     http_method_names = ['post']

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         res = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }

#         return Response({
#             "user": serializer.data,
#             "refresh": res["refresh"],
#             "token": res["access"]
#         }, status=status.HTTP_201_CREATED)


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