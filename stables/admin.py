from django.contrib import admin
from .models import Horse
from django.utils.html import format_html

@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'birth_date', 'color', 'photo_preview')
    search_fields = ('name', 'breed', 'color')
    readonly_fields = ('photo_preview',)

    fieldsets = (
        (None, {
            'fields': ('name', 'breed', 'birth_date', 'color', 'photo', 'photo_preview')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:60px;border-radius:6px" />', obj.photo.url)
        return '—'
    photo_preview.short_description = 'Preview'
