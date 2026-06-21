from django.contrib import admin
from .models import Product, Order, RefundRequest



class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "in_stock")
    # search_fields = ("name", "category")
    # list_filter = ("category", "in_stock")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product_name", "amount", "status", "carrier", "tracking_number")
    # search_fields = ("user__username", "product_name")
    # list_filter = ("status", "created_at")


class RefundRequestAdmin(admin.ModelAdmin):
    list_display = ("order", "user", "reason", "status", "created_at")
    # search_fields = ("order__id", "user__username")
    # list_filter = ("status", "created_at")


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RefundRequest, RefundRequestAdmin)
