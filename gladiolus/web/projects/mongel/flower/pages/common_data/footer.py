from ...models import * #база данных
from django.shortcuts import render, redirect


class Footer(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'columnLinks': self.columnLinks,
            'script_list': self.script_list,
            'info_classes': self.info_pages_cl}

    def startBuilder(self):
        self.info_pages_cl = InfoClass.objects.all()

        self.columnLinks = [{'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'}]
        
        self.script_list = []

    def setData(self, name='name', value='data'):
        self.context[name] = value
    
    def getData(self):
        return self.context