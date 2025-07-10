from django.contrib import admin

from news.models import New, Category

admin.site.register(New)
admin.site.register(Category)