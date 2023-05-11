from ...models import * #база данных

class Authorization():
    def __init__(self, request):
        self.auth_state = False
        self.request = request

    def check_auth(self):
        data = self.request.COOKIES["sessionid"]
        print('------------------------------------------------------------------------',data)
        if User.objects.filter(sessionUNQid = data) != []:
            self.auth_state = True

        return self.auth_state