from ...models import * #база данных
from django.shortcuts import render, redirect


class Footer(object):
    def __init__(self):
        self.startBuilder()
        
        self.context = {
            'columnLinks': self.columnLinks,
            'script_list': self.script_list,
            'info_pages_columns': self.info_pages_data}

    def startBuilder(self):
        self.info_pages_cl = InfoClass.objects.all()
        self.info_pages = InfoPages.objects.all()
        self.columnLinks = [{'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'},
                        {'name':'Цветы', 'path':'home'}]
        
        self.info_pages_data = self.vocabularyFormation(self.info_pages_cl, self.info_pages, self.columnLinks)
        
        self.script_list = []

    def setData(self, name='name', value='data'):
        self.context[name] = value
    
    def getData(self):
        return self.context
    
    def vocabularyFormation(self, class_info, info_pages, pop_pages):
        result_dict = []
        
        for cl_item in class_info:
            temp = []
            for page in info_pages:
                if page.order == cl_item.pk:
                    temp.append({'name': page.name, 'path': page.path})
                
            if cl_item.name_code == 'popular':
                result_dict.append({'column_title': cl_item.name, 'info_pages_links': pop_pages})
            else:
                result_dict.append({'column_title': cl_item.name, 'info_pages_links': temp})            

        return result_dict