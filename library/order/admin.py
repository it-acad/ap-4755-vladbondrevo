# Register your models here.
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "book",
        "created_at",
        "end_at",
        "plated_end_at",
    )
