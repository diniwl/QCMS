from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #AUTH
    path('', views.index, name='index'),
    path('login/', views.view_login, name='view_login'),
    path('register', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    
    #SCHEDULE
    path('home', views.home, name='home'),
    path('homefismed', views.homefismed, name='homefismed'),
    path('<int:id>', views.view_schedule, name='view_schedule'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    #UJI PENERIMAAN
    path('home_penerimaan', views.home_penerimaan, name='home_penerimaan'),
    path('<int:id>', views.view_penerimaan, name='view_penerimaan'),
    path('add_penerimaan/', views.add_penerimaan, name='add_penerimaan'),
    path('edit_penerimaan/<int:id>/', views.edit_penerimaan, name='edit_penerimaan'),
    path('delete_penerimaan/<int:id>/', views.delete_penerimaan, name='delete_penerimaan'),
    
    #KALIBRASI
    path('home_kalibrasi', views.home_kalibrasi, name='home_kalibrasi'),
    path('<int:id>', views.view_kalibrasi, name='view_kalibrasi'),
    path('add_kalibrasi/', views.add_kalibrasi, name='add_kalibrasi'),
    path('edit_kalibrasi/<int:id>/', views.edit_kalibrasi, name='edit_kalibrasi'),
    path('delete_kalibrasi/<int:id>/', views.delete_kalibrasi, name='delete_kalibrasi'),

    #SERTIF KALIBRASI
    path('home_sertifkalibrasi/', views.home_sertifkalibrasi, name='home_sertifkalibrasi'),
    path('sertif_kalibrasi/', views.sertif_kalibrasi, name='sertif_kalibrasi'),
    path('view_sertifkalibrasi/<int:id>/', views.view_sertifkalibrasi, name='view_sertifkalibrasi'),

    #UKES
    path('home_ukes', views.home_ukes, name='home_ukes'),
    path('<int:id>', views.view_ukes, name='view_ukes'),
    path('add_ukes/', views.add_ukes, name='add_ukes'),
    path('edit_ukes/<int:id>/', views.edit_ukes, name='edit_ukes'),
    path('delete_ukes/<int:id>/', views.delete_ukes, name='delete_ukes'),

    #SERVICE REPORT
    path('home_service', views.home_service, name='home_service'),
    path('<int:id>', views.view_service, name='view_service'),
    path('add_service/', views.add_service, name='add_service'),
    path('edit_service/<int:id>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),

    
]

urlpatterns += staticfiles_urlpatterns()
