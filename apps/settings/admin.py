from django.contrib import admin
from apps.settings.models import Settings
# Register your models here.


@admin.register(Settings)
class SettingAdmin(admin.ModelAdmin):
    list_display= ('title', 'description')

