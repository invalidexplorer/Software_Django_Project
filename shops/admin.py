from django.contrib import admin
from .models import Category, Product, Review,ProductReport


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at','no_of_views']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name','text','product','rating']

class ProductReportAdmin(admin.ModelAdmin):
    list_display = ['reason','product']

admin.site.register(Product, ProductAdmin)

admin.site.register(Review,ReviewsAdmin)


admin.site.register(ProductReport,ProductReportAdmin)