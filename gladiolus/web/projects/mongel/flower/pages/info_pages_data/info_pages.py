from ...models import * #база данных
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header

class Set_start_properties(object):
    def __init__(self, request):
        self.startBuilder(request)

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()

        self.header.setData(name='content_style_path', value='flower/css/info_page.css')

    def getHeader(self):
        return self.header;

    def getFooter(self):
        return self.footer;
    

class About_page(object):
    def __init__(self, request):
        self.startBuilder(request)
              
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 1
        }

    def startBuilder(self,request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'О нас')

    def getDict(self):
        return self.context
    
class Payment_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 2
        }

    def startBuilder(self, request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'Оплата')

    def getDict(self):
        return self.context

class Guarantees_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 3
        }

    def startBuilder(self, request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'Гарантии')

    def getDict(self):
        return self.context

class Return_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 4
        }

    def startBuilder(self, request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'Возврат')

    def getDict(self):
        return self.context
    
class Contacts_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 5
        }

    def startBuilder(self, request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'Контакты')

    def getDict(self):
        return self.context
    
class Help_page(object):
    def __init__(self, request):
        self.startBuilder(request)

        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'inf_selected': 6
        }

    def startBuilder(self, request):
        self.contextData = Set_start_properties(request)
        self.contextData.getHeader().setData(value = 'Помощь')

        script_list = [{'script_url':'flower/js/help.js'}]
        self.contextData.getFooter().setData(name='script_list', value=script_list)

    def getDict(self):
        return self.context