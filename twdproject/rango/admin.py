from django.contrib import admin
from rango.models import Category, Page

# Note the typo within the admin interface
# (categorys, not categories). This problem
# can be fixed by adding a nested Meta class
# into your model definitions with the
# verbose_name_plural attribute. Check out
# Django official documentation on models
# for more information.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
