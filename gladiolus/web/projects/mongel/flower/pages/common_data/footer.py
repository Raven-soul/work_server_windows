from ...models import * #база данных
from django.shortcuts import render, redirect
from ..info_pages_data.info_pages_set import *

class Footer(object):
    def __init__(self):
        self.startBuilder()
        

        self.context = {
            'columnLinks': self.columnLinks,
            'script_list': self.script_list
        }

    def startBuilder(self):
        self.first_column = self.dictReady(InfoDataSet().getContext(), value = '0')
        self.second_column = self.dictReady(InfoDataSet().getContext(), value = '1')
        
        self.third_column = [{'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'},
                        {'title':'Цветы', 'url_name':'home'}]

        self.columnLinks = [{'column_title':'О нас', 'column_links': self.first_column},
                       {'column_title':'Клиентам', 'column_links': self.second_column},
                       {'column_title':'Популярное', 'column_links': self.third_column}
                        ]
        
        self.script_list = []

    def setData(self, name='name', value='data'):
        self.context[name] = value
    
    def getData(self):
        return self.context
    
    def dictReady(data, name='order', value='0'):
        print(data[0])
        # result = {}
        # for item in data: 
        #     if item[name] == value:
        #         result.update(item)
        # return result