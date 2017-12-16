from django.contrib import admin
from blog.models import Entry, Category
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Regisger the models to the admin
admin.site.register(Entry,EntryAdmin)
admin.site.register(Category, CategoryAdmin)
