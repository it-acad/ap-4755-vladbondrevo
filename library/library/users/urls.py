from django.urls import path
from .views import users_list_view, user_detail_view

urlpatterns = [
    path('', users_list_view, name='users_list'),
    path('<int:user_id>/', user_detail_view, name='user_detail'),
]