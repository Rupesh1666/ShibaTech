# admin.py
from django.contrib import admin
from .models import CustomUser
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CustomUser)
