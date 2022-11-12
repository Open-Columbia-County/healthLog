from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Symptom)
admin.site.register(Medication)
admin.site.register(Upload)
admin.site.register(Week)
admin.site.register(Log)
admin.site.register(Mood)
admin.site.register(Taken)
admin.site.register(Sugar)