from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse, Http404 #перехват исключения
from django.views.generic import ListView
from .forms import *
from .utils import *

#------------- главные страницы сайта --------------------------
from .pages.info_pages_data.info_pages import *
from .pages.forms.account import Account_page
from .pages.forms.account_lists import AccountlistsPages
from .pages.detail import Detail_page
from .pages.basket import Basket_page
from .pages.empty import Empty_page
from .pages.review import Review_page

from .models import * #база данных
from .pages.common_data.authorisation import Authorization
from .pages.common_data.definitionProduct import DefinitionProduct

#------------------ main_pages --------------------------

class FlowerHome(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = Header(self.request).getData()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 0, 'order': 0}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

def product_details(request, prod_id):
    if not request.session.session_key:
        request.session.create()

    data = Detail_page(prod_id, request).getDict()
    return render(request, 'flower/main/detail_content.html', context=data)

def basket(request):
    if not request.session.session_key:
        request.session.create()
    
    auth = Authorization()
    if auth.isAuthorized == False:
        return redirect('/account/login')
    
    data = Basket_page(request).getDict()
    if len(data['products']) == 0:
        empty_data =  Empty_page(title='Корзина пуста').getDict()
        empty_data['context'] = 'Корзина пуста'
        return render(request, 'flower/main/empty_page.html', context=empty_data)
    else:
        return render(request, 'flower/main/basket_content.html', context=data)
    
def ordering(request):
    if not request.session.session_key:
        request.session.create()
    
    user_id = 1  
    data = Basket_page(user_id, request).getDict()
    if len(data['products']) == 0:
        empty_data =  Empty_page(title='Корзина пуста').getDict()
        empty_data['context'] = 'Корзина пуста'
        return render(request, 'flower/main/empty_page.html', context=empty_data)
    else:
        return render(request, 'flower/main/basket_content.html', context=data)
    
def payment(request):
    if not request.session.session_key:
        request.session.create()
    
    user_id = 1  
    data = Basket_page(user_id, request).getDict()
    if len(data['products']) == 0:
        empty_data =  Empty_page(title='Корзина пуста').getDict()
        empty_data['context'] = 'Корзина пуста'
        return render(request, 'flower/main/empty_page.html', context=empty_data)
    else:
        return render(request, 'flower/main/basket_content.html', context=data)

#--------------- main_cats_pages --------------------------

class FlowerShowCategory(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = Header(self.request).getData()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 1, 'order': self.kwargs['cat_id']}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        return Flower.objects.filter(categ__pk=self.kwargs['cat_id'])

class FlowerShowOccasion(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = Header(self.request).getData()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 2, 'order': self.kwargs['occ_id']}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        return Flower.objects.filter(reason_data__pk=self.kwargs['occ_id'])

class FlowerShowSeason(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = Header(self.request).getData()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 3, 'order': self.kwargs['sea_id']}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        return Flower.objects.filter(maturation_data__pk=self.kwargs['sea_id'])

class FlowerShowType(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = Header(self.request).getData()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 4, 'order': self.kwargs['typ_id']}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        return Flower.objects.filter(type_data__pk=self.kwargs['typ_id'])

#---------------- info_pages --------------------------

def about_info(request):
    if not request.session.session_key:
        request.session.create()
    data = About_page(request).getDict()
    return render(request, 'flower/info_pages/about.html', context=data)

def payment_info(request):
    if not request.session.session_key:
        request.session.create()
    data = Payment_page(request).getDict()
    return render(request, 'flower/info_pages/payment.html', context=data)

def guarantees_info(request):
    if not request.session.session_key:
        request.session.create()
    data = Guarantees_page(request).getDict()
    return render(request, 'flower/info_pages/guarantees.html', context=data)

def return_info(request):
    if not request.session.session_key:
        request.session.create()
    data = Return_page(request).getDict()
    return render(request, 'flower/info_pages/return.html', context=data)

def contacts_info(request):
    if not request.session.session_key:
        request.session.create()
    data = Contacts_page(request).getDict()
    return render(request, 'flower/info_pages/contacts.html', context=data)

def help_info(request):
    if not request.session.session_key:
        request.session.create()
    data = Help_page(request).getDict()
    return render(request, 'flower/info_pages/help.html', context=data)

