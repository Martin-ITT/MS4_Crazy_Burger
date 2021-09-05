from django.contrib import admin
from .models import Product, Category, Allergen

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # adjust defualt columns to be displayed in admin page, must be also registered
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Allergen)
admin.site.register(Category, CategoryAdmin)
