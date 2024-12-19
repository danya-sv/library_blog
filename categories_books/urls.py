from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name="all_books"),
    path('books_for_children/', views.BooksForChildrenView.as_view(), name="books_for_children"),
    path('books_for_adolescents/', views.BooksForAdolescentsView.as_view(), name="books_for_adolescents"),
    path('books_for_young_adults/', views.BooksForYoungAdultsView.as_view(), name="books_for_young_adults"),
    path('books_for_pensioners/', views.BooksForPensionersView.as_view(), name="books_for_pensioners")
]
