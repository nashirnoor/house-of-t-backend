from unfold.admin import ModelAdmin as UnfoldModelAdmin
from django.contrib import admin
from .models import Product


admin.site.register(Product, UnfoldModelAdmin)
