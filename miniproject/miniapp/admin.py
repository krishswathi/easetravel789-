from django.contrib import admin
from .models import BusCard

@admin.register(BusCard)
class BusCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'balance', 'issued_date', 'expiry_date')
    search_fields = ('user__username', 'card_number')
