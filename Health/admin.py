from django.contrib import admin
from .models import Remainder,Patient,Doctor,Medical_Report,Patient_tablets,Room_doc,Extra_Values,Predict
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Medical_Report)
admin.site.register(Extra_Values)
admin.site.register(Room_doc)
admin.site.register(Patient_tablets)
admin.site.register(Remainder)
admin.site.register(Predict)
