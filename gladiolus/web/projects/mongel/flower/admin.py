#
#  admin.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

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

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'description', 'product', 'author')
    list_display_links = ('id',)
    search_fields = ('grade', 'author', 'product',)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'order')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_user_field', 'sessionUNQid', 'email_user_field', 'password_user_field')
    list_display_links = ('id', 'name_user_field')
    search_fields = ('id', 'name_user_field')

class SelectedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'user', 'product', 'time_create')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('id', 'user')

class PurchasedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'user', 'product', 'status', 'time_create')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('id', 'user')

class LikedProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'time_create')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('id', 'user')

class UserPagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alter_name')
    list_display_links = ('id', 'name', 'alter_name')
    search_fields = ('id', 'alter_name')

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'code')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_phone', 'sender_user', 'sender_email', 'order_city', 'order_date', 'order_time')
    list_display_links = ('id', 'sender_phone', 'sender_user', 'sender_email', 'order_city')
    search_fields = ('id', 'sender_phone', 'sender_user', 'order_city')

class PaymentMethodSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Composition)
admin.site.register(Wrapping) #Cities
admin.site.register(Cities, CitiesAdmin)
admin.site.register(InfoPages, InfoPagesAdmin)
admin.site.register(InfoClass)
admin.site.register(User, UserAdmin)
admin.site.register(SelectedProducts, SelectedProductsAdmin)
admin.site.register(PurchasedProducts, PurchasedProductsAdmin)
admin.site.register(LikedProducts, LikedProductsAdmin)
admin.site.register(UserPages, UserPagesAdmin) 
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PaymentMethodSection, PaymentMethodSectionAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
