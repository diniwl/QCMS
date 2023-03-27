from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Schedule
from .forms import Scheduleform

# Import class 
from .models import Schedule

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg  = 'Account created'
            return redirect('view_login')
        else:
            msg = 'Registration failed'
    else:
        form = SignUpForm()
    return render(request, 'myapp/register.html', {'form': form, 'msg': msg})

def view_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST': 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_tem:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_tro:
                login(request, user)
                return redirect('homefismed')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Sign in error'
    return render(request, 'myapp/login.html', {'form': form, 'msg': msg})

def home(request):
    return render(request, 'myapp/homepage.html', {
        'schedule': Schedule.objects.all()
    })

def homefismed(request):
    return render(request, 'myapp/home_fismed.html')

# 2nd step to create function that handles http requests
# Function-based http requests
# def schedule_page(request):
#     # Render .html files
#     return render(request, 'myapp/homepage.html', {
#         'schedule': Schedule.objects.all()
#     })

# A function with 2 arguments
def view_schedule(request, id):
    schedule = Schedule.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))

def add(request):
    if request.method == 'POST':
        form = Scheduleform(request.POST)
        if form.is_valid():
            new_task_date = form.cleaned_data['task_date']
            new_task = form.cleaned_data['task']
            new_machine = form.cleaned_data['machine']
            new_location = form.cleaned_data['location']

            new_schedule = Schedule(
                task_date = new_task_date,
                task = new_task,
                machine = new_machine,
                location = new_location,
            )
            new_schedule.save()
            return render(request, 'myapp/add.html', {
                'form': Scheduleform(),
                'success': True
            })
    else:
        form = Scheduleform(),
    return render(request, 'myapp/add.html', {
        'form': Scheduleform()
    })

def edit(request, id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(pk=id)
        form = Scheduleform(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/edit.html', {
                'form': form,
                'success': True
            })
    else:
        schedule = Schedule.objects.get(pk=id)
        form = Scheduleform(instance=schedule)
    return render(request, 'myapp/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(pk=id)
        schedule.delete()
    return HttpResponseRedirect(reverse('home'))