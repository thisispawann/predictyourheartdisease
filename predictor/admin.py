from django.contrib import admin
from .models import Feedback, HeartData,DoctorHospital
from . import models


#Django Admin Header Customization

admin.site.site_header = "Heart Disease Prediction System"


# Register your models here.
admin.site.register(HeartData)
admin.site.register(DoctorHospital)
admin.site.register(models.Feedback)