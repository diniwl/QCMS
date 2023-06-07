from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Schedule, Penerimaan, Kalibrasi, Ukes, Service, Sertifkalibrasi, Sertifukes, Maintenance

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
    CHOICES = (
        (1, 'Baik'),
        (2, 'Tidak baik'),
        (3, 'Penggantian part'),
        (4, 'Perbaikan'),
        (5, 'Adjustment'),
        (6, 'Penguatan'),
        (7, 'Pembersihan'),
        (8, 'Lubrikasi'),
    )
    
    gnd_cable: forms.ChoiceField(choices=CHOICES)
    ln_vol: forms.ChoiceField(choices=CHOICES)
    hv_cable: forms.ChoiceField(choices=CHOICES)
    lv_cable: forms.ChoiceField(choices=CHOICES)
    rail: forms.ChoiceField(choices=CHOICES)
    std_spt: forms.ChoiceField(choices=CHOICES)
    asb_tube: forms.ChoiceField(choices=CHOICES)
    asb_col: forms.ChoiceField(choices=CHOICES)
    lamp: forms.ChoiceField(choices=CHOICES)
    bout: forms.ChoiceField(choices=CHOICES)

    gen_item1: forms.ChoiceField(choices=CHOICES)
    gen_item2: forms.ChoiceField(choices=CHOICES)
    gen_item3: forms.ChoiceField(choices=CHOICES)

    tube_std_item1: forms.ChoiceField(choices=CHOICES)
    tube_std_item2: forms.ChoiceField(choices=CHOICES)

    tube_sp_item1: forms.ChoiceField(choices=CHOICES)
    tube_sp_item2: forms.ChoiceField(choices=CHOICES)

    bld_item1: forms.ChoiceField(choices=CHOICES)
    bld_item2: forms.ChoiceField(choices=CHOICES)
    bld_item3: forms.ChoiceField(choices=CHOICES)
    bld_item4: forms.ChoiceField(choices=CHOICES)
    bld_item5: forms.ChoiceField(choices=CHOICES)
    bld_item6: forms.ChoiceField(choices=CHOICES)
    bld_item7: forms.ChoiceField(choices=CHOICES)

    acu_item1: forms.ChoiceField(choices=CHOICES)

    bucky_tbl_item1: forms.ChoiceField(choices=CHOICES)
    bucky_tbl_item1: forms.ChoiceField(choices=CHOICES)

    bucky_std_item1: forms.ChoiceField(choices=CHOICES)
    bucky_std_item2: forms.ChoiceField(choices=CHOICES)

    system: forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Penerimaan
        fields = ['task_date', 'location', 'hos_unit', 'tech_name', 'tube_std_brand', 'tube_std_model', 'tube_std_serial', 'tube_std_is_okay',
                  'tube_spt_brand', 'tube_spt_model', 'tube_spt_serial', 'tube_spt_is_okay', 'tube_asb_brand', 'tube_asb_model', 'tube_asb_serial', 'tube_asb_is_okay',
                  'beam_ld_brand', 'beam_ld_model', 'beam_ld_serial', 'beam_ld_is_okay', 'htt_brand', 'htt_model', 'htt_serial', 'htt_is_okay', 'flo_buck_brand', 'flo_buck_model', 
                  'flo_buck_serial', 'flo_buck_is_okay', 'lev_buck_brand', 'lev_buck_model', 'lev_buck_serial', 'lev_buck_is_okay', 'buck_std_brand', 'buck_std_model', 'buck_std_serial', 
                  'buck_std_is_okay', 'acu_brand', 'acu_model', 'acu_serial', 'acu_is_okay', 'fork_brand', 'fork_model', 'fork_serial', 'fork_is_okay', 'gnd_cable', 'ln_vol', 'hv_cable', 'lv_cable',
                  'rail', 'std_spt', 'asb_tube', 'asb_col', 'lamp', 'bout', 'gen_item1', 'gen_item2', 'gen_item3', 'tube_std_item1', 'tube_std_item2', 'tube_sp_item1', 'tube_sp_item2', 'bld_item1', 'bld_item2', 'bld_item3', 'bld_item4', 'bld_item5', 'bld_item6', 
                  'bld_item7', 'acu_item1', 'bucky_tbl_item1', 'bucky_tbl_item2', 'bucky_std_item1', 'bucky_std_item2', 'system', 'is_passed', 'is_failed']
        
        labels = {
            'task_date': 'Scheduled Date',
            'location': 'Location',
            'hos_unit': 'Hospital Unit',
            'tech_name': "Technician's Name",
            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
            'tube_std_brand' : 'Brand', 
            'tube_std_model': 'Model', 
            'tube_std_serial': 'Serial', 
            'tube_std_is_okay': '',
            'tube_spt_brand': 'Brand', 
            'tube_spt_model': 'Model', 
            'tube_spt_serial': 'Serial', 
            'tube_spt_is_okay': '', 
            'tube_asb_brand': 'Brand', 
            'tube_asb_model': 'Model', 
            'tube_asb_serial': 'Serial', 
            'tube_asb_is_okay': '',
            'beam_ld_brand': 'Brand', 
            'beam_ld_model': 'Model', 
            'beam_ld_serial': 'Serial',
            'beam_ld_is_okay': '', 
            'htt_brand':'Brand', 
            'htt_model': 'Model', 
            'htt_serial': 'Serial', 
            'htt_is_okay': '', 
            'flo_buck_brand': 'Brand', 
            'flo_buck_model': 'Model', 
            'flo_buck_serial': 'Serial', 
            'flo_buck_is_okay': '',
            'lev_buck_brand': 'Brand', 
            'lev_buck_model': 'Model',
            'lev_buck_serial': 'Serial', 
            'lev_buck_is_okay': '', 
            'buck_std_brand': 'Brand', 
            'buck_std_model': 'Model', 
            'buck_std_serial': 'Serial', 
            'buck_std_is_okay': '', 
            'acu_brand': 'Brand', 
            'acu_model': 'Model', 
            'acu_serial': 'Serial', 
            'acu_is_okay': '', 
            'fork_brand': 'Brand', 
            'fork_model': 'Model', 
            'fork_serial': 'Serial', 
            'fork_is_okay': '',
            'gnd_cable': '', 
            'ln_vol': '', 
            'hv_cable': '', 
            'lv_cable' : '',
            'rail': '', 
            'std_spt': '', 
            'asb_tube' : '', 
            'asb_col': '', 
            'lamp' : '', 
            'bout': '', 
            'gen_item1': '', 
            'gen_item2': '', 
            'gen_item3': '', 
            'tube_std_item1': '', 
            'tube_std_item2': '', 
            'tube_sp_item1': '', 
            'tube_sp_item2': '',            
            'bld_item1': '', 
            'bld_item2': '', 
            'bld_item3': '', 
            'bld_item4': '', 
            'bld_item5':' ', 
            'bld_item6': '', 
            'bld_item7': '', 
            'acu_item1': '', 
            'bucky_tbl_item1': '', 
            'bucky_tbl_item2': '', 
            'bucky_std_item1': '', 
            'bucky_std_item2': '', 
            'system': '', 
            'is_passed' : 'Passed', 
            'is_failed' : 'Failed'
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'hos_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'tech_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tube_std_brand' : forms.TextInput(attrs={'class': 'form-control'}), 
            'tube_std_model': forms.TextInput(attrs={'class': 'form-control'}),
            'tube_std_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'tube_std_is_okay': forms.CheckboxInput(),
            'tube_spt_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'tube_spt_model': forms.TextInput(attrs={'class': 'form-control'}),
            'tube_spt_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'tube_spt_is_okay': forms.CheckboxInput(),
            'tube_asb_brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'tube_asb_model': forms.TextInput(attrs={'class': 'form-control'}), 
            'tube_asb_serial': forms.TextInput(attrs={'class': 'form-control'}),  
            'tube_asb_is_okay': forms.CheckboxInput(),
            'beam_lb_brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'beam_lb_model': forms.TextInput(attrs={'class': 'form-control'}), 
            'beam_lb_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'beam_lb_is_okay': forms.CheckboxInput(),
            'htt_brand': forms.TextInput(attrs={'class': 'form-control'}),  
            'htt_model': forms.TextInput(attrs={'class': 'form-control'}), 
            'htt_serial': forms.TextInput(attrs={'class': 'form-control'}),  
            'htt_is_okay': forms.CheckboxInput(), 
            'flo_buck_brand': forms.TextInput(attrs={'class': 'form-control'}),  
            'flo_buck_model': forms.TextInput(attrs={'class': 'form-control'}),  
            'flo_buck_serial': forms.TextInput(attrs={'class': 'form-control'}),  
            'flo_buck_is_okay': forms.CheckboxInput(),
            'lev_buck_brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'lev_buck_model': forms.TextInput(attrs={'class': 'form-control'}), 
            'lev_buck_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'lev_buck_is_okay': forms.CheckboxInput(),
            'buck_std_brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'buck_std_model': forms.TextInput(attrs={'class': 'form-control'}),  
            'buck_std_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'buck_std_is_okay': forms.CheckboxInput(), 
            'acu_brand': forms.TextInput(attrs={'class': 'form-control'}),  
            'acu_model': forms.TextInput(attrs={'class': 'form-control'}),  
            'acu_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'acu_is_okay': forms.CheckboxInput(), 
            'fork_brand': forms.TextInput(attrs={'class': 'form-control'}),  
            'fork_model': forms.TextInput(attrs={'class': 'form-control'}), 
            'fork_serial': forms.TextInput(attrs={'class': 'form-control'}), 
            'fork_is_okay': forms.CheckboxInput(),
            'is_passed' : forms.CheckboxInput(),
            'is_failed' : forms.CheckboxInput(),
        }

