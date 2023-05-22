from ...models import * #база данных
from .authorisation import Authorization
from django.shortcuts import render, redirect

class Header(object):
    def __init__(self, request):
        self.startBuilder(request)

        if self.auth.isAuthorized():
            userLoginUrl_name = self.accountPages['us_data'].get_absolute_url
            if self.auth.getAuthorizedUser().city_user_field == None:
                User.objects.filter(pk = self.auth.getAuthorizedUser().pk).update(city_user_field=Cities.objects.get(pk=1))
            else:
                self.user_sity = self.auth.getAuthorizedUser().city_user_field
        else:
            userLoginUrl_name = self.accountPages['log'].get_absolute_url
            self.user_sity = Cities.objects.get(pk=1)

        self.context = {
            'title': 'Гладиолус, магазин доставки цветов',
            'content_style_path': 'flower/css/content/main.css',
            'user_sity': self.user_sity,
            'cities_list': self.getCities(),
            'header_functions':{
                'sity': 'setSity(this)'
            },
            'onload_function':'',
            'topLinks': self.topPageLinks,
            'userLoginUrl_name': userLoginUrl_name,
            'basketUrl_name': 'basket',
            'product_category': self.category,
            'product_occasion': self.occasion,
            'product_season': self.season,
            'product_type': self.type,
            'cat_selected': {'section': -1, 'order': 0},
            'script': 'flower/js/ajax/header.js'
        }

    def getCities(self):
        cities = []
        for elem in Cities.objects.all():
            cities.append({'name': elem.name, 'id': elem.pk})
        return cities

    def startBuilder(self, request):
        self.category = Category.objects.all()
        self.occasion = Occasion.objects.all()
        self.season = Season.objects.all()
        self.type = Type.objects.all()
        self.auth = Authorization(request)

        self.topPageLinks = InfoPages.objects.all()
        self.accountPages = { 'reg': UserPages.objects.get(alter_name = 'registration'),
                              'log': UserPages.objects.get(alter_name = 'login'),
                              'us_data': UserPages.objects.get(alter_name = 'user'),
                              'ord_data': UserPages.objects.get(alter_name = 'order'),
                            }
        self.user_sity = ''

    def setData(self, name='title', value='Гладиолус, магазин доставки цветов'):
        self.context[name] = value
    
    def getData(self):
        return self.context