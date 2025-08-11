from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'time')
    list_filter = ('type', 'date')
