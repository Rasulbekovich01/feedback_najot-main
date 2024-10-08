from django.contrib import admin
from .models import Product
from django.utils.translation import gettext_lazy as _

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (),
        }),
    )
