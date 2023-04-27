from django.urls import path, re_path

from .views import *

urlpatterns = [
    # ----------------------- main pages -------------------------------
    path('', FlowerHome.as_view(), name='home'),
    path('product/<int:prod_id>', product_details, name='product'),
    path('basket/', basket, name='basket'),

    # ----------------------- main form pages -------------------------------
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),

    # ----------------------- information pages -------------------------------
    path('about/', about_info, name='about_info'),
    path('payment/', payment_info, name='payment_info'),
    path('guarantees/', guarantees_info, name='guarantees_info'),
    path('return/', return_info, name='return_info'),
    path('contacts/', contacts_info, name='contacts_info'),
    path('help/', help_info, name='help_info'),

    # ----------------------- main filter pages -------------------------------
    path('category/<int:cat_id>', show_category, name='category'),
    path('occasion/<int:occ_id>', show_occasion, name='occasion'),
    path('season/<int:sea_id>', show_season, name='season'),
    path('type/<int:typ_id>', show_type, name='type'),
]