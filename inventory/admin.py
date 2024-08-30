from django.contrib import admin
from .models import Supplier, Product, PurchaseOrder, PurchaseOrderItem

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem

class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [PurchaseOrderItemInline]
    list_display = ('id', 'supplier', 'order_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'reorder_level', 'supplier')
    list_filter = ('supplier',)
    search_fields = ('name',)

admin.site.register(Supplier)
admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
