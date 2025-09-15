from django.contrib import admin

from myapp.models import Flowers, Category,Tag

admin.site.register(Flowers)
admin.site.register(Category)
admin.site.register(Tag)
