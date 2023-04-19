from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class OccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'currency', 'categ', 'photo', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description_content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Review)
admin.site.register(Composition)
admin.site.register(Wrapping)