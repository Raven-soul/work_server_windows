from ...models import * #база данных

from django.shortcuts import render, redirect
from ..common_data.common import Header, Footer

class Main_type_page(object):    
    def __init__(self, typ_id):
        self.typ_id = typ_id
        self.startBuilder()
        
        #--------------Строка для того чтобы зафиксировалась кнопка на панеле хедера--------
        self.header.setData(name='cat_selected', value={'section': 4, 'order': self.typ_id}) 

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': self.products
        }

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.products = Flower.objects.filter(categ=self.typ_id)

    def getDict(self):
        return self.context