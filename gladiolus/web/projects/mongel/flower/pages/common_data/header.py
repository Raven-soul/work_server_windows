from ...models import * #база данных
from django.shortcuts import render, redirect

class Header(object):
    def __init__(self):
        self.startBuilder()

        self.context = {
            'title': 'Гладиолус, магазин доставки цветов',
            'content_style_path': 'flower/css/content/main_content.css',
            'onload_function':'',
            'topLinks': self.topPageLinks,
            'userLoginUrl_name': self.accountPages['log'].get_absolute_url,
            'basketUrl_name': 'basket',
            'product_category': self.category,
            'product_occasion': self.occasion,
            'product_season': self.season,
            'product_type': self.type,
            'cat_selected': {'section': -1, 'order': 0}
        }

    def startBuilder(self):
        self.category = Category.objects.all()
        self.occasion = Occasion.objects.all()
        self.season = Season.objects.all()
        self.type = Type.objects.all()

        self.topPageLinks = InfoPages.objects.all()
        self.accountPages = { 'reg': UserPages.objects.filter(alter_name = 'registration')[0],
                              'log': UserPages.objects.filter(alter_name = 'login')[0],
                              'us_data': UserPages.objects.filter(alter_name = 'user')[0],
                              'ord_data': UserPages.objects.filter(alter_name = 'order')[0],
                            }

    def setData(self, name='title', value='Гладиолус, магазин доставки цветов'):
        self.context[name] = value
    
    def getData(self):
        return self.context