from ...models import * #база данных
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class Login_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        script_list = [{'script_url':'flower/js/ajax_try.js'}]
        
        self.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
        self.header.setData(value = 'Авторизация пользователя')
        self.footer.setData(name='script_list', value=script_list)
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'form': self.form, 
            'button_submit': 'Войти',
            'button_redirect': 'Регистрация',
            'action_page': 'login',
            'href_page': 'registration'
        }

    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()
        self.form = self.formValidation(request)

    def getDict(self):
        return self.context
    
    def formValidation(self, request):
        if request.method == 'POST':
            form = User_form(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
        else:
            form = User_form()

        return form