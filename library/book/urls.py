from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_list, name="books_list"),

    path(
        "<int:id>/",
        views.book_detail,
        name="book_detail"
    ),

    path(
        "user/<int:user_id>/",
        views.user_books,
        name="user_books"
    ),
]
