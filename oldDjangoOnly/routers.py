from rest_framework import routers
from healthApp.views.api import *
# from healthApp.views.json import *

router = routers.SimpleRouter()

# router.register(r'auth/register', RegistrationViewSet, basename='auth-register')


router.register(r'users', UserViewSet, basename='users')
router.register(r'symptoms', SymptomViewSet, basename='symptoms')
router.register(r'medications', MedicationViewSet, basename='medications')
router.register(r'weeks', WeekViewSet, basename='weeks')
router.register(r'logs', LogViewSet, basename='logs')
router.register(r'moods', MoodViewSet, basename='moods')
router.register(r'taken', TakenViewSet, basename='taken')
router.register(r'sugars', SugarViewSet, basename='sugars')