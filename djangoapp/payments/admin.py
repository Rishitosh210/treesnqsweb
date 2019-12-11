from django.contrib import admin

from payments.models import OrderItem, Order, Payment, Coupon, RefundRequest, BillingAddress


def accept_requested_refund(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


accept_requested_refund.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'order_created',
        'ordered_date',
        'received',
        'refund_requested',
        'refund_granted',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = [
        'ordered',
        'order_created',
        'ordered_date',
        'received',
        'refund_requested',
        'refund_granted'
    ]
    list_display_links = [
        'user',
        'billing_address',
        'payment',
        'coupon'
    ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [accept_requested_refund]


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount']


class RefundRequestAdmin(admin.ModelAdmin):
    list_display = ['order', 'reason', 'accepted']


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'street_address',
                    'apartment_address',
                    'countries',
                    'zip_code']
    list_filter = ['countries']
    search_fields = ['user',
                     'street_address',
                     'apartment_address',
                     'zip_code']


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(RefundRequest, RefundRequestAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
