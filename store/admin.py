from django.contrib import admin
from .models import *

class ProductView(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'category',
        'image',
    ]
class CategoryView(admin.ModelAdmin):
    list_display =[
        'name',
    ]
admin.site.register(Product,ProductView)
admin.site.register(Category,CategoryView)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Status)

# Register your models here.
