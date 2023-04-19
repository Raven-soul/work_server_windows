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
            'userLoginUrl_name': 'login',
            'basketUrl_name': 'basket',
            'product_category': self.category,
            'product_occasion': self.occasion,
            'product_season': self.season,
            'product_type': self.type,
            'cat_selected': {'section': 0, 'order': 0}
        }

    def startBuilder(self):
        self.category = Category.objects.all()
        self.occasion = Occasion.objects.all()
        self.season = Season.objects.all()
        self.type = Type.objects.all()

        self.topPageLinks = [{'title':'О нас', 'url_name':'about_info'},
                        {'title':'Оплата', 'url_name':'payment_info'},
                        {'title':'Гарантии', 'url_name':'guarantees_info'},
                        {'title':'Возврат', 'url_name':'return_info'},
                        {'title':'Корп. клиентам', 'url_name':'corporation_info'},
                        {'title':'Контакты', 'url_name':'contacts_info'},
                        {'title':'Помощь', 'url_name':'help_info'}
                        ]

    def setData(self, name='title', value='Гладиолус, магазин доставки цветов'):
        self.context[name] = value
    
    def getData(self):
        return self.context
    

class Footer(object):
    def __init__(self):
        first_column = [{'title':'О нас', 'url_name':'about_info'},
                        {'title':'Оплата', 'url_name':'payment_info'},
                        {'title':'Гарантии', 'url_name':'guarantees_info'},
                        {'title':'Возврат', 'url_name':'return_info'},
                        {'title':'Корп. клиентам', 'url_name':'corporation_info'}]
        
        second_column = [{'title':'Контакты', 'url_name':'contacts_info'},
                        {'title':'Помощь', 'url_name':'help_info'}]
        
        third_column = [{'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'}]

        columnLinks = [{'column_title':'О нас', 'column_links': first_column},
                       {'column_title':'Клиентам', 'column_links': second_column},
                       {'column_title':'Популярное', 'column_links': third_column}
                        ]
        
        script_list = []

        self.context = {
            'columnLinks': columnLinks,
            'script_list': script_list
        }

    def setData(self, name='name', value='data'):
        self.context[name] = value
    
    def getData(self):
        return self.context