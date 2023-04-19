from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.common import Header, Footer

class About_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'О нас')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация о магазине'
        }

    def getDict(self):
        return self.context
    
class Delivery_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Доставка')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация о доставке'
        }

    def getDict(self):
        return self.context
    
class Payment_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Оплата')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация об оплате'
        }

    def getDict(self):
        return self.context

class Guarantees_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Гарантии')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация о гарантиях'
        }

    def getDict(self):
        return self.context

class Return_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Возврат')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация о возврате товара'
        }

    def getDict(self):
        return self.context
    
class Corporation_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Для корпоративных клиентов')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация корпаративным клиентам'
        }

    def getDict(self):
        return self.context
    
class Contacts_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Контакты')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация о наших контактах'
        }

    def getDict(self):
        return self.context
    
class Help_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Помощь')

        footer = Footer()
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
            'content_data': 'информация'
        }

    def getDict(self):
        return self.context