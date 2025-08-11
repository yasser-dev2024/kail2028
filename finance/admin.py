from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'status', 'issue_date', 'due_date', 'total_amount')
    list_filter = ('status',)
    search_fields = ('invoice_number',)