#-------------------------------- form pages ---------------------------
def account(request, section_name):
    if not request.session.session_key:
        request.session.create()

    auth = Authorization(request)
    data = Account_page(section_name, request).getDict()
    #------------------------------------------------------------------------------- user
    if section_name == 'user':
        if auth.isAuthorized() == False:
            return redirect('/account/login')

        user = auth.getAuthorizedUser()
        if request.method == 'POST':
            form = Account_form(request.POST)
            if form.is_valid():
                user = auth.getAuthorizedUser()
                user.surname_user_field = form.cleaned_data['surname_user_field']
                user.city_user_field = form.cleaned_data['city_user_field']
                user.phone_user_field = form.cleaned_data['phone_user_field']
                user.save()
        else:
            form = Account_form(initial={'name_user_field': user.name_user_field,
                                        'surname_user_field': user.surname_user_field,
                                        'email_user_field': user.email_user_field,
                                        'password_user_field': user.password_user_field,
                                        'city_user_field': user.city_user_field,
                                        'phone_user_field': user.phone_user_field})
        
        data['form'] = form
        return render(request, 'flower/form_pages/account_user.html', context=data)
    
    #------------------------------------------------------------------------------- order
    elif section_name == 'order':
        if auth.isAuthorized() == False:
            return redirect('/account/login')

        data['header']['onload_function'] = '"data-show", "data-content"'
        return render(request, 'flower/form_pages/account_order.html', context=data)
    
    #------------------------------------------------------------------------------- login
    elif section_name == 'login':
        if auth.isAuthorized():
            return redirect('/account/user')

        if request.method == 'POST':
            form = Login_form(request.POST)
            if form.is_valid():
                for user in User.objects.all():
                    if form.cleaned_data['email_user_field'] == user.name_user_field:
                        if form.cleaned_data['password_user_field'] == user.password_user_field:
                            User.objects.filter(pk=user.pk).update(sessionUNQid=request.COOKIES["sessionid"])
                            return redirect('/account/user')
        else:
            form = Login_form()

        data['form'] = form
        return render(request, 'flower/form_pages/login.html', context=data)
    
    #------------------------------------------------------------------------------- registration
    elif section_name == 'registration':
        if auth.isAuthorized():
            return redirect('/account/user')

        if request.method == 'POST':
            form = RegistrationPostForm(request.POST)
            if form.is_valid():
                
                User.objects.create(name_user_field = form.cleaned_data['name_register_field'], 
                                    email_user_field = form.cleaned_data['email_register_field'],
                                    password_user_field = form.cleaned_data['password_first_register_field'])
                auth.logout()
                auth.login(User.objects.filter(email_user_field= form.cleaned_data['email_register_field']))
                return redirect('/account/user')
        else:
            form = RegistrationPostForm()

        data['form'] = form
        return render(request, 'flower/form_pages/login.html', context=data)
    
    #------------------------------------------------------------------------------- registration
    elif section_name == 'logout':
        auth.logout()
        return redirect('/account/login')
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def review(request):
    context = Review_page(request, 9).getDict()
    return render(request, 'flower/main/review.html', context=context)

#----------------------------------- 404 ----------------------------------------

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#---------------------------- additional material ----------------------------------------
def append(request):
    auth = Authorization(request)
    if auth.isAuthorized():
        defProd = DefinitionProduct(auth.getAuthorizedUser())
        JsonData = {}
        if request.POST.get('typeRequest', '') == 'addToSelectList':
            defProd.appendToSelectedList(request.POST.get("user_id", "none"))
            if request.POST.get('isRedirect', ''):
                JsonData['redirect'] = '/basket'
        elif request.POST.get('typeRequest', '') == 'addToFavoriteList':
            defProd.appendTokedList(request.POST.get("user_id", "none"))
    return JsonResponse(JsonData)

def delete(request):
    auth = Authorization(request)
    defProd = DefinitionProduct(auth.getAuthorizedUser())
    if request.POST.get('list', '') == 'select':
        defProd.deleteFromSelectedList(request.POST.get('productId', ''))
    elif request.POST.get('list', '') == 'purchase':
        defProd.deleteFromPurchasedList(request.POST.get('productId', ''))
    elif request.POST.get('list', '') == 'like':
        defProd.deleteFromLikedList(request.POST.get('productId', ''))
    return HttpResponse()

def startReview(request):
    JsonData = {'redirect': '/review'}
    return JsonResponse(JsonData)

def accountLists(request):
    auth = Authorization(request)
    if auth.isAuthorized():
        if request.POST.get('typeRequest', '') == 'choosen_short':
            return render(request, 'flower/form_pages/order_temps/acc_order_choosen_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        elif request.POST.get('typeRequest', '') == 'liked_short':
            return render(request, 'flower/form_pages/order_temps/acc_order_liked_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        elif request.POST.get('typeRequest', '') == 'purchased_short':
            return render(request, 'flower/form_pages/order_temps/acc_order_purchased_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        else:
            return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#---------------------------- other material ----------------------------------------

def js_data(request):
    script_list = [{'script_url':'flower/js/ajax_try.js'}]

    header = Header()
    footer = Footer()

    footer.setData(name='script_list', value=script_list)

    context = {'header': header.getData(),
               'footer': footer.getData(),
               'content_data': 'проверяем аджакс', 
               'onclick_function': 'data_click()'}
    return render(request, 'flower/main/index_shop_page_button.html', context=context)

def js_start_data(request):
    if not request.session.session_key:
        request.session.create()

    auth = Authorization(request)
    username = auth.isAuthorized()
    
    context = {'header': Header(request).getData(),
               'footer': Footer().getData(),
               'content_data': username}
    return render(request, 'flower/main/index_page_button_const.html', context=context)