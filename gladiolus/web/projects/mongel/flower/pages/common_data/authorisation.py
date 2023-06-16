#
#  authorisation.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 11.05.2023.
#

from ...models import * #база данных

class Authorization():
    def __init__(self, request):
        self.auth_state = False
        try:
            self.cookiesId = request.COOKIES["csrftoken"]
        except:
            try:
                self.cookiesId = request.COOKIES["sessionid"]
            except:
                self.cookiesId = "error"
        self.request = request

    def isAuthorized(self):
        if User.objects.filter(sessionUNQid = self.cookiesId).exists():
            self.auth_state = True
        return self.auth_state
    
    def getAuthorizedUser(self):
        return User.objects.get(sessionUNQid = self.cookiesId)
    
    def logout(self):
        if self.isAuthorized():
            User.objects.filter(sessionUNQid = self.cookiesId).update(sessionUNQid = '0')

    def login(self, user = User.objects.filter(pk=1)):
        user.update(sessionUNQid = self.cookiesId)
