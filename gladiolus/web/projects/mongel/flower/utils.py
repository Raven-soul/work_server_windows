#------------- Общие страницы сайта --------------------------

from .pages.common_data.footer import Footer
from .pages.common_data.header import Header

#------------------ common data --------------------------

class DataMixin:
    def get_user_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        header = Header()
        footer = Footer()

        self.context['header'] = header.getData()
        self.context['footer'] = footer.getData()
        return self.context
    
    def setContextData(self, context_data, diction=[{'name': '', 'value': ''},]):
        context = context_data
        for  elem in diction:
            if elem['name'] != '':
                name = elem['name']
                value = elem['value']
                context[name] = value 
        return context