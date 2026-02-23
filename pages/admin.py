# pages/admin.py
from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "subject")
    ordering = ("-created_at",)
