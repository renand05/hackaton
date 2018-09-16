from django.contrib import admin

# Register your models here.
from .models import Provider, Product, Customer, Point, Stock, Order

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiration_date')
    search_fields = ('name', 'expiration_date')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'price', 'points', 'ratio', 'active', 'expiration_date')
    list_filter = ('provider',)
    search_fields = ('name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('email',)

class PointAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quantity', 'expiration_date')
    list_filter = ('customer',)

class StockAdmin (admin.ModelAdmin):
    list_display = ('product', 'quantity')
    list_filter = ('product',)

class OrderAdmin (admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'status')
    list_filter = ('customer',)
    search_fields = ('customer',)


admin.site.site_header = 'Providers System'
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Order, OrderAdmin)
