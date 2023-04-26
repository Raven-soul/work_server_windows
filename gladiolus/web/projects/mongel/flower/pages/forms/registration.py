from ...models import * #база данных
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class Registration_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
        self.header.setData(value = 'Регистрация пользователя')
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'form': '',
            'button_submit': 'Зарегистрировать',
            'button_redirect': 'Авторизация',
            'action_page': 'registration',
            'href_page': 'login'
        }

    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()

    def getDict(self):
        return self.context

