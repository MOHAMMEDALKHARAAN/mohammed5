from django.contrib import admin
from .models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'phone', 'updated_at')
    search_fields = ('site_name', 'contact_email', 'phone')
    list_per_page = 20
