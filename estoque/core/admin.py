from django.contrib import admin
from .models import Product, Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'value', 'quantity', 'unit_value')

    def unit_value(self, Purchase):
        unit_price = Purchase.value / Purchase.quantity
        return round(unit_price, 2)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'average_coast')

admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
