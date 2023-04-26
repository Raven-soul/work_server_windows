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

class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'order')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Review)
admin.site.register(Composition)
admin.site.register(Wrapping)
admin.site.register(InfoPages, InfoPagesAdmin)
admin.site.register(InfoClass)
admin.site.register(User, UserAdmin)
admin.site.register(Register_form)