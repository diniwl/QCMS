from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Schedule

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