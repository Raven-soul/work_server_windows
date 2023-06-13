#
#  account_list.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 17.05.2023.
#

from ...models import * #база данных
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
                'products': products,
                'listCode': 'select'
            }
        elif section_name == 'purchased_short':
            products = []
            for elem in PurchasedProducts.objects.filter(user = auth.getAuthorizedUser()):
                products.append({
                        'position': elem,
                        'totalPrice': round(int(elem.count)*float(elem.product.price)),
                        'color': self.getColor(elem.status.code),
                        'button': {
                            'name': self.getButton(elem.status.code),
                            'function': self.getFunction(elem.status.code)
                        }
                    })
            
            self.context = {
                'products': products,
                'listCode': 'purchase'
            }
        elif section_name == 'liked_short':
            self.context = {
                'products': LikedProducts.objects.filter(user = auth.getAuthorizedUser()),
                'listCode': 'like'
            }

    def getDict(self):
        return self.context
    
    def getColor(self, code):
        if code == 0:
            return 'red;'
        elif code == 1:
            return 'rgb(238, 191, 37);'
        elif code == 2:
            return 'green;'
        else:
            return ''
        
    def getButton(self, code):
        if code == 0:
            return 'Отмена'
        elif code == 1:
            return 'none'
        elif code == 2:
            return 'Отзыв'
        else:
            return ''
        
    def getFunction(self, code):
        if code == 0:
            return 'productDelete'
        elif code == 1:
            return 'none'
        elif code == 2:
            return 'addReview'
        else:
            return ''