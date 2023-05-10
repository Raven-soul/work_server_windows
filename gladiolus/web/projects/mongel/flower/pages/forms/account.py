from ...models import * #база данных
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..common_data.footer import Footer
from ..common_data.header import Header
from ...forms import *

class Account_page(object):
    def __init__(self, request, section_name):
        self.startBuilder(request)
        
        if section_name == 'user':
            self.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_pages.css')
            self.header.setData(value = self.userPages[0].name)
            
            
            self.context = {
                'header': self.header.getData(),
                'footer': self.footer.getData(),
                'form': '',
                'form_title': self.userPages[0].name,
                'action_page': self.userPages[0].get_absolute_url,
                'button_submit': 'Сохранить',
                'page_selected': 1,
                'user_page_links': self.userPages
            }
        elif section_name == 'order':
            self.header.setData(name = 'content_style_path', value = 'flower/css/user_account_pages.css')
            self.header.setData(value = self.userPages[1].name)
            
            
            self.context = {
                'header': self.header.getData(),
                'footer': self.footer.getData(),
                
                'page_selected': 2,
                'data_selected': 0,
                'user_page_links': self.userPages
            }
        elif section_name == 'logout':
            self.context = {                
                'page_selected': 3,
                'user_page_links': self.userPages
            }


    def startBuilder(self, request):
        self.header = Header()
        self.footer = Footer()
        self.userPages= [] 
        self.userPages.append(UserPages.objects.filter(alter_name = 'user')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'order')[0])
        self.userPages.append(UserPages.objects.filter(alter_name = 'logout')[0])

    def getDict(self):
        return self.context