#KALIBRASI
class Kalibrasiform(forms.ModelForm):
    class Meta:
        model = Kalibrasi
        fields = ['task_date', 'location', 'tech_name', 'xray_tube_brand', 'xray_tube_type', 'xray_tube_serial', 'xray_gen_brand', 'xray_gen_type', 'xray_gen_serial', 'temp_before', 
                  'temp_after', 'hum_before', 'hum_after', 'kv_set1', 'kv_set2', 'kv_set3', 'kv1', 'kv2', 'kv3', 'kv4', 'kv5', 'kv6' , 'kv7', 'kv8', 'kv9', 'kv_avg1', 'kv_avg2', 'kv_avg3',
                  'kv_dev1', 'kv_dev2', 'kv_dev3', 'kv_prc1', 'kv_prc2', 'kv_prc3', 'ma_set1', 'ma_set2', 'ma_set3', 'ma1', 'ma2', 'ma3', 'ma4', 'ma5', 'ma6', 'ma7', 'ma8', 'ma9', 'ma_avg1',
                  'ma_avg2', 'ma_avg3', 'ma_dev1', 'ma_dev2', 'ma_dev3', 'ma_prc1', 'ma_prc2', 'ma_prc3', 'is_passed', 'is_failed']
        labels = {
            'task_date': 'Scheduled Date',
            'location': 'Location',
            'tech_name': "Technician's Name",

            'xray_tube_brand': 'Brand',
            'xray_tube_type': 'Type',
            'xray_tube_serial': 'Serial',

            'xray_gen_brand': 'Brand',
            'xray_gen_type': 'Type',
            'xray_gen_serial': 'Serial',

            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'tech_name': forms.TextInput(attrs={'class': 'form-control'}),

            'xray_tube_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'xray_tube_type': forms.TextInput(attrs={'class': 'form-control'}),
            'xray_tube_serial': forms.TextInput(attrs={'class': 'form-control'}),

            'xray_gen_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'xray_gen_type': forms.TextInput(attrs={'class': 'form-control'}),
            'xray_gen_serial': forms.TextInput(attrs={'class': 'form-control'}),

            'temp_before': forms.NumberInput(attrs={'class': 'form-control'}),
            'temp_after': forms.NumberInput(attrs={'class': 'form-control'}),
            'hum_before': forms.NumberInput(attrs={'class': 'form-control'}),
            'hum_after': forms.NumberInput(attrs={'class': 'form-control'}),

            'kv_set1': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_set2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_set3': forms.NumberInput(attrs={'class': 'form-control'}),

            'kv1': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv3': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv4': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv5': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv6': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv7': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv8': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv9': forms.NumberInput(attrs={'class': 'form-control'}),

            'kv_avg1': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_avg2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_avg3': forms.NumberInput(attrs={'class': 'form-control'}),
   
            'kv_dev1': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_dev2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_dev3': forms.NumberInput(attrs={'class': 'form-control'}),

            'kv_prc1': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_prc2': forms.NumberInput(attrs={'class': 'form-control'}),
            'kv_prc3': forms.NumberInput(attrs={'class': 'form-control'}),

            'ma_set1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_set2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_set3': forms.NumberInput(attrs={'class': 'form-control'}),

            'ma1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma3': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma4': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma5': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma6': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma7': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma8': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma9': forms.NumberInput(attrs={'class': 'form-control'}),

            'ma_avg1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_avg2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_avg3': forms.NumberInput(attrs={'class': 'form-control'}),
   
            'ma_dev1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_dev2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_dev3': forms.NumberInput(attrs={'class': 'form-control'}),

            'ma_prc1': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_prc2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ma_prc3': forms.NumberInput(attrs={'class': 'form-control'}),

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
        fields = '__all__'
        labels = {
            'task_date': 'Scheduled Date',
            'location': 'Location',
            'tech_name': "Technician's Name",

            'xray_tube_brand': 'Brand',
            'xray_tube_type': 'Type',
            'xray_tube_serial': 'Serial',

            'xray_gen_brand': 'Brand',
            'xray_gen_type': 'Type',
            'xray_gen_serial': 'Serial',

            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }

#SERTIF UKES
class Sertifukesform(forms.ModelForm):
    class Meta:
        model = Sertifukes
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
            'service_type': "Type of service",
            'brand': 'Brand',
            'type' : 'Type',
            'serial': 'Serial',
            'address': "Customer's address",
            'problem': 'Problem/Request',
            'repair': 'Repair comments',
            'cust_name': "Customer's identity",
            'tech_name': "Technician's identity",
            'complain_num': "Document's Number",
            'is_completed': 'Completed',
            'is_continue': 'Continue',
        }

        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}), 
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'problem': forms.TextInput(attrs={'class': 'form-control'}),
            'repair': forms.Textarea(attrs={'class': 'form-control'}),
            'cust_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tech_name': forms.TextInput(attrs={'class': 'form-control'}),
            'complain_num': forms.TextInput(attrs={'class': 'form-control'}),
            'is_completed' : forms.CheckboxInput(),
            'is_continue' : forms.CheckboxInput(),
        }

