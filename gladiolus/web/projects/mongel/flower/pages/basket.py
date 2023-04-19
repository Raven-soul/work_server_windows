from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Basket_page(object):
    def __init__(self):
        posts = Flower.objects.all()
        header = Header()
        header.setData(value = 'Корзина пользователя')
        header.setData(name = 'content_style_path', value = 'flower/css/content/basket_content.css')
        header.setData(name = 'onload_function', value = "'common-data', 'product-item-'")

        script_list = [{'script_url':'flower/js/basket.js'}]

        footer = Footer()
        footer.setData(name = 'script_list', value = script_list)
        
        self.context = {
            'header': header.getData(),
            'footer': footer.getData(),
        }

    def getDict(self):
        return self.context
