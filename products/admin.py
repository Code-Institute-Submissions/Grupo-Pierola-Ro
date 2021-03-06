from django.contrib import admin
from .models import color, grape_variety, region, size, product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'price',
        'region',
        'rating'
    )
    ordering = ('name',)
    readonly_fields = ('total_quantity_sold',)


admin.site.register(color)
admin.site.register(grape_variety)
admin.site.register(region)
admin.site.register(size)
admin.site.register(product, ProductAdmin)
