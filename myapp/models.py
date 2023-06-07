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
    OK = 'BAIK'
    BAD = 'TIDAK BAIK'
    PART = 'PENGGANTIAN PART'
    SVC = 'PERBAIKAN'
    ADJ = 'ADJUSTMENT'
    STR = 'PENGUATAN'
    CLN = 'PEMBERSIHAN'
    LBC = 'LUBRIKASI'

    CHOICES = (
        (OK, 'Baik'),
        (BAD, 'Tidak baik'),
        (PART, 'Penggantian part'),
        (SVC, 'Perbaikan'),
        (ADJ, 'Adjustment'),
        (STR, 'Penguatan'),
        (CLN, 'Pembersihan'),
        (LBC, 'Lubrikasi'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    location = models.CharField(max_length=150)
    hos_unit = models.CharField(max_length=150)
    tech_name = models.CharField(max_length=150)

    tube_std_brand = models.CharField(max_length=150)
    tube_std_model = models.CharField(max_length=150)
    tube_std_serial = models.CharField(max_length=150)
    tube_std_is_okay = models.BooleanField('okay', default=False)

    tube_spt_brand = models.CharField(max_length=150)
    tube_spt_model = models.CharField(max_length=150)
    tube_spt_serial = models.CharField(max_length=150)
    tube_spt_is_okay = models.BooleanField('okay', default=False)

    tube_asb_brand = models.CharField(max_length=150)
    tube_asb_model = models.CharField(max_length=150)
    tube_asb_serial = models.CharField(max_length=150)
    tube_asb_is_okay = models.BooleanField('okay', default=False)

    beam_ld_brand = models.CharField(max_length=150)
    beam_ld_model = models.CharField(max_length=150)
    beam_ld_serial = models.CharField(max_length=150)
    beam_ld_is_okay = models.BooleanField('okay', default=False)

    htt_brand = models.CharField(max_length=150)
    htt_model = models.CharField(max_length=150)
    htt_serial = models.CharField(max_length=150)
    htt_is_okay = models.BooleanField('okay', default=False)

    flo_buck_brand = models.CharField(max_length=150)
    flo_buck_model = models.CharField(max_length=150)
    flo_buck_serial = models.CharField(max_length=150)
    flo_buck_is_okay = models.BooleanField('okay', default=False)

    lev_buck_brand = models.CharField(max_length=150)
    lev_buck_model = models.CharField(max_length=150)
    lev_buck_serial = models.CharField(max_length=150)
    lev_buck_is_okay = models.BooleanField('okay', default=False)

    buck_std_brand = models.CharField(max_length=150)
    buck_std_model = models.CharField(max_length=150)
    buck_std_serial = models.CharField(max_length=150)
    buck_std_is_okay = models.BooleanField('okay', default=False)

    acu_brand = models.CharField(max_length=150)
    acu_model = models.CharField(max_length=150)
    acu_serial = models.CharField(max_length=150)
    acu_is_okay = models.BooleanField('okay', default=False)

    fork_brand = models.CharField(max_length=150)
    fork_model = models.CharField(max_length=150)
    fork_serial = models.CharField(max_length=150)
    fork_is_okay = models.BooleanField('okay', default=False)

    gnd_cable = models.CharField(max_length=100, choices=CHOICES, default=OK)
    ln_vol = models.CharField(max_length=100, choices=CHOICES, default=OK)
    hv_cable = models.CharField(max_length=100, choices=CHOICES, default=OK)
    lv_cable = models.CharField(max_length=100, choices=CHOICES, default=OK)
    rail = models.CharField(max_length=100, choices=CHOICES, default=OK)
    std_spt = models.CharField(max_length=100, choices=CHOICES, default=OK)
    asb_tube = models.CharField(max_length=100, choices=CHOICES, default=OK)
    asb_col = models.CharField(max_length=100, choices=CHOICES, default=OK)
    lamp = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bout = models.CharField(max_length=100, choices=CHOICES, default=OK)

    gen_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    gen_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    gen_item3 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    tube_std_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    tube_std_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    tube_sp_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    tube_sp_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    bld_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item3 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item4 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item5 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item6 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bld_item7 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    acu_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    bucky_tbl_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bucky_tbl_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    
    bucky_std_item1 = models.CharField(max_length=100, choices=CHOICES, default=OK)
    bucky_std_item2 = models.CharField(max_length=100, choices=CHOICES, default=OK)

    system = models.CharField(max_length=100, choices=CHOICES, default=OK)

    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)

    def clean(self):
        if self.is_passed and self.is_failed:
            raise ValidationError('You can only select one')
        super().clean()
    

#  KALIBRASI
class Kalibrasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)

    location = models.CharField(max_length=150)
    tech_name = models.CharField(max_length=150)
    
    xray_tube_brand = models.CharField(max_length=150)
    xray_tube_type = models.CharField(max_length=150)
    xray_tube_serial = models.CharField(max_length=150)

    xray_gen_brand = models.CharField(max_length=150)
    xray_gen_type = models.CharField(max_length=150)
    xray_gen_serial = models.CharField(max_length=150)

    temp_before = models.FloatField(max_length=10)
    temp_after = models.FloatField(max_length=10)
    hum_before = models.FloatField(max_length=10)
    hum_after = models.FloatField(max_length=10)

    kv_set1 = models.FloatField(max_length=10)
    kv_set2 = models.FloatField(max_length=10)
    kv_set3 = models.FloatField(max_length=10)

    kv1 = models.FloatField(max_length=10)
    kv2 = models.FloatField(max_length=10)
    kv3 = models.FloatField(max_length=10)
    kv4 = models.FloatField(max_length=10)
    kv5 = models.FloatField(max_length=10)
    kv6 = models.FloatField(max_length=10)
    kv7 = models.FloatField(max_length=10)
    kv8 = models.FloatField(max_length=10)
    kv9 = models.FloatField(max_length=10)

    kv_avg1 = models.FloatField(max_length=10)
    kv_avg2 = models.FloatField(max_length=10)
    kv_avg3 = models.FloatField(max_length=10)

    kv_dev1 = models.FloatField(max_length=10)
    kv_dev2 = models.FloatField(max_length=10)
    kv_dev3 = models.FloatField(max_length=10)

    kv_prc1 = models.FloatField(max_length=10)
    kv_prc2 = models.FloatField(max_length=10)
    kv_prc3 = models.FloatField(max_length=10)

    ma_set1 = models.FloatField(max_length=10)
    ma_set2 = models.FloatField(max_length=10)
    ma_set3 = models.FloatField(max_length=10)

    ma1 = models.FloatField(max_length=10)
    ma2 = models.FloatField(max_length=10)
    ma3 = models.FloatField(max_length=10)
    ma4 = models.FloatField(max_length=10)
    ma5 = models.FloatField(max_length=10)
    ma6 = models.FloatField(max_length=10)
    ma7 = models.FloatField(max_length=10)
    ma8 = models.FloatField(max_length=10)
    ma9 = models.FloatField(max_length=10)

    ma_avg1 = models.FloatField(max_length=10)
    ma_avg2 = models.FloatField(max_length=10)
    ma_avg3 = models.FloatField(max_length=10)
 
    ma_dev1 = models.FloatField(max_length=10)
    ma_dev2 = models.FloatField(max_length=10)
    ma_dev3 = models.FloatField(max_length=10)

    ma_prc1 = models.FloatField(max_length=10)
    ma_prc2 = models.FloatField(max_length=10)
    ma_prc3 = models.FloatField(max_length=10)

    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)

    def clean(self):
        if self.is_passed and self.is_failed:
            raise ValidationError('You can only select one')
        super().clean()
    
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

    location = models.CharField(max_length=150)
    tech_name = models.CharField(max_length=150)
    
    xray_tube_brand = models.CharField(max_length=150)
    xray_tube_type = models.CharField(max_length=150)
    xray_tube_serial = models.CharField(max_length=150)

    xray_gen_brand = models.CharField(max_length=150)
    xray_gen_type = models.CharField(max_length=150)
    xray_gen_serial = models.CharField(max_length=150)

    lux_avg = models.FloatField(max_length=10)
    lux_bg = models.FloatField(max_length=10)
    lux_fk = models.FloatField(max_length=10)
    lux_fin = models.FloatField(max_length=10)

    delta_x = models.FloatField(max_length=10)
    delta_y = models.FloatField(max_length=10)
    sigma_xy = models.FloatField(max_length=10)
    
    degree = models.FloatField(max_length=10)

    kv_set1 = models.FloatField(max_length=10)
    kv_set2 = models.FloatField(max_length=10)
    kv_set3 = models.FloatField(max_length=10)
    kv_set4 = models.FloatField(max_length=10)
    kv_set5 = models.FloatField(max_length=10)
    kv_set6 = models.FloatField(max_length=10)
    kv_set7 = models.FloatField(max_length=10)
    kv_set8 = models.FloatField(max_length=10)

    kv_msr1 = models.FloatField(max_length=10)
    kv_msr2 = models.FloatField(max_length=10)
    kv_msr3 = models.FloatField(max_length=10)
    kv_msr4 = models.FloatField(max_length=10)
    kv_msr5 = models.FloatField(max_length=10)
    kv_msr6 = models.FloatField(max_length=10)
    kv_msr7 = models.FloatField(max_length=10)
    kv_msr8 = models.FloatField(max_length=10)
    
    kverror1 = models.FloatField(max_length=10)
    kverror2 = models.FloatField(max_length=10)
    kverror3 = models.FloatField(max_length=10)
    kverror4 = models.FloatField(max_length=10)
    kverror5 = models.FloatField(max_length=10)
    kverror6 = models.FloatField(max_length=10)
    kverror7 = models.FloatField(max_length=10)
    kverror8 = models.FloatField(max_length=10)

    kvdose1 = models.FloatField(max_length=10)
    kvdose2 = models.FloatField(max_length=10)
    kvdose3 = models.FloatField(max_length=10)
    kvdose4 = models.FloatField(max_length=10)
    kvdose5 = models.FloatField(max_length=10)
    kvdose6 = models.FloatField(max_length=10)
    kvdose7 = models.FloatField(max_length=10)
    kvdose8 = models.FloatField(max_length=10)

    kvdose_ma1 = models.FloatField(max_length=10)
    kvdose_ma2 = models.FloatField(max_length=10)
    kvdose_ma3 = models.FloatField(max_length=10)
    kvdose_ma4 = models.FloatField(max_length=10)
    kvdose_ma5 = models.FloatField(max_length=10)
    kvdose_ma6 = models.FloatField(max_length=10)
    kvdose_ma7 = models.FloatField(max_length=10)
    kvdose_ma8 = models.FloatField(max_length=10)
    
    ms_set1 = models.FloatField(max_length=10)
    ms_set2 = models.FloatField(max_length=10)
    ms_set3 = models.FloatField(max_length=10)
    ms_set4 = models.FloatField(max_length=10)
    ms_set5 = models.FloatField(max_length=10)

    ms_msr1 = models.FloatField(max_length=10)
    ms_msr2 = models.FloatField(max_length=10)
    ms_msr3 = models.FloatField(max_length=10)
    ms_msr4 = models.FloatField(max_length=10)
    ms_msr5 = models.FloatField(max_length=10)
    
    mserror1 = models.FloatField(max_length=10)
    mserror2 = models.FloatField(max_length=10)
    mserror3 = models.FloatField(max_length=10)
    mserror4 = models.FloatField(max_length=10)
    mserror5 = models.FloatField(max_length=10)

    msdose1 = models.FloatField(max_length=10)
    msdose2 = models.FloatField(max_length=10)
    msdose3 = models.FloatField(max_length=10)
    msdose4 = models.FloatField(max_length=10)
    msdose5 = models.FloatField(max_length=10)

    msdose_ma1 = models.FloatField(max_length=10)
    msdose_ma2 = models.FloatField(max_length=10)
    msdose_ma3 = models.FloatField(max_length=10)
    msdose_ma4 = models.FloatField(max_length=10)
    msdose_ma5 = models.FloatField(max_length=10)
    
    lin_ma1 = models.FloatField(max_length=10)
    lin_ma2 = models.FloatField(max_length=10)
    lin_ma3 = models.FloatField(max_length=10)
    lin_ma4 = models.FloatField(max_length=10)
    lin_ma5 = models.FloatField(max_length=10)

    lin_kv1 = models.FloatField(max_length=10)
    lin_kv2 = models.FloatField(max_length=10)
    lin_kv3 = models.FloatField(max_length=10)
    lin_kv4 = models.FloatField(max_length=10)
    lin_kv5 = models.FloatField(max_length=10)

    lin_dose1 = models.FloatField(max_length=10)
    lin_dose2 = models.FloatField(max_length=10)
    lin_dose3 = models.FloatField(max_length=10)
    lin_dose4 = models.FloatField(max_length=10)
    lin_dose5 = models.FloatField(max_length=10)

    lin_dosema1 = models.FloatField(max_length=10)
    lin_dosema2 = models.FloatField(max_length=10)
    lin_dosema3 = models.FloatField(max_length=10)
    lin_dosema4 = models.FloatField(max_length=10)
    lin_dosema5 = models.FloatField(max_length=10)

    lin_cl1 = models.FloatField(max_length=10)
    lin_cl2 = models.FloatField(max_length=10)
    lin_cl3 = models.FloatField(max_length=10)
    lin_cl4 = models.FloatField(max_length=10)
    lin_cl5 = models.FloatField(max_length=10)

    rep_kv_avg = models.FloatField(max_length=10)
    rep_s_avg = models.FloatField(max_length=10)
    rep_dose_avg = models.FloatField(max_length=10)

    rep_kv_std = models.FloatField(max_length=10)
    rep_s_std = models.FloatField(max_length=10)
    rep_dose_std = models.FloatField(max_length=10)

    rep_kv_cv = models.FloatField(max_length=10)
    rep_s_cv = models.FloatField(max_length=10)
    rep_dose_cv = models.FloatField(max_length=10)
    
    al70_ls = models.FloatField(max_length=10)
    al80_ls = models.FloatField(max_length=10)

    al70_pr = models.FloatField(max_length=10)
    al80_pr = models.FloatField(max_length=10)

    tb_leak_kvset = models.FloatField(max_length=10)
    tb_leak_kvmax = models.FloatField(max_length=10)
    tb_leak_maset = models.FloatField(max_length=10)
    tb_leak_tset = models.FloatField(max_length=10)
    tb_leak_mcont = models.FloatField(max_length=10)

    tb_leak_r = models.FloatField(max_length=10)
    tb_leak_f = models.FloatField(max_length=10)
    tb_leak_l = models.FloatField(max_length=10)
    tb_leak_u = models.FloatField(max_length=10)
    tb_leak_bh = models.FloatField(max_length=10)

    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)


    def clean(self):
        if self.is_passed and self.is_failed:
            raise ValidationError('You can only select one')
        super().clean()
    
