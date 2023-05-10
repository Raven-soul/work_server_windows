from ...models import * #база данных
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class Account_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
        self.header.setData(value = 'Аккаунт пользователя')
        
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'form': '',
            'action_page': 'account',
            'button_submit': 'Сохранить',
            'page_selected': 0,
            'user_page_links': [{'pk': 0, 'data': 'Данные пользователя', 'path': 'account'},
                                {'pk': 1, 'data': 'Заказы', 'path': 'account_order'}]
        }

    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()

    def getDict(self):
        return self.context