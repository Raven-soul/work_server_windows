from ...models import * #база данных
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
            'form': self.form
        }

    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()
        self.form = self.formValidation(request)

    def getDict(self):
        return self.context
    
    def formValidation(self, request):
        if request.method == 'POST':
            form = RegistrationPostForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
        else:
            form = RegistrationPostForm()

        return form
