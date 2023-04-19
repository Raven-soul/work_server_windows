from ...models import * #база данных
from django.shortcuts import render, redirect

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