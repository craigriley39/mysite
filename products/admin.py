from django.contrib import admin
from .models import Product
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    exclude = ['created','id']


    def get_readonly_fields(self, request, obj=None):
        # we need to cast the readonly_fields to a list and append and then return that.
        tmp = list(self.readonly_fields)
        tmp.append('product_id')
        return tmp



admin.site.register(Product,ProductAdmin)