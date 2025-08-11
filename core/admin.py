from django.contrib import admin
from .models import SiteSetting

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'updated_at')
