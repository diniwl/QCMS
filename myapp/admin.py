from django.contrib import admin
from .models import User, Schedule, Penerimaan, Kalibrasi, Ukes, Service, Sertifkalibrasi

# Register your models here.
admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Penerimaan)
admin.site.register(Kalibrasi)
admin.site.register(Ukes)
admin.site.register(Service)
admin.site.register(Sertifkalibrasi)