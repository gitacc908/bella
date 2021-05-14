from django.contrib import admin

from apps.order.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ('owner.', 'last_name')
    list_filter = ('is_paid', 'created')
    inlines = [OrderItemInline]
