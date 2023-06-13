"""
WSGI config for mongel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
#
#  wsgi.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongel.settings')

application = get_wsgi_application()
