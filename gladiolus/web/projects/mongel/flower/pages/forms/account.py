from ...models import * #база данных
from ..common_data.footer import Footer
from ..common_data.header import Header
from ..common_data.authorisation import Authorization

class CommonBuild(object):
    def __init__(self, request):
        self.startBuilder(request)

        self.context = {
            'header': self.header.getData(),
            'footer': self.footer.getData(),
            'user_page_links': self.userPages.values()
        }
    

    def startBuilder(self, request):
        self.header = Header(request)
        self.footer = Footer()
        self.auth = Authorization(request)

        self.userPages = {'user': UserPages.objects.get(alter_name = 'user'),
                           'order': UserPages.objects.get(alter_name = 'order'),
                           'logout': UserPages.objects.get(alter_name = 'logout')}
        
        self.authenticationPages = {'login': UserPages.objects.get(alter_name = 'login'),
                                     'registration': UserPages.objects.get(alter_name = 'registration')}

class User_context(object):
    def __init__(self, request):
        self.commonData = CommonBuild(request)

        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
        self.commonData.header.setData(value = self.commonData.userPages['user'].name)
        
        self.context = {
            'form': '',
            'form_title': self.commonData.userPages['user'].name,
            'action_page': self.commonData.userPages['user'].get_absolute_url,
            'button_submit': 'Сохранить',
            'page_selected': 1
        }

        self.contextAll = dict(list(self.context.items()) + list(self.commonData.context.items()))
    
    def getContext(self):
        return self.contextAll
    
class Order_context(object):
    def __init__(self, request):
        self.commonData = CommonBuild(request)
        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/user_account_pages.css')
        self.commonData.header.setData(value = self.commonData.userPages['order'].name)
        self.commonData.footer.setData(name = 'script_list', value = [{'script_url':'flower/js/ajax/accountLists.js'}])  
              
        products = []
        for elem in SelectedProducts.objects.filter(user=self.commonData.auth.getAuthorizedUser()):
            products.append({
                'position': elem,
                'totalPrice': round(int(elem.count)*float(elem.product.price))
            })

        buttons = [{'pk': 0, 'img': 'fa-solid fa-cart-shopping', 'function': 'showSelectedList(this)'},
                   {'pk': 1, 'img': 'fa-solid fa-check', 'function': 'showPurchasedList(this)'},
                   {'pk': 2, 'img': 'fa-regular fa-heart', 'function': 'showFavoriteList(this)'}]

        self.context = {            
            'page_selected': 2,
            'button_selected': 0,
            'buttons': {'array': buttons,
                        'length': len(buttons)},
            'products' : products
        }

        self.contextAll = dict(list(self.context.items()) + list(self.commonData.context.items()))
    
    def getContext(self):
        return self.contextAll
    
class Login_context(object):
    def __init__(self, request):
        self.commonData = CommonBuild(request)

        script_list = [{'script_url':'flower/js/ajax_try.js'}]
        
        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
        self.commonData.header.setData(value = self.commonData.authenticationPages['login'].name)
        self.commonData.footer.setData(name='script_list', value=script_list)
        
        self.context = {
            'form': '', 
            'button_submit': 'Войти',
            'button_redirect': 'Регистрация',
            'action_page': self.commonData.authenticationPages['login'].get_absolute_url,
            'href_page': self.commonData.authenticationPages['registration'].get_absolute_url
        }

        self.contextAll = dict(list(self.context.items()) + list(self.commonData.context.items()))

    def getContext(self):
        return self.contextAll

class Registration_context(object):
    def __init__(self, request):
        self.commonData = CommonBuild(request)
        
        self.commonData.header.setData(name = 'content_style_path', value = 'flower/css/forms/user_form_pages.css')
        self.commonData.header.setData(value = self.commonData.authenticationPages['registration'].name)
        
        self.context = {
            'form': '',
            'button_submit': 'Зарегистрировать',
            'button_redirect': 'Авторизация',
            'action_page': self.commonData.authenticationPages['registration'].get_absolute_url,
            'href_page': self.commonData.authenticationPages['login'].get_absolute_url
        }

        self.contextAll = dict(list(self.context.items()) + list(self.commonData.context.items()))

    def getContext(self):
        return self.contextAll

class Account_page(object):
    def __init__(self, section_name, request):
        if section_name == 'user':
            self.context = User_context(request).getContext()
        elif section_name == 'order':
            self.context = Order_context(request).getContext()
        elif section_name == 'login':
            self.context = Login_context(request).getContext()
        elif section_name == 'registration':
            self.context = Registration_context(request).getContext() 
        elif section_name == 'logout':
            self.context = {'page_selected': 3}
        else:
            return {}

    def getDict(self):
        return self.context