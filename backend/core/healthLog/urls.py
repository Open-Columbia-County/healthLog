from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.jsonBase),
    path('json/', views.jsonBase),
    path('json/data/', views.jsonAllData),
    path('json/<int:user_id>/userData/', views.jsonUserData),
    path('json/<int:user_id>/pcpData/', views.jsonPcpData),
    path('json/<int:user_id>/mentalData/', views.jsonMentalData),
]