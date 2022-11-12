from django.contrib import admin
from core.user.models import *
from core.healthLog.models import *

admin.site.register(User)
admin.site.register(Symptom)
admin.site.register(Medication)
admin.site.register(Week)
admin.site.register(Log)
admin.site.register(Mood)
admin.site.register(Taken)
admin.site.register(Sugar)
admin.site.register(Patient)