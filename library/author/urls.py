from django.urls import path
from .views import authors_list_view, author_create_view, author_delete_view

urlpatterns = [
    path('', authors_list_view, name='authors_list'),
    path('create/', author_create_view, name='author_create'),
    path('<int:author_id>/delete/', author_delete_view, name='author_delete'),
]