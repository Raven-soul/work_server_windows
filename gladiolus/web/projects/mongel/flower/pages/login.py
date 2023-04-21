from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Login_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Авторизация пользователя')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'Окно авторизации'
        }

    def getDict(self):
        return self.context