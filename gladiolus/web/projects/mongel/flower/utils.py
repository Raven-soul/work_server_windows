#
#  utils.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 26.04.2023.
#

#------------- Общие страницы сайта --------------------------

from .pages.common_data.footer import Footer
from .pages.common_data.authorisation import Authorization

#------------------ common data --------------------------

class DataMixin:
    def get_user_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        footer = Footer()

        self.context['header'] = ''
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