from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list_view, name="book"),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about/', views.about, name='about'),
    path('about_pet/', views.about_pet, name='about_pet'),
    path('system_time/', views.system_time, name='system_time'),

    
]
