# Register your models here.
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "count",
    )

    list_filter = (
        "authors",
    )

    search_fields = (
        "id",
        "name",
    )

    filter_horizontal = (
        "authors",
    )

    fieldsets = (
        (
            "Static information",
            {
                "fields": (
                    "name",
                    "authors",
                    "description",
                )
            },
        ),
        (
            "Dynamic information",
            {
                "fields": (
                    "count",
                )
            },
        ),
    )
