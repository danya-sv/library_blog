from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from django.views.generic import ListView
from .models import Book




class AllBooksView(ListView):
    model = Book
    template_name = "tags/all_books.html"
    context_object_name = "books"
    queryset = Book.objects.all().order_by("-id")


class BooksForChildrenView(ListView):
    model = Book
    template_name = "tags/books_for_children.html"
    context_object_name = "books_child"
    queryset = Book.objects.filter(tags__name="Книги для детей").order_by("-id")


class BooksForAdolescentsView(ListView):
    model = Book
    template_name = "tags/books_for_adolescents.html"
    context_object_name = "books_adolescents"
    queryset = Book.objects.filter(tags__name="Книги для подростков").order_by("-id")


class BooksForYoungAdultsView(ListView):
    model = Book
    template_name = "tags/books_for_young_adults.html"
    context_object_name = "books_young_adults"
    queryset = Book.objects.filter(tags__name="Книги для молодежи").order_by("-id")


class BooksForPensionersView(ListView):
    model = Book
    template_name = "tags/books_for_pensioners.html"
    context_object_name = "books_pensioners"
    queryset = Book.objects.filter(tags__name="Книги для пенсионеров").order_by("-id")
