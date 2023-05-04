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
    list_display = ('id', 'title', 'price', 'currency', 'categ', 'photo', 'time_create', 'count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description_content')

class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'order')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_user_field', 'email_user_field', 'password_user_field')
    list_display_links = ('id', 'name_user_field')
    search_fields = ('id', 'name_user_field')

class SelectedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'user', 'product', 'time_create')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('id', 'user')

class PurchasedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'user', 'product', 'time_create')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('id', 'user')

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
admin.site.register(SelectedProducts, SelectedProductsAdmin)
admin.site.register(purchasedProducts, PurchasedProductsAdmin)