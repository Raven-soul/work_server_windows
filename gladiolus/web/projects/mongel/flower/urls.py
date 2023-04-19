from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),

    path('login_user/', login, name='login'),
    path('buket/', buket, name='buket'),
    path('basket/', basket, name='basket'),

    path('about/', about_info, name='about_info'),
    path('payment/', payment_info, name='payment_info'),
    path('guarantees/', guarantees_info, name='guarantees_info'),
    path('return/', return_info, name='return_info'),
    path('corporation/', corporation_info, name='corporation_info'),
    path('contacts/', contacts_info, name='contacts_info'),
    path('help/', help_info, name='help_info'),
    path('category/<int:cat_id>', show_category, name='category'),
    path('occasion/<int:occ_id>', show_occasion, name='occasion'),
    path('season/<int:sea_id>', show_season, name='season'),
    path('type/<int:typ_id>', show_type, name='type'),
]