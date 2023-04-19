from ...models import * #база данных

from django.shortcuts import render, redirect
from ..common_data.common import Header, Footer

class Main_occasion_page(object):    
    def __init__(self, occ_id):
        self.occ_id = occ_id
        self.startBuilder()
        
        #--------------Строка для того чтобы зафиксировалась кнопка на панеле хедера--------
        self.header.setData(name='cat_selected', value={'section': 2, 'order': self.occ_id}) 

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': self.products
        }

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.products = Flower.objects.filter(categ=self.occ_id)

    def getDict(self):
        return self.context