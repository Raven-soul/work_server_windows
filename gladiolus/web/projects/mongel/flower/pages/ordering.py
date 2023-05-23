from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header
from .common_data.authorisation import Authorization

class Ordering_page(object):
    def __init__(self, request):
        self.startBuilder(request)

        self.header.setData(value = 'Оформление заказа')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/ordering.css')
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'form': ''
        }    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)

    def getDict(self):
        return self.context
