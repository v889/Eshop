from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.db.models.functions import Lower
from .modelinline import *

class CategoryView(admin.ModelAdmin):
    list_display =[
        'name',
    ]

admin.site.register(Category,CategoryView)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(ProductImage)

# Register your models here.

@admin.register(Product)
class JobAdmin(admin.ModelAdmin):
    list_display = ["name", 'price','category']
    inlines = [ProductImageInline]


    search_fields = ('name','price')

