from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('about_pet/', views.about_pet, name='about_pet'),
    path('system_time/', views.system_time, name='system_time'),
]
