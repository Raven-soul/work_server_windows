from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Basket_page(object):
    def __init__(self, user_id, request):
        self.startBuilder(request)
        user = User.objects.filter(pk = int(user_id))
        products = self.doublesClear(SelectedProducts.objects.filter(user=user[0]))

        self.header.setData(value = 'Корзина пользователя')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/basket_content.css')
        self.header.setData(name = 'onload_function', value = "'common-data', 'product-item-'")
        self.footer.setData(name = 'script_list', value = self.script_list)
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': products,
            'products_length': len(products)
        }

    def doublesClear(self, list):
        result_List= []
        pk_list= []

        for elem in list:
            if elem.product.pk in pk_list:
                pass
            else:
                result_List.append(elem)
                pk_list.append(elem.product.pk)

        return result_List
    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.script_list = [{'script_url':'flower/js/basket.js'}]

    def getDict(self):
        return self.context
