from django.urls import path
from . import views

urlpatterns = [
    path("knigogid_books_list/", views.KnigoGidListView.as_view(), name="knigogid_list"),
    path("form_parser_knigogid/", views.KnigoGidFormView.as_view()),
]
