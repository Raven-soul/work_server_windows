#
#  payment.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 21.05.2023.
#

from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header
from .common_data.authorisation import Authorization

class Payment_main_page(object):
    def __init__(self, request):
        self.startBuilder(request)
        
        self.header.setData(value = 'Оплата')
        self.header.setData(name = 'content_style_path', value = 'flower/css/content/payment.css')
        self.footer.setData(name = 'script_list', value = self.script_list)

        totalPrice = 0
        for element in self.products:
            totalPrice += element.product.price * element.count
        
        print('------------------------------', self.getMethods())

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'total_price': totalPrice,
            'methods': self.getMethods(),
            'user': self.auth.getAuthorizedUser()
        }    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)
        self.products = SelectedProducts.objects.filter(user=self.auth.getAuthorizedUser())
        self.script_list = [{'script_url':'flower/js/ajax/payment.js'}]

    def getMethods(self):
        result = []
        for section in PaymentMethodSection.objects.all():
            result.append({'section': section.name, 'methods': ''})

        for element in result:
            element['methods'] = PaymentMethod.objects.filter(section=PaymentMethodSection.objects.get(name=element['section']))
        
        return result

    def getDict(self):
        return self.context
