#
#  review.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.05.2023.
#

from ..models import * #база данных
from .common_data.footer import Footer
from .common_data.header import Header
from .common_data.authorisation import Authorization

class Review_page(object):
    def __init__(self,request, product_id):
        self.startBuilder(request)

        self.header.setData(value = 'Добавить комментарий')
        self.header.setData(name = 'content_style_path', value = 'flower/css/review.css')
        
        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'user': self.auth.getAuthorizedUser(),
            'product': Flower.objects.get(pk=product_id),
            'action_url': reverse("review", kwargs={"product_id": product_id}),
            'form': ''
        }    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)

    def getDict(self):
        return self.context
