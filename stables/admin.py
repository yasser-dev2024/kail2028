from django.contrib import admin
from django.utils.html import format_html
from .models import Horse, NewsTicker

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'color', 'price_sar', 'location', 'contact_phone')
    search_fields = ('name', 'breed', 'color', 'location', 'contact_phone')
    list_filter = ('breed', 'color')
    fields = (
        'name', 'breed', 'birth_date', 'color', 'photo',
        'price', 'contact_phone', 'location', 'specs',
        'preview',
    )
    readonly_fields = ('preview',)

    def price_sar(self, obj):
        if obj.price is None:
            return '-'
        return f"﷼ {obj.price:,.0f}"
    price_sar.short_description = "السعر"
    price_sar.admin_order_field = 'price'

    def preview(self, obj):
        if obj and obj.photo:
            return format_html("<img src='{}' style='max-width:240px;border-radius:8px;' />", obj.photo.url)
        return "—"
    preview.short_description = "Preview"

@admin.register(NewsTicker)
class NewsTickerAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('text',)
    ordering = ('-updated_at',)

    def short_text(self, obj):
        t = (obj.text or '').strip().replace('\n', ' ')
        return (t[:60] + '…') if len(t) > 60 else t
    short_text.short_description = "النص"
