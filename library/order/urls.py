from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.orders_list,
        name="orders_list"
    ),

    path(
        "my/",
        views.my_orders,
        name="my_orders"
    ),

    path(
        "user/<int:user_id>/",
        views.user_orders,
        name="user_orders"
    ),

    path(
        "create/<int:book_id>/",
        views.create_order,
        name="create_order"
    ),

    path(
        "close/<int:id>/",
        views.close_order,
        name="close_order"
    ),
]
