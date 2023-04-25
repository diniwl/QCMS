from django.shortcuts import render, redirect,  get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Schedule, Penerimaan, Kalibrasi, Ukes, Service, Sertifkalibrasi
from .forms import Scheduleform, Penerimaanform, Kalibrasiform, Ukesform, Serviceform, SertifKalibrasiform

# Create your views here.

# AUTHENTICATION
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


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('index'))

# SCHEDULE PAGE
@login_required
def home(request):
    schedule  = Schedule.objects.filter(user=request.user)
    return render(request, 'myapp/homepage.html', {
        'schedule': schedule
    })

def homefismed(request):
    return render(request, 'myapp/home_fismed.html')

def view_schedule(request, id):
    schedule = Schedule.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))

@login_required
def add(request):
    if request.method == 'POST':
        form = Scheduleform(request.POST)
        if form.is_valid():
            new_task_date = form.cleaned_data['task_date']
            new_task = form.cleaned_data['task']
            new_machine = form.cleaned_data['machine']
            new_location = form.cleaned_data['location']

            new_schedule = Schedule(
                user=request.user,
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

# UJI PENERIMAAN
@login_required
def home_penerimaan(request):
    penerimaan = Penerimaan.objects.filter(user=request.user)
    return render(request, 'myapp/penerimaan.html', {
        'penerimaan': penerimaan
    })

def view_penerimaan(request, id):
    penerimaan = Penerimaan.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_penerimaan'))

@login_required
def add_penerimaan(request):
    if request.method == 'POST':
        form = Penerimaanform(request.POST)
        if form.is_valid():
            new_task_date = form.cleaned_data['task_date']
            new_machine = form.cleaned_data['machine']
            new_location = form.cleaned_data['location']
            new_ispassed = form.cleaned_data['is_passed']
            new_isfailed = form.cleaned_data['is_failed']

            new_penerimaan = Penerimaan(
                user=request.user,
                task_date = new_task_date,
                machine = new_machine,
                location = new_location,
                is_passed = new_ispassed,
                is_failed = new_isfailed,
            )
            new_penerimaan.save()
            return render(request, 'myapp/add_penerimaan.html', {
                'form': Penerimaanform(),
                'success': True
            })
    else:
        form = Penerimaanform(),
    return render(request, 'myapp/add_penerimaan.html', {
        'form': Penerimaanform()
    })

def edit_penerimaan(request, id):
    if request.method == 'POST':
        penerimaan = Penerimaan.objects.get(pk=id)
        form = Penerimaanform(request.POST, instance=penerimaan)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/edit_penerimaan.html', {
                'form': form,
                'success': True
            })
    else:
        penerimaan = Penerimaan.objects.get(pk=id)
        form = Penerimaanform(instance=penerimaan)
    return render(request, 'myapp/edit_penerimaan.html', {
        'form': form
    })

def delete_penerimaan(request, id):
    if request.method == 'POST':
        penerimaan = Penerimaan.objects.get(pk=id)
        penerimaan.delete()
    return HttpResponseRedirect(reverse('home_penerimaan'))


# KALIBRASI
@login_required
def home_kalibrasi(request):
    kalibrasi = Kalibrasi.objects.filter(user=request.user)
    return render(request, 'myapp/kalibrasi.html', {
        'kalibrasi': kalibrasi
    })

def view_kalibrasi(request, id):
    kalibrasi = Kalibrasi.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_kalibrasi'))

@login_required
def add_kalibrasi(request):
    if request.method == 'POST':
        form = Kalibrasiform(request.POST)
        if form.is_valid():
            new_task_date = form.cleaned_data['task_date']
            new_machine = form.cleaned_data['machine']
            new_location = form.cleaned_data['location']
            new_ispassed = form.cleaned_data['is_passed']
            new_isfailed = form.cleaned_data['is_failed']

            new_kalibrasi = Kalibrasi(
                user=request.user,
                task_date = new_task_date,
                machine = new_machine,
                location = new_location,
                is_passed = new_ispassed,
                is_failed = new_isfailed,
            )
            new_kalibrasi.save()
            return render(request, 'myapp/add_kalibrasi.html', {
                'form': Kalibrasiform(),
                'success': True
            })
    else:
        form = Kalibrasiform(),
    return render(request, 'myapp/add_kalibrasi.html', {
        'form': Kalibrasiform()
    })

def edit_kalibrasi(request, id):
    if request.method == 'POST':
        kalibrasi = Kalibrasi.objects.get(pk=id)
        form = Kalibrasiform(request.POST, instance=kalibrasi)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/edit_kalibrasi.html', {
                'form': form,
                'success': True
            })
    else:
        kalibrasi = Kalibrasi.objects.get(pk=id)
        form = Kalibrasiform(instance=kalibrasi)
    return render(request, 'myapp/edit_kalibrasi.html', {
        'form': form
    })

def delete_kalibrasi(request, id):
    if request.method == 'POST':
        kalibrasi = Kalibrasi.objects.get(pk=id)
        kalibrasi.delete()
    return HttpResponseRedirect(reverse('home_kalibrasi'))


