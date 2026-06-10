from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser

def register_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        role = request.POST.get('role', 0)

        if not email or not password:
            error = "Будь ласка, заповніть усі обов'язкові поля."
        elif CustomUser.objects.filter(email=email).exists():
            error = "Користувач з таким Email вже існує."
        else:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=int(role)
            )
            login(request, user)
            return redirect('dashboard')

    return render(request, 'authentication/register.html', {'error': error})


def login_view(request):
    error = None
    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')

        user = authenticate(request, username=email_input, password=password_input)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Невірний Email або пароль."

    return render(request, 'authentication/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):

    return render(request, 'authentication/dashboard.html')