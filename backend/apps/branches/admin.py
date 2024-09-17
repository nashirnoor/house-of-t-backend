from unfold.admin import ModelAdmin as UnfoldModelAdmin
from django.contrib import admin
from .models import Branch, BranchProduct, ProductRequest


admin.site.register(Branch, UnfoldModelAdmin)
admin.site.register(BranchProduct, UnfoldModelAdmin)
admin.site.register(ProductRequest, UnfoldModelAdmin)
