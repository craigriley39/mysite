from django.contrib import admin
from .models import Customer,Order,Product
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    exclude = ['created','id']


    def get_readonly_fields(self, request, obj=None):
        # we need to cast the readonly_fields to a list and append and then return that.
        tmp = list(self.readonly_fields)
        tmp.append('customer_id')
        return tmp



class OrderAdmin(admin.ModelAdmin):
    exclude = ['created','id']


    def get_readonly_fields(self, request, obj=None):
        # we need to cast the readonly_fields to a list and append and then return that.
        tmp = list(self.readonly_fields)
        tmp.append('order_id')
        return tmp


class ProductAdmin(admin.ModelAdmin):
    exclude = ['created','id']


    def get_readonly_fields(self, request, obj=None):
        # we need to cast the readonly_fields to a list and append and then return that.
        tmp = list(self.readonly_fields)
        tmp.append('product_id')
        return tmp


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategorytAdmin)
