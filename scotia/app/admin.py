from django.contrib import admin

# Register your models here.
from .models import Provider, Product, Customer, Point, Stock, Order

admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Point)
admin.site.register(Stock)
admin.site.register(Order)
