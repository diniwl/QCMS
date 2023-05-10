from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# USER 
class User(AbstractUser):
    full_name = models.CharField(max_length=150, null=True)
    is_tem = models.BooleanField('is tem', default=False)
    is_tro = models.BooleanField('is tro', default=False)
    institute_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def clean(self):
        if self.is_tem and self.is_tro:
            raise ValidationError('You can only select one')
        super().clean()

# SCHEDULE
class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    task = models.CharField(max_length=150)
    machine = models.CharField(max_length=150)
    location = models.CharField(max_length=150)

# UJI PENERIMAAN
class Penerimaan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    machine = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)

#  KALIBRASI
class Kalibrasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    machine = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)

#SERTIF KALIBRASI
class Sertifkalibrasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    submit_date = models.DateField(null=True)
    location = models.CharField(max_length=150)
    file_name = models.CharField(max_length=150)
    machine = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)
    pdf_file = models.FileField(upload_to='sertifkalibrasi/')

#SERTIF UJI KESESUAIAN
class Sertifukes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    submit_date = models.DateField(null=True)
    location = models.CharField(max_length=150)
    file_name = models.CharField(max_length=150)
    machine = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)
    pdf_file = models.FileField(upload_to='sertifukes/')

# UJI  KESESUAIAN
class Ukes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    machine = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)

# # PEMELIHARAAN PREVENTIF
# class Preventif(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     task_date = models.DateField(null=True)
#     machine = models.CharField(max_length=150)
#     location = models.CharField(max_length=150)
#     period = models.CharField(max_length=150)

# SERVICE REPORT
class Service(models.Model):
    EMG = 'EMERGENCY'
    NONEMG = 'NON-EMERGENCY'
    CONTRACT = 'CONTRACT'
    INSTALL = 'INSTALL'
    WARRANTY = 'WARRANTY'
    OTHER = 'OTHER'

    CHOICES = (
        (EMG, 'Emergency'),
        (NONEMG, 'Non-emergency'),
        (CONTRACT, 'Contract'),
        (INSTALL, 'Install'),
        (WARRANTY, 'Warranty'),
        (OTHER, 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    address = models.CharField(max_length=150)
    complain_num = models.CharField(max_length=150)
    service_type = models.CharField(max_length=100, choices=CHOICES, default=NONEMG)
    brand = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    serial = models.CharField(max_length=150)
    problem = models.CharField(max_length=350)
    repair = models.CharField(max_length=350)
    cust_name = models.CharField(max_length=150)
    tech_name = models.CharField(max_length=150)
    is_completed = models.BooleanField('completed', default=False)
    is_continue = models.BooleanField('continue', default=False)
