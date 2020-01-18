from django.contrib import admin
from .models import Patients, Bottles, BottleStats
# Register your models here.
admin.site.register(Patients)
admin.site.register(Bottles)
admin.site.register(BottleStats)