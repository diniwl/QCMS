from django.urls import path
from . import views

urlpatterns = [
    #AUTH
    path('', views.index, name='index'),
    path('login/', views.view_login, name='view_login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('homefismed', views.homefismed, name='homefismed'),


    path('<int:id>', views.view_schedule, name='view_schedule'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
