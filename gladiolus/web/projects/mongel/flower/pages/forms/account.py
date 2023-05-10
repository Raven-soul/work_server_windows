from ...models import * #база данных
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class Account_page(object):
    def __init__(self, request, section_name):
        self.startBuilder(request)
        
        if section_name == 'user':
            self.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
            self.header.setData(value = 'Аккаунт пользователя')
            
            
            self.context = {
                'header': self.header.getData(),
                'footer': self.footer.getData(),
                'form': '',
                'action_page': 'home',
                'button_submit': 'Сохранить',
                'page_selected': 0,
                'user_page_links': [{'pk': 0, 'data': 'Данные пользователя', 'path': 'home'},
                                    {'pk': 1, 'data': 'Заказы', 'path': 'home'}]
                                    }
        elif section_name == 'order':
            self.header.setData(name = 'content_style_path', value = 'flower/css/user_account_pages.css')
            self.header.setData(value = 'Данные заказов')
            
            
            self.context = {
                'header': self.header.getData(),
                'footer': self.footer.getData(),
                
                'page_selected': 1,
                'user_page_links': [{'pk': 0, 'data': 'Данные пользователя', 'path': 'home'},
                                    {'pk': 1, 'data': 'Заказы', 'path': 'home'}]
                                    }

    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()

    def getDict(self):
        return self.context