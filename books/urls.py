from django.urls import path
from books import views

urlpatterns = [
    path("library", views.index),
    path("books", views.books),
]