# SERTIF KALIBRAsi
@login_required
def home_sertifkalibrasi(request):
    sertifkalibrasi = Sertifkalibrasi.objects.filter(user=request.user)
    return render(request, 'myapp/home_sertifk.html', {
        'sertifkalibrasi': sertifkalibrasi
    })

@login_required
def sertif_kalibrasi(request):
    if request.method == 'POST':
        form = SertifKalibrasiform(request.POST, request.FILES)
        if form.is_valid():
            new_submitdate = form.cleaned_data['submit_date']
            new_filename = form.cleaned_data['file_name']
            new_machine = form.cleaned_data['machine']
            new_serial = form.cleaned_data['serial']
            new_file = form.cleaned_data['pdf_file']

            new_sertifkalibrasi = Sertifkalibrasi(
                user=request.user,
                submit_date = new_submitdate,
                file_name = new_filename,
                machine = new_machine,
                serial = new_serial,
                pdf_file = new_file
            )
            new_sertifkalibrasi.save()
    else:
        form = SertifKalibrasiform()
    return render(request, 'myapp/upload_kalibrasi.html', {'form': form})

@login_required
def view_sertifkalibrasi(request, id):
    pdf = get_object_or_404(Sertifkalibrasi, pk=id, user=request.user)
    return render(request, 'myapp/view_sertifk.html', {'pdf': pdf})
    # response = HttpResponse(pdf.pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = f'filename="{pdf.name}.pdf"'
    # return response


# UJI KESESUAIAN
@login_required
def home_ukes(request):
    ukes = Ukes.objects.filter(user=request.user)
    return render(request, 'myapp/ukes.html', {
        'ukes': ukes
    })

def view_ukes(request, id):
    ukes = Ukes.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_ukes'))

@login_required
def add_ukes(request):
    if request.method == 'POST':
        form = Ukesform(request.POST)
        if form.is_valid():
            new_task_date = form.cleaned_data['task_date']
            new_machine = form.cleaned_data['machine']
            new_location = form.cleaned_data['location']
            new_ispassed = form.cleaned_data['is_passed']
            new_isfailed = form.cleaned_data['is_failed']

            new_ukes = Ukes(
                user=request.user,
                task_date = new_task_date,
                machine = new_machine,
                location = new_location,
                is_passed = new_ispassed,
                is_failed = new_isfailed,
            )
            new_ukes.save()
            return render(request, 'myapp/add_ukes.html', {
                'form': Ukesform(),
                'success': True
            })
    else:
        form = Ukesform(),
    return render(request, 'myapp/add_ukes.html', {
        'form': Ukesform()
    })

def edit_ukes(request, id):
    if request.method == 'POST':
        ukes = Ukes.objects.get(pk=id)
        form = Ukesform(request.POST, instance=ukes)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/edit_ukes.html', {
                'form': form,
                'success': True
            })
    else:
        ukes = Ukes.objects.get(pk=id)
        form = Ukesform(instance=ukes)
    return render(request, 'myapp/edit_ukes.html', {
        'form': form
    })

def delete_ukes(request, id):
    if request.method == 'POST':
        ukes = Ukes.objects.get(pk=id)
        ukes.delete()
    return HttpResponseRedirect(reverse('home_ukes'))

# SERVICE REPORT
@login_required
def home_service(request):
    service = Service.objects.filter(user=request.user)
    return render(request, 'myapp/service.html', {
        'service': service
    })

def view_service(request, id):
    service = Service.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_service'))

@login_required
def add_service(request):
    if request.method == 'POST':
        form = Serviceform(request.POST)
        if form.is_valid():
            new_taskdate = form.cleaned_data['task_date']
            new_brand = form.cleaned_data['brand']
            new_type = form.cleaned_data['type']
            new_serial = form.cleaned_data['serial']
            new_address = form.cleaned_data['address']
            new_problem = form.cleaned_data['problem']
            new_repair = form.cleaned_data['repair']
            new_custname = form.cleaned_data['cust_name']
            new_techname = form.cleaned_data['tech_name']
            new_complainnum = form.cleaned_data['complain_num']
            new_iscompleted = form.cleaned_data['is_completed']
            new_iscontinue = form.cleaned_data['is_continue']
            new_servicetype = form.cleaned_data['service_type']

            new_service = Service(
                user=request.user,
                task_date = new_taskdate,
                brand = new_brand,
                type = new_type,
                serial = new_serial,
                address = new_address,
                problem = new_problem,
                repair = new_repair,
                cust_name = new_custname,
                tech_name = new_techname,
                complain_num = new_complainnum,
                is_completed = new_iscompleted,
                is_continue = new_iscontinue,
                service_type = new_servicetype,
            )
            new_service.save()
            return render(request, 'myapp/add_service.html', {
                'form': Serviceform(),
                'success': True
            })
    else:
        form = Serviceform(),
    return render(request, 'myapp/add_service.html', {
        'form': Serviceform()
    })

def edit_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        form = Serviceform(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/edit_service.html', {
                'form': form,
                'success': True
            })
    else:
        service = Service.objects.get(pk=id)
        form = Serviceform(instance=service)
    return render(request, 'myapp/edit_service.html', {
        'form': form
    })

def delete_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        service.delete()
    return HttpResponseRedirect(reverse('home_service'))

# PEMELIHARAAN PREVENTIF