# PEMELIHARAAN PREVENTIF
class Maintenance(models.Model):
    ANN = 'ANNUAL'
    SEMI = 'SEMI-ANNUAL'
    WEEK = 'WEEKLY'
    MON = 'MONTHLY'

    OK = 'BAIK'
    BAD = 'TIDAK BAIK'
    PART = 'PENGGANTIAN PART'
    SVC = 'PERBAIKAN'
    ADJ = 'ADJUSTMENT'
    STR = 'PENGUATAN'
    CLN = 'PEMBERSIHAN'
    LBC = 'LUBRIKASI'

    CHOICES = (
        (ANN, 'Annual'),
        (SEMI, 'Semi-annual'),
        (WEEK, 'Weekly'),
        (MON, 'Monthly'),
    )

    COND = (
        (OK, 'Baik'),
        (BAD, 'Tidak baik'),
        (PART, 'Penggantian part'),
        (SVC, 'Perbaikan'),
        (ADJ, 'Adjustment'),
        (STR, 'Penguatan'),
        (CLN, 'Pembersihan'),
        (LBC, 'Lubrikasi'),
    )

    # GENERAL INFO
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    period = models.CharField(max_length=100, choices=CHOICES, default=WEEK)
    location = models.CharField(max_length=150)
    hospital_unit = models.CharField(max_length=150)

    # X-RAY INFO
    xray_brand = models.CharField(max_length=150)
    xray_type = models.CharField(max_length=150)
    xray_serial = models.CharField(max_length=150)

    # PHYSICAL CONDITION
    ctrl_panel_cond = models.CharField(max_length=100, choices=COND, default=OK)
    cmd_arm_cond = models.CharField(max_length=100, choices=COND, default=OK)
    bucky_tbl_cond = models.CharField(max_length=100, choices=COND, default=OK)
    bucky_std_cond = models.CharField(max_length=100, choices=COND, default=OK)
    tube_std_cond = models.CharField(max_length=100, choices=COND, default=OK)
    generator_cond = models.CharField(max_length=100, choices=COND, default=OK)
    tube_spt_cond = models.CharField(max_length=100, choices=COND, default=OK)
    el_cable_cond = models.CharField(max_length=100, choices=COND, default=OK)
    htt_cable_cond = models.CharField(max_length=100, choices=COND, default=OK)
    psu_cond = models.CharField(max_length=100, choices=COND, default=OK)
    cable_cond = models.CharField(max_length=100, choices=COND, default=OK)
    sw_cond = models.CharField(max_length=100, choices=COND, default=OK)
    ind_lamp_cond = models.CharField(max_length=100, choices=COND, default=OK)
    col_lamp_cond = models.CharField(max_length=100, choices=COND, default=OK)
    sel_cond = models.CharField(max_length=100, choices=COND, default=OK)
    tube_lock_cond = models.CharField(max_length=100, choices=COND, default=OK)
    panel_ctl_cond = models.CharField(max_length=100, choices=COND, default=OK)
    buck_lock_cond = models.CharField(max_length=100, choices=COND, default=OK)

    kvp_std = models.FloatField(max_length=10)
    kvp_tol = models.FloatField(max_length=10)
    kvp_set = models.FloatField(max_length=10)
    kvp_output = models.FloatField(max_length=10)
    kvp_ok = models.BooleanField('Baik', default=False)
    kvp_not = models.BooleanField('Tidak Baik', default=False)

    ma_std = models.FloatField(max_length=10)
    ma_tol = models.FloatField(max_length=10)
    ma_set = models.FloatField(max_length=10)
    ma_output = models.FloatField(max_length=10)
    ma_ok = models.BooleanField('Baik', default=False)
    ma_not = models.BooleanField('Tidak Baik', default=False)

    ln_ma_std = models.FloatField(max_length=10)
    ln_ma_tol = models.FloatField(max_length=10)
    ln_ma_set = models.FloatField(max_length=10)
    ln_ma_output = models.FloatField(max_length=10)
    ln_ma_ok = models.BooleanField('Baik', default=False)
    ln_ma_not = models.BooleanField('Tidak Baik', default=False)

    expose_std = models.FloatField(max_length=10)
    expose_tol = models.FloatField(max_length=10)
    expose_set = models.FloatField(max_length=10)
    expose_output = models.FloatField(max_length=10)
    exp_ok = models.BooleanField('Baik', default=False)
    exp_not = models.BooleanField('Tidak Baik', default=False)

    rad_area_std = models.FloatField(max_length=10)
    rad_area_tol = models.FloatField(max_length=10)
    rad_area_set = models.FloatField(max_length=10)
    rad_area_output = models.FloatField(max_length=10)
    rad_area_ok = models.BooleanField('Baik', default=False)
    rad_area_not = models.BooleanField('Tidak Baik', default=False)

    exp_in_std = models.FloatField(max_length=10)
    exp_in_tol = models.FloatField(max_length=10)
    exp_in_set = models.FloatField(max_length=10)
    exp_in_output = models.FloatField(max_length=10)
    exp_in_ok = models.BooleanField('Baik', default=False)
    exp_in_not = models.BooleanField('Tidak Baik', default=False)

    amp_leak_std = models.FloatField(max_length=10)
    amp_leak_tol = models.FloatField(max_length=10)
    amp_leak_set = models.FloatField(max_length=10)
    amp_leak_output = models.FloatField(max_length=10)
    amp_leak_ok = models.BooleanField('Baik', default=False)
    amp_leak_not = models.BooleanField('Tidak Baik', default=False)

    cbl_gnd_std = models.FloatField(max_length=10)
    cbl_gnd_tol = models.FloatField(max_length=10)
    cbl_gnd_set = models.FloatField(max_length=10)
    cbl_gnd_output = models.FloatField(max_length=10)
    cbl_gnd_ok = models.BooleanField('Baik', default=False)
    cbl_gnd_not = models.BooleanField('Tidak Baik', default=False)

    rad_leak_std = models.FloatField(max_length=10)
    rad_leak_tol = models.FloatField(max_length=10)
    rad_leak_set = models.FloatField(max_length=10)
    rad_leak_output = models.FloatField(max_length=10)    
    rad_leak_ok = models.BooleanField('Baik', default=False)
    rad_leak_not = models.BooleanField('Tidak Baik', default=False)

    is_passed = models.BooleanField('passed', default=False)
    is_failed = models.BooleanField('failed', default=False)   
    

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


    def clean(self):
        if self.is_completed and self.is_continue:
            raise ValidationError('You can only select one')
        super().clean()
    