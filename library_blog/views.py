from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models
from .models import BookModel
from .forms import ReviewForm


def book_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            "book_id": book_id,
        }
        return render(request, template_name="book_detail.html", context=context)


def book_list_view(request):
    if request.method == "GET":
        book_list = models.BookModel.objects.all().order_by("-id")
        context = {
            "book_list": book_list,
        }
        return render(request, template_name="book.html", context=context)


def about(request):
    if request.method == "GET":
        return HttpResponse("Привет, меня зовут Даня, мне 17 лет!")


def about_pet(request):
    if request.method == "GET":
        return HttpResponse("У меня есть собака по кличке Нора. Ее порода - Малинуа")


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now()
        return HttpResponse(f"Текущее время: {current_time}")


def book_detail_view(request, id):
    book = get_object_or_404(BookModel, id=id)

    reviews = book.reviews.all()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect("book_detail", id=book.id)
    else:
        form = ReviewForm()

    context = {
        "book_id": book,
        "review_form": form,
        "reviews": reviews,
    }
    return render(request, "book_detail.html", context)
