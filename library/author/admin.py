# Register your models here.
from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "surname",
        "patronymic",
    )

    fieldsets = (
        (
            "Author information",
            {
                "fields": (
                    "name",
                    "surname",
                    "patronymic",
                )
            }
        ),
    )
