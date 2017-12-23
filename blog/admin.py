from django.contrib import admin
from blog.models import Entry, Category
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    exclude = ['posted']
    #prepopulated_fields = {'slug': ('title',)}

    # def get_readonly_fields(self, request, obj=None):
    #     # we need to cast the readonly_fields to a list and append and then return that.
    #     tmp = list(self.readonly_fields)
    #     tmp.append('slug')
    #     return tmp

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posted']
# Regisger the models to the admin
admin.site.register(Entry,EntryAdmin)
admin.site.register(Category, CategoryAdmin)
