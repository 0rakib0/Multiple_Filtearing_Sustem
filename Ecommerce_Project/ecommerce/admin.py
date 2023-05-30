from django.contrib import admin
from .models import Category, Brand, Seller, Warranty, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Seller)
admin.site.register(Warranty)
admin.site.register(Product)
