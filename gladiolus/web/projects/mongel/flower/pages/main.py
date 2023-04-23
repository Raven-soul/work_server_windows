from ..models import * #база данных

from django.shortcuts import render, redirect
from .common_data.footer import Footer
from .common_data.header import Header

class Main_page(object):    
    def __init__(self):
        self.startBuilder()
        
        self.header.setData(name='cat_selected', value= {'section': 0, 'order': 0})
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': self.products
        }

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.products = Flower.objects.all()
        

    def getDict(self):
        return self.context
