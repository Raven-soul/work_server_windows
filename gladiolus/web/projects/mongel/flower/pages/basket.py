from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Basket_page(object):
    def __init__(self):
        self.startBuilder()

        self.header.setData(value = 'Корзина пользователя')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/basket_content.css')
        self.header.setData(name = 'onload_function', value = "'common-data', 'product-item-'")
        self.footer.setData(name = 'script_list', value = self.script_list)
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
        }

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.script_list = [{'script_url':'flower/js/basket.js'}]

    def getDict(self):
        return self.context
