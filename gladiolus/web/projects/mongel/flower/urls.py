#
#  urls.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

from django.urls import path

from .views import *

urlpatterns = [
    # ----------------------- main pages -------------------------------
    path('', index, name='index'),
    path('home/', FlowerHome.as_view(), name='home'),
    path('product/<int:prod_id>', product_details, name='product'),
    path('basket/', basket, name='basket'),
    path('ordering/', ordering, name='ordering'),
    path('payment/', payment, name='payment'),

    # ----------------------- main form pages -------------------------------
    path('account/<str:section_name>', account, name='account'),
    path('review/<int:product_id>', review, name='review'),

    # ----------------------- information pages -------------------------------
    path('about/', about_info, name='about_info'),
    path('payment_info/', payment_info, name='payment_info'),
    path('guarantees/', guarantees_info, name='guarantees_info'),
    path('return/', return_info, name='return_info'),
    path('contacts/', contacts_info, name='contacts_info'),
    path('help/', help_info, name='help_info'),

    # ----------------------- main filter pages -------------------------------
    path('category/<int:cat_id>', FlowerShowCategory.as_view(), name='category'),
    path('occasion/<int:occ_id>', FlowerShowOccasion.as_view(), name='occasion'),
    path('season/<int:sea_id>', FlowerShowSeason.as_view(), name='season'),
    path('type/<int:typ_id>', FlowerShowType.as_view(), name='type'),

    # ----------------------- ajax pages- -------------------------------
    path('append/', append, name='append'),
    path('delete/', delete, name='delete'),
    path('accountLists/', accountLists, name='accountLists'),
    path('setReview/', setReview, name='setReview'),
    path('setSity/', setSity, name='setSity'),
    path('getSity/', getSity, name='getSity'),
    path('basketConfirm/', basketConfirm, name='basketConfirm'),
    path('pay/', pay, name='pay')
]