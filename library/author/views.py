from django.shortcuts import render, redirect, get_object_or_404
from .models import Author



def authors_list_view(request):
    authors = Author.objects.all()
    return render(request, 'author/authors_list.html', {'authors': authors})



def author_create_view(request):
    # Перевірка прав (тільки адмін/бібліотекар)
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        if name:
            Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        return redirect('authors_list')

    return render(request, 'author/author_form.html')



def author_delete_view(request, author_id):
    # Перевірка прав
    if not request.user.is_authenticated or (
            not request.user.is_superuser and getattr(request.user, 'role', None) != 1):
        return redirect('login')

    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        # Перевірка: чи є у автора книжки? (використовуємо book_set - це стандартний Django related_name)
        if author.book_set.exists():
            # Тут можна додати вивід повідомлення про помилку, якщо хочеш
            return redirect('authors_list')

        author.delete()
        return redirect('authors_list')

    return render(request, 'author/author_confirm_delete.html', {'author': author})