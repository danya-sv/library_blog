from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name="all_books"),
    path('books_for_children/', views.books_for_children, name="books_for_children"),
    path('books_for_adolescents/', views.books_for_adolescents, name="books_for_adolescents"),
    path('books_for_young_adults/', views.books_for_young_adults, name="books_for_young_adults"),
    path('books_for_pensioners/', views.books_for_pensioners, name="books_for_pensioners")

]