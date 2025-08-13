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
        amount = f"{obj.price:,.0f}"
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            'width="14" height="14" fill="currentColor" '
            'style="vertical-align:-2px;margin-inline-end:4px;display:inline-block">'
            '<rect x="7.5" y="1.8" width="3" height="20.4" rx="1.2"/>'
            '<rect x="13.5" y="1.8" width="3" height="20.4" rx="1.2"/>'
            '<rect x="3" y="6" width="18" height="2.2" rx="1" transform="rotate(-10 12 7.1)"/>'
            '<rect x="3" y="11.5" width="18" height="2.2" rx="1" transform="rotate(-10 12 12.6)"/>'
            '<rect x="3" y="17" width="18" height="2.2" rx="1" transform="rotate(-10 12 18.1)"/>'
            '</svg>'
        )
        return format_html('{}{}', svg, amount)
    price_sar.short_description = "السعر"
    price_sar.admin_order_field = 'price'

    def preview(self, obj):
        if obj and getattr(obj, "photo", None):
            return format_html(
                "<img src='{}' style='max-width:240px; height:auto;'/>",
                obj.photo.url
            )
        return "-"
    preview.short_description = "المعاينة"
