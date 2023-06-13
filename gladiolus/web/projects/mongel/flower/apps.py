#
#  apps.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

from django.apps import AppConfig


class FlowerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flower'
    verbose_name = 'Товары'
