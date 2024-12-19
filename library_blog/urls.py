from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book"),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about_pet/', views.AboutPetView.as_view(), name='about_pet'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
]
