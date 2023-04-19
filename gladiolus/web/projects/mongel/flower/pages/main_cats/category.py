from ...models import * #база данных

from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header

class Main_category_page(object):    
    def __init__(self, cat_id):
        self.cat_id = cat_id
        self.startBuilder()
        
        #--------------Строка для того чтобы зафиксировалась кнопка на панеле хедера--------
        self.header.setData(name='cat_selected', value={'section': 1, 'order': self.cat_id}) 

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': self.products
        }

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.products = Flower.objects.filter(categ=self.cat_id)

    def getDict(self):
        return self.context