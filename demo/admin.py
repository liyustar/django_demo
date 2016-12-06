from django.contrib import admin

from .models import Counter

# Register your models here.
class CounterAdmin(admin.ModelAdmin):
    list_display = ('text', 'count')

admin.site.register(Counter, CounterAdmin)
