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
        self.authenticationPages= []

        self.userPages.append(UserPages.objects.filter(alter_name = 'user')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'order')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'logout')[0])
        self.authenticationPages.append(UserPages.objects.filter(alter_name = 'login')[0])
        self.authenticationPages.append(UserPages.objects.filter(alter_name = 'registration')[0])

class User_context():
    def __init__(self):
        self.commonData = CommonBuild()

        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
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
    
class Login_context(object):
    def __init__(self):
        self.commonData = CommonBuild()

        script_list = [{'script_url':'flower/js/ajax_try.js'}]
        
        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
        self.commonData.header.setData(value = 'Авторизация пользователя')
        self.commonData.footer.setData(name='script_list', value=script_list)
        
        self.context = {
            'header': self.commonData.header.getData(),
            'footer': self.commonData.footer.getData(),
            'form': '', 
            'button_submit': 'Войти',
            'button_redirect': 'Регистрация',
            'action_page': self.commonData.authenticationPages[0].get_absolute_url,
            'href_page': self.commonData.authenticationPages[1].get_absolute_url
        }

    def getContext(self):
        return self.context

class Registration_context(object):
    def __init__(self):
        self.commonData = CommonBuild()
        
        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
        self.commonData.header.setData(value = self.commonData.authenticationPages[1].name)
        
        self.context = {
            'header': self.commonData.header.getData(),
            'footer': self.commonData.footer.getData(),
            'form': '',
            'button_submit': 'Зарегистрировать',
            'button_redirect': 'Авторизация',
            'action_page': self.commonData.authenticationPages[1].get_absolute_url,
            'href_page': self.commonData.authenticationPages[0].get_absolute_url
        }

    def getContext(self):
        return self.context

class Account_page(object):
    def __init__(self, section_name):
        if section_name == 'user':
            self.context = User_context().getContext()
        elif section_name == 'order':
            self.context = Order_context().getContext()
        elif section_name == 'login':
            self.context = Login_context().getContext()
        elif section_name == 'registration':
            self.context = Registration_context().getContext() 
        elif section_name == 'logout':
            self.context = {'page_selected': 3}
        else:
            return {}

    def getDict(self):
        return self.context