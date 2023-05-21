from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header
from .common_data.authorisation import Authorization

class Basket_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        user = self.auth.getAuthorizedUser()
        products = SelectedProducts.objects.filter(user=user)

        self.header.setData(value = 'Корзина пользователя')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/basket.css')
        self.header.setData(name = 'onload_function', value = "'common-data', 'product-item-'")
        self.footer.setData(name = 'script_list', value = self.script_list)
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'products': products,
            'products_length': len(products)
        }    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)
        self.script_list = [{'script_url':'flower/js/basket.js'}]

    def getDict(self):
        return self.context