#MAINTENANCE
class Maintenanceform(forms.ModelForm):
    CHOICES = (
        ('ANNUAL', 'Annual'),
        ('SEMI-ANNUAL', 'Semi-annual'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
    )

    COND = (
        ('BAIK', 'Baik'),
        ('TIDAK BAIK', 'Tidak baik'),
        ('PENGGANTIAN PART', 'Penggantian part'),
        ('PERBAIKAN', 'Perbaikan'),
        ('ADJUSTMENT', 'Adjustment'),
        ('PENGUATAN', 'Penguatan'),
        ('PEMBERSIHAN', 'Pembersihan'),
        ('LUBRIKASI', 'Lubrikasi'),
    )

    period = forms.ChoiceField(choices=CHOICES)
    ctrl_panel_cond = forms.ChoiceField(choices=COND)
    cmd_arm_cond = forms.ChoiceField(choices=COND)
    bucky_tbl_cond = forms.ChoiceField(choices=COND)
    bucky_std_cond = forms.ChoiceField(choices=COND)
    tube_std_cond = forms.ChoiceField(choices=COND)
    generator_cond = forms.ChoiceField(choices=COND)
    tube_spt_cond = forms.ChoiceField(choices=COND)
    el_cable_cond = forms.ChoiceField(choices=COND)
    htt_cable_cond = forms.ChoiceField(choices=COND)
    psu_cond = forms.ChoiceField(choices=COND)
    cable_cond = forms.ChoiceField(choices=COND)
    sw_cond = forms.ChoiceField(choices=COND)
    ind_lamp_cond = forms.ChoiceField(choices=COND)
    col_lamp_cond = forms.ChoiceField(choices=COND)
    sel_cond = forms.ChoiceField(choices=COND)
    tube_lock_cond = forms.ChoiceField(choices=COND)
    panel_ctl_cond = forms.ChoiceField(choices=COND)
    buck_lock_cond = forms.ChoiceField(choices=COND)

    class Meta:
        model = Maintenance
        fields = ['task_date', 'location', 'period', 'hospital_unit', 'xray_brand', 'xray_type', 'xray_serial', 'ctrl_panel_cond', 'cmd_arm_cond', 'bucky_tbl_cond', 'bucky_std_cond', 'tube_std_cond', 'generator_cond',
                  'tube_spt_cond', 'el_cable_cond', 'htt_cable_cond', 'psu_cond', 'cable_cond', 'sw_cond', 'ind_lamp_cond', 'col_lamp_cond', 'sel_cond', 'tube_lock_cond', 'panel_ctl_cond', 'buck_lock_cond', 
                  'kvp_std', 'kvp_tol', 'kvp_set', 'kvp_output', 'kvp_ok', 'kvp_not', 
                  'ma_std', 'ma_tol', 'ma_set', 'ma_output', 'ma_ok', 'ma_not', 
                  'ln_ma_std', 'ln_ma_tol', 'ln_ma_set', 'ln_ma_output', 'ln_ma_ok', 'ln_ma_not',
                  'expose_std', 'expose_tol', 'expose_set', 'expose_output', 'exp_ok', 'exp_not', 
                  'rad_area_std', 'rad_area_tol', 'rad_area_set', 'rad_area_output', 'rad_area_ok', 'rad_area_not',
                  'exp_in_std', 'exp_in_tol', 'exp_in_set', 'exp_in_output', 'exp_in_ok', 'exp_in_not', 
                  'amp_leak_std', 'amp_leak_tol', 'amp_leak_set', 'amp_leak_output', 'amp_leak_ok', 'amp_leak_not', 
                  'cbl_gnd_std', 'cbl_gnd_tol', 'cbl_gnd_set', 'cbl_gnd_output', 'cbl_gnd_ok', 'cbl_gnd_not', 
                  'rad_leak_std', 'rad_leak_tol', 'rad_leak_set', 'rad_leak_output', 'rad_leak_ok', 'rad_leak_not', 'is_passed', 'is_failed']
        
        labels = {
            'task_date': 'Scheduled Date',
            'location': 'Location',
            'period' : 'Maintenance Period',
            'hospital_unit' : 'Hospital Unit',
            'xray_brand' : 'Brand',
            'xray_type' : 'Type',
            'xray_serial' : 'Serial',
            'is_passed' : 'Passed',
            'is_failed' : 'Failed',
        }
        widgets = {
            'task_date': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital_unit': forms.TextInput(attrs={'class': 'form-control'}),
            'xray_brand' : forms.TextInput(attrs={'class': 'form-control'}),
            'xray_type' : forms.TextInput(attrs={'class': 'form-control'}),
            'xray_serial' : forms.TextInput(attrs={'class': 'form-control'}),
            'is_passed' : forms.CheckboxInput(),
            'is_failed' : forms.CheckboxInput(),
        }