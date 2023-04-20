from ...models import * #база данных
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header

class Set_start_properties():
    def __init__(self):
        self.startBuilder()

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()

        self.header.setData(name='content_style_path', value='flower/css/info_page.css')

    def getHeader(self):
        return self.header;

    def getFooter(self):
        return self.header;
    

class About_page(object):
    def __init__(self):
        self.startBuilder()
              
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация о магазине'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'О нас')

    def getDict(self):
        return self.context
    
class Payment_page(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация об оплате'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'Оплата')

    def getDict(self):
        return self.context

class Guarantees_page(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация о гарантиях'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'Гарантии')

    def getDict(self):
        return self.context

class Return_page(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация о возврате товара'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'Возврат')

    def getDict(self):
        return self.context
    
class Contacts_page(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация о наших контактах'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'Контакты')

    def getDict(self):
        return self.context
    
class Help_page(object):
    def __init__(self):
        self.startBuilder()

        self.context = {
            'header': self.contextData.getHeader().getData(),
            'footer': self.contextData.getFooter().getData(),
            'content_data': 'информация'
        }

    def startBuilder(self):
        self.contextData = Set_start_properties()
        self.contextData.getHeader().setData(value = 'Помощь')

        script_list = [{'script_url':'flower/js/help.js'}]
        self.contextData.getFooter().setData(name='script_list', value=script_list)

    def getDict(self):
        return self.context