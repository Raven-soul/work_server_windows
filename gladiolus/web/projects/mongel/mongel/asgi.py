"""
ASGI config for mongel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
#
#  asgi.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongel.settings')

application = get_asgi_application()
