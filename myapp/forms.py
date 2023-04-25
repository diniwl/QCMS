from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Schedule, Penerimaan, Kalibrasi, Ukes, Service, Sertifkalibrasi

#AUTH
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    institute_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'password1', 'password2', 'is_tem', 'is_tro', 'institute_name')

#SCHEDULE
class Scheduleform(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['task_date', 'task', 'machine', 'location']
        labels = {
            'task_date': 'Scheduled Date',
            'task': 'Task',
            'machine': 'Machine',
            'location': 'Location',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'task': forms.TextInput(attrs={'class': 'form-control'}), 
            'machine': forms.TextInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'})
        }

#UJI PENERIMAAN
class Penerimaanform(forms.ModelForm):
    class Meta:
        model = Penerimaan
        fields = ['task_date', 'machine', 'location', 'is_passed', 'is_failed']
        labels = {
            'task_date': 'Scheduled Date',
            'machine': 'Machine',
            'location': 'Location',
            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'machine': forms.TextInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_passed' : forms.CheckboxInput(),
            'is_failed' : forms.CheckboxInput(),
        }

#KALIBRASI
class Kalibrasiform(forms.ModelForm):
    class Meta:
        model = Kalibrasi
        fields = ['task_date', 'machine', 'location', 'is_passed', 'is_failed']
        labels = {
            'task_date': 'Scheduled Date',
            'machine': 'Machine',
            'location': 'Location',
            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'machine': forms.TextInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_passed' : forms.CheckboxInput(),
            'is_failed' : forms.CheckboxInput(),
        }

#SERTIF KALIBRASI
class SertifKalibrasiform(forms.ModelForm):
    class Meta:
        model = Sertifkalibrasi
        fields = ['submit_date', 'location','file_name', 'machine', 'serial', 'pdf_file']
        labels = {
            'submit_date': 'Submit Date',
            'location': 'Location',
            'file_name': 'File name (in PDF)',
            'machine': 'Brand and Type',
            'serial': 'Serial number',
            'pdf_file': 'File',
        }

        Widgets = {
            'submit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'file_name': forms.TextInput(attrs={'class': 'form-control'}),
            'machine': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
        }

#UKES
class Ukesform(forms.ModelForm):
    class Meta:
        model = Ukes
        fields = ['task_date', 'machine', 'location', 'is_passed', 'is_failed']
        labels = {
            'task_date': 'Scheduled Date',
            'machine': 'Machine',
            'location': 'Location',
            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'machine': forms.TextInput(attrs={'class': 'form-control'}), 
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_passed' : forms.CheckboxInput(),
            'is_failed' : forms.CheckboxInput(),
        }

#SERVICE
class Serviceform(forms.ModelForm):
    CHOICES = (
        (1, 'Emergency'),
        (2, 'Non-emergency'),
        (3, 'Contract'),
        (4, 'Install'),
        (5, 'Warranty'),
        (6, 'Other'),
    )

    service_type: forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Service
        fields = ['task_date', 'brand', 'type', 'serial', 'address', 'problem', 'repair', 'cust_name', 'tech_name', 'complain_num', 'is_completed', 'is_continue', 'service_type']
        labels = {
            'task_date': 'Service Date',
            'brand': 'Brand',
            'type' : 'Type',
            'serial': 'Serial',
            'address': 'Customer with adress',
            'problem': 'Problem/Request',
            'repair': 'Repair comments',
            'cust_name': "Customer's identity",
            'tech_name': "Technician's identity",
            'complain_num': "Document's Number",
            'is_completed': 'Completed',
            'is_continue': 'Continue',
            'service_type': "Type of service"
        }

        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'problem': forms.TextInput(attrs={'class': 'form-control'}),
            'repair': forms.TextInput(attrs={'class': 'form-control'}),
            'cust_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tech_name': forms.TextInput(attrs={'class': 'form-control'}),
            'complain_num': forms.TextInput(attrs={'class': 'form-control'}),
            'is_completed' : forms.CheckboxInput(),
            'is_continue' : forms.CheckboxInput(),
        }