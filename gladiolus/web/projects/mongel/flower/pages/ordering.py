from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header
from .common_data.authorisation import Authorization

class Ordering_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.header.setData(value = 'Оформление заказа')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/ordering.css')

        totalPrice = 0
        for element in self.products:
            totalPrice += element.product.price * element.count
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'total_price': totalPrice,
            'user': self.auth.getAuthorizedUser(),
            'form': ''
        }    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)
        self.products = SelectedProducts.objects.filter(user=self.auth.getAuthorizedUser())

    def getDict(self):
        return self.context
