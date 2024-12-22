from django.shortcuts import get_object_or_404, redirect 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import BookModel
from .forms import ReviewForm
import datetime

class BookListView(ListView):
    model = BookModel
    template_name = "book.html"
    context_object_name = "book_list"
    queryset = BookModel.objects.all().order_by("-id")

class BookDetailView(DetailView):
    model = BookModel
    template_name = "book_detail.html"
    context_object_name = "book_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['reviews'] = book.reviews.all()
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', pk=book.pk)
        context = self.get_context_data()
        context['review_form'] = form
        return self.render_to_response(context)

class AboutView(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse("Привет, меня зовут Даня, мне 17 лет!")

class AboutPetView(TemplateView):
    template_name = "about_pet.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse("У меня есть собака по кличке Нора. Ее порода - Малинуа")

class SystemTimeView(TemplateView):
    template_name = "system_time.html"

    def get(self, request, *args, **kwargs):
        current_time = datetime.now()
        return HttpResponse(f"Текущее время: {current_time}")

