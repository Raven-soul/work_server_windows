from ..models import * #база данных
from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Detail_page(object):
    def __init__(self, prod_id):
        self.startBuilder(prod_id)

        script_list = [{'script_url':'flower/js/detail.js'}]

        self.header.setData(name = 'content_style_path', value = 'flower/css/content/detail_content.css')
        self.footer.setData(name = 'script_list', value = script_list)

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'product': self.productContext
        }

    def startBuilder(self, prod_id):
        self.header = Header()
        self.footer = Footer()

        productList = Flower.objects.all()
        productItem = self.productSearch(productList, prod_id)

        print('--------------------------------', productItem.photo)

        self.productContext = {'name': productItem.title,
                               'grade': 0, 
                               'image': productItem.photo,
                               'price': productItem.price}

    def getDict(self):
        return self.context
    
    def productSearch(self, productDBList, desired_id):
        for item in productDBList:
            if item.pk == desired_id:
                return item
