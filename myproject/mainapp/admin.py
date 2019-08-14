from django.contrib import admin
from .models import category,brand_for_category
# Register your models here.

admin.site.register(category)
admin.site.register(brand_for_category)
