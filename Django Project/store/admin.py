from django.contrib import admin

from store.models import Product, Category

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'is_available')
    # list_display_links = ('name', 'price', 'quantity')
    list_editable = ('price', 'quantity', 'is_available')
    # list_filter = ('is_available',)
    search_fields = ('name', 'description')
    # readonly_fields = ('quantity', )