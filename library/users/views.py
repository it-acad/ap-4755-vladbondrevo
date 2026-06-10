from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


def users_list_view(request):

    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')


    users = User.objects.all()


    return render(request, 'users/users_list.html', {'users': users})


def user_detail_view(request, user_id):

    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')


    target_user = get_object_or_404(User, id=user_id)

    return render(request, 'users/user_detail.html', {'target_user': target_user})