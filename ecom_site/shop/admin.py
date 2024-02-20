from django.contrib import admin
from .models import Products,Order
admin.site.site_header="E-commerce Site"
admin.site.site_title="Ankit Shopping"
admin.site.index_title="Manage Ankit Shopping"
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description='Default Category'
    list_display=('title','price','discount_price','description','category')
    search_fields=('title','category')
    actions=('change_category_to_default',)
    fields=('title','price')
    list_editable=('price','discount_price','category')
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)