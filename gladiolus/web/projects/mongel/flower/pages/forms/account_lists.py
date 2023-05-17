from ...models import * #база данных
from ..common_data.footer import Footer
from ..common_data.header import Header
from ..common_data.authorisation import Authorization        

class AccountlistsPages(object):
    def __init__(self, section_name, request):
        auth = Authorization(request)
        
        if section_name == 'choosen_short':
            products = []
            for elem in SelectedProducts.objects.filter(user = auth.getAuthorizedUser()):
                products.append({
                    'position': elem,
                    'totalPrice': round(int(elem.count)*float(elem.product.price))
                })
            
            self.context = {
                'products': products
            }
        elif section_name == 'purchased_short':
            for elem in PurchasedProducts.objects.filter(user = auth.getAuthorizedUser()):
                products.append({
                        'position': elem,
                        'totalPrice': round(int(elem.count)*float(elem.product.price)),
                        'button': ''
                    })
            
            self.context = {
                'products': PurchasedProducts.objects.filter(user = auth.getAuthorizedUser())
            }
        elif section_name == 'liked_short':
            self.context = {
                'products': LikedProducts.objects.filter(user = auth.getAuthorizedUser())
            }

    def getDict(self):
        return self.context