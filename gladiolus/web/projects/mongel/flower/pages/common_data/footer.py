from ...models import * #база данных
from django.shortcuts import render, redirect


class Footer(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'columnLinks': self.columnLinks,
            'script_list': self.script_list
        }

    def startBuilder(self):
        self.third_column = [{'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'}]

        self.columnLinks = [{'column_title':'О нас'},
                       {'column_title':'Клиентам'},
                       {'column_title':'Популярное', 'column_links': self.third_column}
                        ]
        
        self.script_list = []

    def setData(self, name='name', value='data'):
        self.context[name] = value
    
    def getData(self):
        return self.context