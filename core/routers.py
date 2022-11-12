from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from core.healthLog.viewsets import *


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# DATA
routes.register(r'symptom', SymptomViewSet, basename='symptom')
routes.register(r'medication', MedicationViewSet, basename='medication')
routes.register(r'week', WeekViewSet, basename='week')
routes.register(r'log', LogViewSet, basename='log')
routes.register(r'mood', MoodViewSet, basename='mood')
routes.register(r'taken', TakenViewSet, basename='taken')
routes.register(r'sugar', SugarViewSet, basename='sugar')
routes.register(r'provider', ProviderViewSet, basename='provider')

urlpatterns = [
    *routes.urls
]
