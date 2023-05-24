from ...models import * #база данных
from ..common_data.header import Header
from ..common_data.authorisation import Authorization

class City_stroke(object):
    def __init__(self, cityId, request):
        self.startBuilder(cityId, request)
        self.context = {
            'header': self.header.getData(),
        }    

    def startBuilder(self, cityId, request):
        auth = Authorization(request)
        User.objects.filter(pk= auth.getAuthorizedUser().pk).update(city_user_field=Cities.objects.get(pk=cityId))
        self.header = Header(request)
        

    def getDict(self):
        return self.context
