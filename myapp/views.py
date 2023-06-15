from django.shortcuts import render, redirect,  get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout as django_logout, update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
import pytz

from .models import Schedule, Penerimaan, Kalibrasi, Ukes, Service, Sertifkalibrasi, Sertifukes, User, Maintenance
from .forms import Scheduleform, Penerimaanform, Kalibrasiform, Ukesform, Serviceform, SertifKalibrasiform, Sertifukesform, Maintenanceform
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.utils import timezone

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
    return render(request, 'myapp/auth_pages/register.html', {'form': form, 'msg': msg})

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
                return redirect('home')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Sign in error'
    return render(request, 'myapp/auth_pages/login.html', {'form': form, 'msg': msg})


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('index'))

# EDIT ACCOUNT PAGE
class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

def account_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, user_form.instance)
            return redirect('account_edit')
    else:
        user_form = UserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'myapp/acc_setting/account_edit.html', {'user_form':user_form, 'password_form':password_form})

# SCHEDULE PAGE
@login_required
def home(request):
    schedule  = Schedule.objects.filter(user=request.user)
    return render(request, 'myapp/schedule/homepage.html', {
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
            new_time = form.cleaned_data['time']

            new_schedule = Schedule(
                user=request.user,
                task_date=new_task_date,
                task=new_task,
                machine=new_machine,
                location=new_location,
                time=new_time,
            )
            new_schedule.save()       
            return render(request, 'myapp/schedule/add.html', {
                'form': Scheduleform(),
                'success': True
            })
    else:
        form = Scheduleform()
    return render(request, 'myapp/schedule/add.html', {
        'form': Scheduleform()
    })

def edit(request, id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(pk=id)
        form = Scheduleform(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/schedule/edit.html', {
                'form': form,
                'success': True
            })
    else:
        schedule = Schedule.objects.get(pk=id)
        form = Scheduleform(instance=schedule)
    return render(request, 'myapp/schedule/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        schedule = Schedule.objects.get(pk=id)
        schedule.delete()
    return HttpResponseRedirect(reverse('home'))


#NOTIFICATION
def check_notification(request):
    # Get the current date and time in the server's timezone
    current_datetime = timezone.now()

    # Convert the timezone to Indonesia's timezone
    indonesia_tz = pytz.timezone('Asia/Jakarta')
    current_datetime = current_datetime.astimezone(indonesia_tz)

    # Query the tasks that match the current date and time
    matching_tasks = Schedule.objects.filter(task_date=current_datetime.date(), time__lte=current_datetime.time())

    # Prepare the response data
    response_data = {
        'has_notification': False,
        'message': '',
    }

    if matching_tasks:
        response_data['has_notification'] = True
        response_data['message'] = 'Ada pekerjaan yang harus dilakukan hari ini'

    return JsonResponse(response_data)


# UJI PENERIMAAN
@login_required
def home_penerimaan(request):
    if request.user.is_tro:
        return HttpResponseForbidden("Access Denied! Sorry You Cannot Access This Page")
    penerimaan = Penerimaan.objects.filter(user=request.user)
    return render(request, 'myapp/acceptance/penerimaan.html', {
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
            new_location = form.cleaned_data['location']
            new_hos_unit = form.cleaned_data['hos_unit']
            new_techname = form.cleaned_data['tech_name']

            new_tubestd_brand = form.cleaned_data['tube_std_brand']
            new_tubestd_model = form.cleaned_data['tube_std_model']
            new_tubestd_serial = form.cleaned_data['tube_std_serial']
            new_tubestd_isok = form.cleaned_data['tube_std_is_okay']

            new_tubespt_brand = form.cleaned_data['tube_spt_brand']
            new_tubespt_model = form.cleaned_data['tube_spt_model']
            new_tubespt_serial = form.cleaned_data['tube_spt_serial']
            new_tubespt_isok = form.cleaned_data['tube_spt_is_okay']

            new_tubeasb_brand = form.cleaned_data['tube_asb_brand']
            new_tubeasb_model = form.cleaned_data['tube_asb_model']
            new_tubeasb_serial = form.cleaned_data['tube_asb_serial']
            new_tubeasb_isok = form.cleaned_data['tube_asb_is_okay']

            new_bld_brand = form.cleaned_data['beam_ld_brand']
            new_bld_model = form.cleaned_data['beam_ld_model']
            new_bld_serial = form.cleaned_data['beam_ld_serial']
            new_bld_isok = form.cleaned_data['beam_ld_is_okay']

            new_htt_brand = form.cleaned_data['htt_brand']
            new_htt_model = form.cleaned_data['htt_model']
            new_htt_serial = form.cleaned_data['htt_serial']
            new_htt_isok = form.cleaned_data['htt_is_okay']

            new_flobuck_brand = form.cleaned_data['flo_buck_brand']
            new_flobuck_model = form.cleaned_data['flo_buck_model']
            new_flobuck_serial = form.cleaned_data['flo_buck_serial']
            new_flobuck_isok = form.cleaned_data['flo_buck_is_okay']

            new_levbuck_brand = form.cleaned_data['lev_buck_brand']
            new_levbuck_model = form.cleaned_data['lev_buck_model']
            new_levbuck_serial = form.cleaned_data['lev_buck_serial']
            new_levbuck_isok = form.cleaned_data['lev_buck_is_okay']

            new_buckstd_brand = form.cleaned_data['buck_std_brand']
            new_buckstd_model = form.cleaned_data['buck_std_model']
            new_buckstd_serial = form.cleaned_data['buck_std_serial']
            new_buckstd_isok = form.cleaned_data['buck_std_is_okay']

            new_acu_brand = form.cleaned_data['acu_brand']
            new_acu_model = form.cleaned_data['acu_model']
            new_acu_serial = form.cleaned_data['acu_serial']
            new_acu_isok = form.cleaned_data['acu_is_okay']

            new_fork_brand = form.cleaned_data['fork_brand']
            new_fork_model = form.cleaned_data['fork_model']
            new_fork_serial = form.cleaned_data['fork_serial']
            new_fork_isok = form.cleaned_data['fork_is_okay']

            new_gnd_cable = form.cleaned_data['gnd_cable']
            new_ln_vol = form.cleaned_data['ln_vol']
            new_hv_cable = form.cleaned_data['hv_cable']
            new_lv_cable = form.cleaned_data['lv_cable']

            new_rail = form.cleaned_data['rail']
            new_std_spt = form.cleaned_data['std_spt']
            new_asb_tube = form.cleaned_data['asb_tube']
            new_asb_col = form.cleaned_data['asb_col']
            new_lamp = form.cleaned_data['lamp']
            new_bout = form.cleaned_data['bout']

            new_genitem1 = form.cleaned_data['gen_item1']
            new_genitem2 = form.cleaned_data['gen_item2']
            new_genitem3 = form.cleaned_data['gen_item3']

            new_tubestd1 = form.cleaned_data['tube_std_item1']
            new_tubestd2 = form.cleaned_data['tube_std_item2']

            new_tubesp1 = form.cleaned_data['tube_sp_item1']
            new_tubesp2 = form.cleaned_data['tube_sp_item2']

            new_bld1 = form.cleaned_data['bld_item1']
            new_bld2 = form.cleaned_data['bld_item2']
            new_bld3 = form.cleaned_data['bld_item3']
            new_bld4 = form.cleaned_data['bld_item4']
            new_bld5 = form.cleaned_data['bld_item5']
            new_bld6 = form.cleaned_data['bld_item6']
            new_bld7 = form.cleaned_data['bld_item7']

            new_acu1 = form.cleaned_data['acu_item1']

            new_bucky_tbl1 = form.cleaned_data['bucky_tbl_item1']
            new_bucky_tbl2 = form.cleaned_data['bucky_tbl_item2']

            new_bucky_std1 = form.cleaned_data['bucky_std_item1']
            new_bucky_std2 = form.cleaned_data['bucky_std_item2']

            new_system = form.cleaned_data['system']

            new_ispassed = form.cleaned_data['is_passed']
            new_isfailed = form.cleaned_data['is_failed']

            new_penerimaan = Penerimaan(
                user=request.user,
                task_date = new_task_date,
                location = new_location,
                hos_unit = new_hos_unit,
                tech_name = new_techname,

                tube_std_brand = new_tubestd_brand,
                tube_std_model = new_tubestd_model,
                tube_std_serial = new_tubestd_serial,
                tube_std_is_okay = new_tubestd_isok,

                tube_spt_brand = new_tubespt_brand,
                tube_spt_model = new_tubespt_model,
                tube_spt_serial = new_tubespt_serial,
                tube_spt_is_okay = new_tubespt_isok,

                tube_asb_brand = new_tubeasb_brand,
                tube_asb_model = new_tubeasb_model,
                tube_asb_serial = new_tubeasb_serial,
                tube_asb_is_okay = new_tubeasb_isok,

                beam_ld_brand = new_bld_brand,
                beam_ld_model = new_bld_model,
                beam_ld_serial = new_bld_serial,
                beam_ld_is_okay = new_bld_isok,

                htt_brand = new_htt_brand,
                htt_model = new_htt_model,
                htt_serial = new_htt_serial,
                htt_is_okay = new_htt_isok,

                flo_buck_brand = new_flobuck_brand,
                flo_buck_model = new_flobuck_model,
                flo_buck_serial = new_flobuck_serial,
                flo_buck_is_okay = new_flobuck_isok,

                lev_buck_brand = new_levbuck_brand,
                lev_buck_model = new_levbuck_model,
                lev_buck_serial = new_levbuck_serial,
                lev_buck_is_okay = new_levbuck_isok,

                buck_std_brand = new_buckstd_brand,
                buck_std_model = new_buckstd_model,
                buck_std_serial = new_buckstd_serial,
                buck_std_is_okay = new_buckstd_isok,

                acu_brand = new_acu_brand,
                acu_model = new_acu_model,
                acu_serial = new_acu_serial,
                acu_is_okay = new_acu_isok,

                fork_brand = new_fork_brand,
                fork_model = new_fork_model,
                fork_serial = new_fork_serial,
                fork_is_okay = new_fork_isok,

                gnd_cable = new_gnd_cable,
                ln_vol = new_ln_vol,
                hv_cable = new_hv_cable,
                lv_cable = new_lv_cable,
                rail = new_rail,
                std_spt = new_std_spt,
                asb_tube = new_asb_tube,
                asb_col = new_asb_col,
                lamp = new_lamp,
                bout = new_bout,

                gen_item1 = new_genitem1,
                gen_item2 = new_genitem2,
                gen_item3 = new_genitem3,

                tube_std_item1 = new_tubestd1,
                tube_std_item2 = new_tubestd2,

                tube_sp_item1 = new_tubesp1,
                tube_sp_item2 = new_tubesp2,

                bld_item1 = new_bld1,
                bld_item2 = new_bld2,
                bld_item3 = new_bld3,
                bld_item4 = new_bld4,
                bld_item5 = new_bld5,
                bld_item6 = new_bld6,
                bld_item7 = new_bld7,

                acu_item1 = new_acu1,

                bucky_tbl_item1 = new_bucky_tbl1,
                bucky_tbl_item2 = new_bucky_tbl2,
                
                bucky_std_item1 = new_bucky_std1,
                bucky_std_item2 = new_bucky_std2,

                system = new_system,

                is_passed = new_ispassed,
                is_failed = new_isfailed,
            )
            new_penerimaan.save()
            return render(request, 'myapp/acceptance/add_penerimaan.html', {
                'form': Penerimaanform(),
                'success': True
            })
    else:
        form = Penerimaanform(),
    return render(request, 'myapp/acceptance/add_penerimaan.html', {
        'form': Penerimaanform()
    })

def edit_penerimaan(request, id):
    if request.method == 'POST':
        penerimaan = Penerimaan.objects.get(pk=id)
        form = Penerimaanform(request.POST, instance=penerimaan)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/acceptance/edit_penerimaan.html', {
                'form': form,
                'success': True
            })
    else:
        penerimaan = Penerimaan.objects.get(pk=id)
        form = Penerimaanform(instance=penerimaan)
    return render(request, 'myapp/acceptance/edit_penerimaan.html', {
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
    return render(request, 'myapp/kalibrasi/kalibrasi.html', {
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
            new_location = form.cleaned_data['location']
            new_techname = form.cleaned_data['tech_name']

            new_tube_brand = form.cleaned_data['xray_tube_brand']
            new_tube_type = form.cleaned_data['xray_tube_type']
            new_tube_serial = form.cleaned_data['xray_tube_serial']

            new_gen_brand = form.cleaned_data['xray_tube_brand']
            new_gen_type = form.cleaned_data['xray_tube_type']
            new_gen_serial = form.cleaned_data['xray_tube_serial']

            new_temp_before = form.cleaned_data['temp_before']
            new_temp_after = form.cleaned_data['temp_after']
            new_hum_before = form.cleaned_data['hum_before']
            new_hum_after = form.cleaned_data['hum_after']

            new_kvset1 = form.cleaned_data['kv_set1']
            new_kvset2 = form.cleaned_data['kv_set2']
            new_kvset3 = form.cleaned_data['kv_set3']

            new_kv1 = form.cleaned_data['kv1']
            new_kv2 = form.cleaned_data['kv2']
            new_kv3 = form.cleaned_data['kv3']
            new_kv4 = form.cleaned_data['kv4']
            new_kv5 = form.cleaned_data['kv5']
            new_kv6 = form.cleaned_data['kv6']
            new_kv7 = form.cleaned_data['kv7']
            new_kv8 = form.cleaned_data['kv8']
            new_kv9 = form.cleaned_data['kv9']

            new_kvavg1 = form.cleaned_data['kv_avg1']
            new_kvavg2 = form.cleaned_data['kv_avg2']
            new_kvavg3 = form.cleaned_data['kv_avg3']

            new_kvdev1 = form.cleaned_data['kv_dev1']
            new_kvdev2 = form.cleaned_data['kv_dev2']
            new_kvdev3 = form.cleaned_data['kv_dev3']

            new_kvprc1 = form.cleaned_data['kv_prc1']
            new_kvprc2 = form.cleaned_data['kv_prc2']
            new_kvprc3 = form.cleaned_data['kv_prc3']
            
            new_maset1 = form.cleaned_data['ma_set1']
            new_maset2 = form.cleaned_data['ma_set2']
            new_maset3 = form.cleaned_data['ma_set3']

            new_ma1 = form.cleaned_data['ma1']
            new_ma2 = form.cleaned_data['ma2']
            new_ma3 = form.cleaned_data['ma3']
            new_ma4 = form.cleaned_data['ma4']
            new_ma5 = form.cleaned_data['ma5']
            new_ma6 = form.cleaned_data['ma6']
            new_ma7 = form.cleaned_data['ma7']
            new_ma8 = form.cleaned_data['ma8']
            new_ma9 = form.cleaned_data['ma9']

            new_maavg1 = form.cleaned_data['ma_avg1']
            new_maavg2 = form.cleaned_data['ma_avg2']
            new_maavg3 = form.cleaned_data['ma_avg3']

            new_madev1 = form.cleaned_data['ma_dev1']
            new_madev2 = form.cleaned_data['ma_dev2']
            new_madev3 = form.cleaned_data['ma_dev3']

            new_maprc1 = form.cleaned_data['ma_prc1']
            new_maprc2 = form.cleaned_data['ma_prc2']
            new_maprc3 = form.cleaned_data['ma_prc3']
                        
            new_ispassed = form.cleaned_data['is_passed']
            new_isfailed = form.cleaned_data['is_failed']

            new_kalibrasi = Kalibrasi(
                user=request.user,
                task_date = new_task_date,
                location = new_location,
                tech_name = new_techname,

                xray_tube_brand = new_tube_brand,
                xray_tube_type = new_tube_type,
                xray_tube_serial = new_tube_serial,

                xray_gen_brand = new_gen_brand,
                xray_gen_type = new_gen_type,
                xray_gen_serial = new_gen_serial,

                temp_before = new_temp_before,
                temp_after = new_temp_after,
                hum_before = new_hum_before,
                hum_after = new_hum_after,

                kv_set1 = new_kvset1,
                kv_set2 = new_kvset2,
                kv_set3 = new_kvset3,

                kv1 = new_kv1,
                kv2 = new_kv2,
                kv3 = new_kv3,
                kv4 = new_kv4,
                kv5 = new_kv5,
                kv6 = new_kv6,
                kv7 = new_kv7,
                kv8 = new_kv8,
                kv9 = new_kv9,

                kv_avg1 = new_kvavg1,
                kv_avg2 = new_kvavg2,
                kv_avg3 = new_kvavg3,

                kv_dev1 = new_kvdev1,
                kv_dev2 = new_kvdev2,
                kv_dev3 = new_kvdev3,

                kv_prc1 = new_kvprc1,
                kv_prc2 = new_kvprc2,
                kv_prc3 = new_kvprc3,

                ma_set1 = new_maset1,
                ma_set2 = new_maset2,
                ma_set3 = new_maset3,

                ma1 = new_ma1,
                ma2 = new_ma2,
                ma3 = new_ma3,
                ma4 = new_ma4,
                ma5 = new_ma5,
                ma6 = new_ma6,
                ma7 = new_ma7,
                ma8 = new_ma8,
                ma9 = new_ma9,

                ma_avg1 = new_maavg1,
                ma_avg2 = new_maavg2,
                ma_avg3 = new_maavg3,

                ma_dev1 = new_madev1,
                ma_dev2 = new_madev2,
                ma_dev3 = new_madev3,

                ma_prc1 = new_maprc1,
                ma_prc2 = new_maprc2,
                ma_prc3 = new_maprc3,

                is_passed = new_ispassed,
                is_failed = new_isfailed,
            )
            new_kalibrasi.save()
            return render(request, 'myapp/kalibrasi/add_kalibrasi.html', {
                'form': Kalibrasiform(),
                'success': True
            })
    else:
        form = Kalibrasiform(),
    return render(request, 'myapp/kalibrasi/add_kalibrasi.html', {
        'form': Kalibrasiform()
    })

def edit_kalibrasi(request, id):
    if request.method == 'POST':
        kalibrasi = Kalibrasi.objects.get(pk=id)
        form = Kalibrasiform(request.POST, instance=kalibrasi)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/kalibrasi/edit_kalibrasi.html', {
                'form': form,
                'success': True
            })
    else:
        kalibrasi = Kalibrasi.objects.get(pk=id)
        form = Kalibrasiform(instance=kalibrasi)
    return render(request, 'myapp/kalibrasi/edit_kalibrasi.html', {
        'form': form
    })

def delete_kalibrasi(request, id):
    if request.method == 'POST':
        kalibrasi = Kalibrasi.objects.get(pk=id)
        kalibrasi.delete()
    return HttpResponseRedirect(reverse('home_kalibrasi'))


# SERTIF KALIBRASI
@login_required
def home_sertifkalibrasi(request):
    sertifkalibrasi = Sertifkalibrasi.objects.filter(user=request.user)
    return render(request, 'myapp/kalibrasi/home_sertifk.html', {
        'sertifkalibrasi': sertifkalibrasi
    })

@login_required
def sertif_kalibrasi(request):
    if request.method == 'POST':
        form = SertifKalibrasiform(request.POST, request.FILES)
        if form.is_valid():
            new_submitdate = form.cleaned_data['submit_date']
            new_location = form.cleaned_data['location']
            new_filename = form.cleaned_data['file_name']
            new_machine = form.cleaned_data['machine']
            new_serial = form.cleaned_data['serial']
            new_file = form.cleaned_data['pdf_file']

            new_sertifkalibrasi = Sertifkalibrasi(
                user=request.user,
                submit_date = new_submitdate,
                location = new_location,
                file_name = new_filename,
                machine = new_machine,
                serial = new_serial,
                pdf_file = new_file
            )
            new_sertifkalibrasi.save()
            return render(request, 'myapp/kalibrasi/upload_kalibrasi.html', {
                'form': Kalibrasiform(),
                'success': True
            })
    else:
        form = SertifKalibrasiform()
    return render(request, 'myapp/kalibrasi/upload_kalibrasi.html', {'form': form})


def view_sertifk(request, id):
    sertifkalibrasi = Sertifkalibrasi.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_sertifkalibrasi'))

@login_required
def focus_sertifk(request, id):
    pdf = get_object_or_404(Sertifkalibrasi, pk=id, user=request.user)
    response = HttpResponse(pdf.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{pdf.file_name}.pdf"'
    return response

def edit_sertifkalibrasi(request, id):
    if request.method == 'POST':
        sertifkalibrasi = Sertifkalibrasi.objects.get(pk=id)
        form = SertifKalibrasiform(request.POST, instance=sertifkalibrasi)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/kalibrasi/edit_sertifk.html', {
                'form': form,
                'success': True
            })
    else:
        sertifkalibrasi = Sertifkalibrasi.objects.get(pk=id)
        form = SertifKalibrasiform(instance=sertifkalibrasi)
    return render(request, 'myapp/kalibrasi/edit_sertifk.html', {
        'form': form
    })

def delete_sertifkalibrasi(request, id):
    if request.method == 'POST':
        sertifkalibrasi = Sertifkalibrasi.objects.get(pk=id)
        sertifkalibrasi.delete()
    return HttpResponseRedirect(reverse('home_sertifkalibrasi'))


# UJI KESESUAIAN
@login_required
def home_ukes(request):
    ukes = Ukes.objects.filter(user=request.user)
    return render(request, 'myapp/ukes/ukes.html', {
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
            new_ukes = form.save(commit=False)
            new_ukes.user = request.user
            new_ukes.save()
            return render(request, 'myapp/ukes/add_ukes.html', {
                'form': Ukesform(),
                'success': True
            })
    else:
        form = Ukesform()
    
    return render(request, 'myapp/ukes/add_ukes.html', {
        'form': form
    })

def edit_ukes(request, id):
    if request.method == 'POST':
        ukes = Ukes.objects.get(pk=id)
        form = Ukesform(request.POST, instance=ukes)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/ukes/edit_ukes.html', {
                'form': form,
                'success': True
            })
    else:
        ukes = Ukes.objects.get(pk=id)
        form = Ukesform(instance=ukes)
    return render(request, 'myapp/ukes/edit_ukes.html', {
        'form': form
    })

def delete_ukes(request, id):
    if request.method == 'POST':
        ukes = Ukes.objects.get(pk=id)
        ukes.delete()
    return HttpResponseRedirect(reverse('home_ukes'))

# SERTIFIKAT UKES
@login_required
def home_sertifukes(request):
    sertifukes = Sertifukes.objects.filter(user=request.user)
    return render(request, 'myapp/ukes/home_sertifukes.html', {
        'sertifukes': sertifukes
    })

@login_required
def add_sertifukes(request):
    if request.method == 'POST':
        form = Sertifukesform(request.POST, request.FILES)
        if form.is_valid():
            new_submitdate = form.cleaned_data['submit_date']
            new_location = form.cleaned_data['location']
            new_filename = form.cleaned_data['file_name']
            new_machine = form.cleaned_data['machine']
            new_serial = form.cleaned_data['serial']
            new_file = form.cleaned_data['pdf_file']

            new_sertifukes = Sertifukes(
                user=request.user,
                submit_date = new_submitdate,
                location = new_location,
                file_name = new_filename,
                machine = new_machine,
                serial = new_serial,
                pdf_file = new_file
            )
            new_sertifukes.save()
            return render(request, 'myapp/ukes/upload_sertifukes.html', {
                'form': Sertifukesform(),
                'success': True,
            })
    else:
        form = Sertifukesform()
    return render(request, 'myapp/ukes/upload_sertifukes.html', {'form': form})


def view_sertifukes(request, id):
    sertifukes = Sertifukes.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_sertifukes'))

@login_required
def focus_sertifukes(request, id):
    pdf = get_object_or_404(Sertifukes, pk=id, user=request.user)
    response = HttpResponse(pdf.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{pdf.file_name}.pdf"'
    return response

def edit_sertifukes(request, id):
    if request.method == 'POST':
        sertifukes = Sertifukes.objects.get(pk=id)
        form = Sertifukesform(request.POST, instance=sertifukes)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/ukes/edit_sertifukes.html', {
                'form': form,
                'success': True
            })
    else:
        sertifukes = Sertifukes.objects.get(pk=id)
        form = Sertifukesform(instance=sertifukes)
    return render(request, 'myapp/ukes/edit_sertifukes.html', {
        'form': form
    })

def delete_sertifukes(request, id):
    if request.method == 'POST':
        sertifukes = Sertifukes.objects.get(pk=id)
        sertifukes.delete()
    return HttpResponseRedirect(reverse('home_sertifukes'))


# SERVICE REPORT
@login_required
def home_service(request):
    if request.user.is_tro:
        return HttpResponseForbidden("Access Denied! Sorry You Cannot Access This Page")
    service = Service.objects.filter(user=request.user)
    return render(request, 'myapp/service_report/service.html', {
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
            new_servicetype = form.cleaned_data['service_type']
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

            new_service = Service(
                user=request.user,
                task_date = new_taskdate,
                service_type = new_servicetype,
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
            )
            new_service.save()
            return render(request, 'myapp/service_report/add_service.html', {
                'form': Serviceform(),
                'success': True
            })
    else:
        form = Serviceform(),
    return render(request, 'myapp/service_report/add_service.html', {
        'form': Serviceform()
    })

def edit_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        form = Serviceform(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/service_report/edit_service.html', {
                'form': form,
                'success': True
            })
    else:
        service = Service.objects.get(pk=id)
        form = Serviceform(instance=service)
    return render(request, 'myapp/service_report/edit_service.html', {
        'form': form
    })

def delete_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        service.delete()
    return HttpResponseRedirect(reverse('home_service'))

# PEMELIHARAAN PREVENTIF
@login_required
def home_maintenance(request):
    if request.user.is_tro:
        return HttpResponseForbidden("Access Denied! Sorry You Cannot Access This Page")
    maintenance = Maintenance.objects.filter(user=request.user)
    return render(request, 'myapp/pm/maintenance.html', {
        'maintenance': maintenance
    })

def view_maintenance(request, id):
    maintenance = Maintenance.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home_maintenance'))

@login_required
def add_maintenance(request):
    if request.method == 'POST':
        form = Maintenanceform(request.POST)
        if form.is_valid():
            new_maintenance = form.save(commit=False)
            new_maintenance.user = request.user
            new_maintenance.save()
            return render(request, 'myapp/pm/add_maintenance.html', {
                'form': Maintenanceform(),
                'success': True
            })
    else:
        form = Maintenanceform()
    
    return render(request, 'myapp/pm/add_maintenance.html', {
        'form': form
    })

# @login_required
# def add_maintenance(request):
#     if request.method == 'POST':
#         form = Maintenanceform(request.POST)
#         if form.is_valid():
#             new_taskdate = form.cleaned_data['task_date']
#             new_location = form.cleaned_data['location']
#             new_period = form.cleaned_data['period']
#             new_hospital_unit = form.cleaned_data['hospital_unit']
#             new_xray_brand = form.cleaned_data['xray_brand']
#             new_xray_type = form.cleaned_data['xray_type']
#             new_xray_serial = form.cleaned_data['xray_serial']
#             new_ctrl_panel_cond = form.cleaned_data['ctrl_panel_cond']
#             new_cmd_arm_cond = form.cleaned_data['cmd_arm_cond']
#             new_bucky_tbl_cond = form.cleaned_data['bucky_tbl_cond']
#             new_bucky_std_cond = form.cleaned_data['bucky_std_cond']
#             new_tube_std_cond = form.cleaned_data['tube_std_cond']
#             new_generator_cond = form.cleaned_data['generator_cond']
#             new_tube_spt_cond = form.cleaned_data['tube_spt_cond']
#             new_el_cable_cond = form.cleaned_data['el_cable_cond']
#             new_htt_cable_cond = form.cleaned_data['htt_cable_cond']
#             new_psu_cond = form.cleaned_data['psu_cond']
#             new_cable_cond = form.cleaned_data['cable_cond']
#             new_sw_cond = form.cleaned_data['sw_cond']
#             new_ind_lamp_cond = form.cleaned_data['ind_lamp_cond']
#             new_col_lamp_cond = form.cleaned_data['col_lamp_cond']
#             new_sel_cond = form.cleaned_data['sel_cond']
#             new_tube_lock_cond = form.cleaned_data['tube_lock_cond']
#             new_panel_ctl_cond = form.cleaned_data['panel_ctl_cond']
#             new_buck_lock_cond = form.cleaned_data['buck_lock_cond']

#             new_kvp_acr = form.cleaned_data['kvp_acr']
#             new_kvp_std = form.cleaned_data['kvp_std']
#             new_kvp_tol = form.cleaned_data['kvp_tol']
#             new_kvp_set = form.cleaned_data['kvp_set']
#             new_kvp_output = form.cleaned_data['kvp_output']
#             new_kvp_ok = form.cleaned_data['kvp_ok']
#             new_kvp_not = form.cleaned_data['kvp_not']

#             new_ma_acr = form.cleaned_data['ma_acr']
#             new_ma_std = form.cleaned_data['ma_std']
#             new_ma_tol = form.cleaned_data['ma_tol']
#             new_ma_set = form.cleaned_data['ma_set']
#             new_ma_output = form.cleaned_data['ma_output']
#             new_ma_ok = form.cleaned_data['ma_ok']
#             new_ma_not = form.cleaned_data['ma_not']

#             new_ln_ma_acr = form.cleaned_data['ln_ma_acr']
#             new_ln_ma_std = form.cleaned_data['ln_ma_std']
#             new_ln_ma_tol = form.cleaned_data['ln_ma_tol']
#             new_ln_ma_set = form.cleaned_data['ln_ma_set']
#             new_ln_ma_output = form.cleaned_data['ln_ma_output']
#             new_ln_ma_ok = form.cleaned_data['ln_ma_ok']
#             new_ln_ma_not = form.cleaned_data['ln_ma_not']

#             new_expose_acr = form.cleaned_data['expose_acr']
#             new_expose_std = form.cleaned_data['expose_std']
#             new_expose_tol = form.cleaned_data['expose_tol']
#             new_expose_set = form.cleaned_data['expose_set']
#             new_expose_output = form.cleaned_data['expose_output']
#             new_expose_ok = form.cleaned_data['exp_ok']
#             new_expose_not = form.cleaned_data['exp_not']

#             new_rad_area_acr = form.cleaned_data['rad_area_acr']
#             new_rad_area_std = form.cleaned_data['rad_area_std']
#             new_rad_area_tol = form.cleaned_data['rad_area_tol']
#             new_rad_area_set = form.cleaned_data['rad_area_set']
#             new_rad_area_output = form.cleaned_data['rad_area_output']
#             new_rad_area_ok = form.cleaned_data['rad_area_ok']
#             new_rad_area_not = form.cleaned_data['rad_area_not']

#             new_exp_in_acr = form.cleaned_data['exp_in_acr']
#             new_exp_in_std = form.cleaned_data['exp_in_std']
#             new_exp_in_tol = form.cleaned_data['exp_in_tol']
#             new_exp_in_set = form.cleaned_data['exp_in_set']
#             new_exp_in_output = form.cleaned_data['exp_in_output']
#             new_exp_in_ok = form.cleaned_data['exp_in_ok']
#             new_exp_in_not = form.cleaned_data['exp_in_not']

#             new_amp_leak_acr = form.cleaned_data['amp_leak_acr']
#             new_amp_leak_std = form.cleaned_data['amp_leak_std']
#             new_amp_leak_tol = form.cleaned_data['amp_leak_tol']
#             new_amp_leak_set = form.cleaned_data['amp_leak_set']
#             new_amp_leak_output = form.cleaned_data['amp_leak_output']
#             new_amp_leak_ok = form.cleaned_data['amp_leak_ok']
#             new_amp_leak_not = form.cleaned_data['amp_leak_not']

#             new_cbl_gnd_acr = form.cleaned_data['cbl_gnd_acr']
#             new_cbl_gnd_std = form.cleaned_data['cbl_gnd_std']
#             new_cbl_gnd_tol = form.cleaned_data['cbl_gnd_tol']
#             new_cbl_gnd_set = form.cleaned_data['cbl_gnd_set']
#             new_cbl_gnd_output = form.cleaned_data['cbl_gnd_output']
#             new_cbl_gnd_ok = form.cleaned_data['cbl_gnd_ok']
#             new_cbl_gnd_not = form.cleaned_data['cbl_gnd_not']

#             new_rad_leak_acr = form.cleaned_data['rad_leak_acr']
#             new_rad_leak_std = form.cleaned_data['rad_leak_std']
#             new_rad_leak_tol = form.cleaned_data['rad_leak_tol']
#             new_rad_leak_set = form.cleaned_data['rad_leak_set']
#             new_rad_leak_output = form.cleaned_data['rad_leak_output']
#             new_rad_leak_ok = form.cleaned_data['rad_leak_ok']
#             new_rad_leak_not = form.cleaned_data['rad_leak_not']
#             new_ispassed = form.cleaned_data['is_passed']
#             new_isfailed = form.cleaned_data['is_failed']

#             new_maintenance = Maintenance(
#                 user = request.user,
#                 task_date = new_taskdate,
#                 location = new_location,
#                 period = new_period,
#                 hospital_unit = new_hospital_unit,
#                 xray_brand = new_xray_brand,
#                 xray_type = new_xray_type,
#                 xray_serial = new_xray_serial,
#                 ctrl_panel_cond = new_ctrl_panel_cond,
#                 cmd_arm_cond = new_cmd_arm_cond,
#                 bucky_tbl_cond = new_bucky_tbl_cond,
#                 bucky_std_cond = new_bucky_std_cond,
#                 tube_std_cond = new_tube_std_cond,
#                 generator_cond = new_generator_cond,

#                 tube_spt_cond = new_tube_spt_cond,
#                 el_cable_cond = new_el_cable_cond,
#                 htt_cable_cond = new_htt_cable_cond,
#                 psu_cond = new_psu_cond,
#                 cable_cond = new_cable_cond,
#                 sw_cond = new_sw_cond,
#                 ind_lamp_cond = new_ind_lamp_cond, 
#                 col_lamp_cond = new_col_lamp_cond,
#                 sel_cond = new_sel_cond,
#                 tube_lock_cond = new_tube_lock_cond,
#                 panel_ctl_cond = new_panel_ctl_cond,
#                 buck_lock_cond = new_buck_lock_cond,

#                 kvp_acr = new_kvp_acr,
#                 kvp_std = new_kvp_std,
#                 kvp_tol = new_kvp_tol,
#                 kvp_set = new_kvp_set,
#                 kvp_output = new_kvp_output,
#                 kvp_ok = new_kvp_ok,
#                 kvp_not = new_kvp_not,

#                 ma_acr = new_ma_acr,
#                 ma_std = new_ma_std,
#                 ma_tol = new_ma_tol,
#                 ma_set = new_ma_set,
#                 ma_output = new_ma_output,
#                 ma_ok = new_ma_ok,
#                 ma_not = new_ma_not,

#                 ln_ma_acr = new_ln_ma_acr,
#                 ln_ma_std = new_ln_ma_std,
#                 ln_ma_tol = new_ln_ma_tol,
#                 ln_ma_set = new_ln_ma_set,
#                 ln_ma_output = new_ln_ma_output,
#                 ln_ma_ok = new_ln_ma_ok,
#                 ln_ma_not = new_ln_ma_not,

#                 expose_acr = new_expose_acr,
#                 expose_std = new_expose_std,
#                 expose_tol = new_expose_tol,
#                 expose_set = new_expose_set,
#                 expose_output = new_expose_output,
#                 exp_ok = new_expose_ok,
#                 exp_not = new_expose_not,

#                 rad_area_acr = new_rad_area_acr,
#                 rad_area_std = new_rad_area_std,
#                 rad_area_tol = new_rad_area_tol,
#                 rad_area_set = new_rad_area_set,
#                 rad_area_output = new_rad_area_output,
#                 rad_area_ok = new_rad_area_ok,
#                 rad_area_not = new_rad_area_not,

#                 exp_in_acr = new_exp_in_acr,
#                 exp_in_std = new_exp_in_std,
#                 exp_in_tol = new_exp_in_tol,
#                 exp_in_set = new_exp_in_set,
#                 exp_in_output = new_exp_in_output,
#                 exp_in_ok = new_exp_in_ok,
#                 exp_in_not = new_exp_in_not,

#                 amp_leak_acr = new_amp_leak_acr,
#                 amp_leak_std = new_amp_leak_std,
#                 amp_leak_tol = new_amp_leak_tol,
#                 amp_leak_set = new_amp_leak_set,
#                 amp_leak_output = new_amp_leak_output,
#                 amp_leak_ok = new_amp_leak_ok,
#                 amp_leak_not = new_amp_leak_not,

#                 cbl_gnd_acr = new_cbl_gnd_acr,
#                 cbl_gnd_std = new_cbl_gnd_std,
#                 cbl_gnd_tol = new_cbl_gnd_tol,
#                 cbl_gnd_set = new_cbl_gnd_set,
#                 cbl_gnd_output = new_cbl_gnd_output,
#                 cbl_gnd_ok = new_cbl_gnd_ok,
#                 cbl_gnd_not = new_cbl_gnd_not,

#                 rad_leak_acr = new_rad_leak_acr,
#                 rad_leak_std = new_rad_leak_std,
#                 rad_leak_tol = new_rad_leak_tol,
#                 rad_leak_set = new_rad_leak_set,
#                 rad_leak_output = new_rad_leak_output,    
#                 rad_leak_ok = new_rad_leak_ok,
#                 rad_leak_not = new_rad_leak_not,

#                 is_passed = new_ispassed,
#                 is_failed = new_isfailed,  
#             )
#             new_maintenance.save()
#             return render(request, 'myapp/pm/add_maintenance.html', {
#                 'form': Maintenanceform(),
#                 'success': True
#             })
#     else:
#         form = Maintenanceform(),
#     return render(request, 'myapp/pm/add_maintenance.html', {
#         'form': Maintenanceform()
#     })

def edit_maintenance(request, id):
    if request.method == 'POST':
        maintenance = Maintenance.objects.get(pk=id)
        form = Maintenanceform(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/pm/edit_maintenance.html', {
                'form': form,
                'success': True
            })
    else:
        maintenance = Maintenance.objects.get(pk=id)
        form = Maintenanceform(instance=maintenance)
    return render(request, 'myapp/pm/edit_maintenance.html', {
        'form': form
    })

def delete_maintenance(request, id):
    if request.method == 'POST':
        maintenance = Maintenance.objects.get(pk=id)
        maintenance.delete()
    return HttpResponseRedirect(reverse('home_maintenance'))

# USERS GUIDE

def usersguide(request):
    return render(request, 'myapp/usersguide.html')