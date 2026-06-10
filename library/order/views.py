from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Order
from book.models import Book


def orders_list(request):
    """
    Show all orders (librarian).
    """
    orders = Order.objects.all()

    return render(
        request,
        "order/list.html",
        {"orders": orders}
    )


@login_required
def my_orders(request):
    """
    Show orders of current user.
    """
    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        "order/my_orders.html",
        {"orders": orders}
    )


def user_orders(request, user_id):
    """
    Show all books provided to a specific user (by id).
    """
    orders = Order.objects.filter(
        user_id=user_id
    )

    return render(
        request,
        "order/list.html",
        {"orders": orders}
    )


@login_required
def create_order(request, book_id):
    """
    Create new order.
    """
    if request.method == "POST":

        book = Book.get_by_id(book_id)

        if not book:
            return redirect("books_list")

        planned_date = (
            timezone.now() +
            timedelta(days=14)
        )

        Order.create(
            user=request.user,
            book=book,
            plated_end_at=planned_date
        )

        return redirect("my_orders")

    return redirect("books_list")


@login_required
def close_order(request, id):
    """
    Close order and return book.
    """
    order = Order.get_by_id(id)

    if order:
        order.update(
            end_at=timezone.now()
        )

        order.book.count += 1
        order.book.save()

    return redirect("orders_list")
