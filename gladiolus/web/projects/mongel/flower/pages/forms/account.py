from ...models import * #база данных
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class CommonBuild():
    def __init__(self):
        self.startBuilder()

    def startBuilder(self):
        self.header = Header()
        self.footer = Footer()
        self.userPages= [] 
        self.userPages.append(UserPages.objects.filter(alter_name = 'user')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'order')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'logout')[0])

class User_context():
    def __init__(self):
        self.commonData = CommonBuild()

        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
        self.commonData.header.setData(value = self.commonData.userPages[0].name)
        
        self.context = {
            'header': self.commonData.header.getData(),
            'footer': self.commonData.footer.getData(),
            'form': '',
            'form_title': self.commonData.userPages[0].name,
            'action_page': self.commonData.userPages[0].get_absolute_url,
            'button_submit': 'Сохранить',
            'page_selected': 1,
            'user_page_links': self.commonData.userPages
        }
    
    def getContext(self):
        return self.context
    
class Order_context():
    def __init__(self):
        self.commonData = CommonBuild()

        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/user_account_pages.css')
        self.commonData.header.setData(value = self.commonData.userPages[1].name)
        
        
        self.context = {
            'header': self.commonData.header.getData(),
            'footer': self.commonData.footer.getData(),
            
            'page_selected': 2,
            'button_selected': 0,
            'buttons': [{'pk': 0, 'name': 'Выбранные продукты'},
                    {'pk': 1, 'name': 'Оплаченные продукты'}],
            'user_page_links': self.commonData.userPages
        }
    
    def getContext(self):
        return self.context

class Account_page(object):
    def __init__(self, section_name):
        if section_name == 'user':
            self.context = User_context().getContext()
        elif section_name == 'order':
            self.context = Order_context().getContext()
        elif section_name == 'logout':
            self.context = {'page_selected': 3}

    def getDict(self):
        return self.context