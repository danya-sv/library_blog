from django.shortcuts import render
from . import models

#все книги 
def all_books(request):
    if request.method == 'GET':
        books = models.Book.objects.all().order_by("-id")
        context = {'books': books}
        return render(request,
                      template_name="tags/all_books.html",
                      context=context
                      )
        
#книги для детей
def books_for_children(request):
    if request.method == 'GET':
        books_child = models.Book.objects.filter(tags__name="Книги для детей").order_by("-id")
        context = {'books_child': books_child}
        return render(
            request,
            template_name="tags/books_for_children.html",
            context=context
        )
        
#книги для подростков
def books_for_adolescents(request):
    if request.method == 'GET':
        books_adolescents = models.Book.objects.filter(tags__name="Книги для подростков").order_by("-id")
        context = {'books_adolescents': books_adolescents}
        return render(
            request,
            template_name="tags/books_for_adolescents.html",
            context=context
        )
            
#книги для молодежи

def books_for_young_adults(request):
    if request.method == 'GET':
        books_young_adults = models.Book.objects.filter(tags__name="Книги для молодежи").order_by("-id")
        context = {'books_young_adults': books_young_adults}
        return render(
            request,
            template_name="tags/books_for_young_adults.html",
            context=context
        )
        
#книги для пенсионеров

def books_for_pensioners(request):
    if request.method == 'GET':
        books_pensioners = models.Book.objects.filter(tags__name="Книги для пенсионеров").order_by("-id")
        context = {'books_pensioners': books_pensioners}
        return render(
            request,
            template_name="tags/books_for_pensioners.html",
            context=context
        )

    

