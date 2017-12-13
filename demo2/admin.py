from django.contrib import admin

from .models import FundInfo

# Register your models here.
class FundInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name', 'wave3', 'wave_evaluate3', 'risk3', 'risk_evaluate3', 'sharp3', 'sharp_evaluate3', 'return_rate', 'rank', 'update_time')

admin.site.register(FundInfo, FundInfoAdmin)
