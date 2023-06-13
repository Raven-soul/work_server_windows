#
#  empty.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 28.04.2023.
#

from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header

class Empty_page(object):
    def __init__(self, request):
        self.startBuilder(request)

        self.header.setData(value = 'Корзина пользователя')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/detail_content.css')

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'content': ''
        }

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()

    def setContent(self, value = ''):
        self.context['context'] = value

    def getDict(self):
        return self.context