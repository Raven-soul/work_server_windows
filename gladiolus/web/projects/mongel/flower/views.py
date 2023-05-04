from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse, Http404 #перехват исключения
from django.views.generic import ListView
from .forms import *
from .utils import *

#------------- главные страницы сайта --------------------------
from .pages.info_pages_data.info_pages import *
from .pages.forms.login import Login_page
from .pages.forms.registration import Registration_page
from .pages.forms.account import Account_page
from .pages.detail import Detail_page
from .pages.basket import Basket_page
from .pages.empty import Empty_page

from .models import * #база данных

#------------------ main_pages --------------------------

class FlowerHome(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main_content.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_data()
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 0, 'order': 0}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

def product_details(request, prod_id):
    data = Detail_page(prod_id).getDict()
    return render(request, 'flower/main/detail_content.html', context=data)

def setCookie(request):
    user_id = request.param['user_id']
    print('-------------------------------------------------------------- user_id', user_id)
    response = HttpResponse(user_id)
    response.method = "POST"
    response.set_cookie(key='user_id', value=user_id, path='/')
    return response

def basket(request):
    try:
        user_id = request.COOKIES["user_id"]
    except:
        # return redirect('login')
        user_id = 1

    data = Basket_page(user_id).getDict()
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
        c_def['header'] = self.setContextData(c_def['header'], diction=[{'name':'cat_selected', 'value':{'section': 4, 'order': self.kwargs['typ_id']}},])
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    
    def get_queryset(self):
        return Flower.objects.filter(type_data__pk=self.kwargs['typ_id'])

#---------------- info_pages --------------------------

def about_info(request):
    data = About_page().getDict()
    return render(request, 'flower/info_pages/about.html', context=data)

def payment_info(request):
    data = Payment_page().getDict()
    return render(request, 'flower/info_pages/payment.html', context=data)

def guarantees_info(request):
    data = Guarantees_page().getDict()
    return render(request, 'flower/info_pages/guarantees.html', context=data)

def return_info(request):
    data = Return_page().getDict()
    return render(request, 'flower/info_pages/return.html', context=data)

def contacts_info(request):
    data = Contacts_page().getDict()
    return render(request, 'flower/info_pages/contacts.html', context=data)

def help_info(request):
    data = Help_page().getDict()
    return render(request, 'flower/info_pages/help.html', context=data)

#-------------------------------- form pages ---------------------------

def login(request):
    data = Login_page(request).getDict()

    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            print('-*-------------------------------------------------- login')

    else:
        form = RegistrationPostForm()

    data['form'] = form
    return render(request, 'flower/form_pages/login.html', context=data)

def registration(request):
    data = Registration_page(request).getDict()

    if request.method == 'POST':
        form = RegistrationPostForm(request.POST)
        if form.is_valid():
            print('-*-------------------------------------------------- register')

    else:
        form = RegistrationPostForm()

    data['form'] = form
    return render(request, 'flower/form_pages/login.html', context=data)

def account(request):
    data = Account_page(request).getDict()
    user = User.objects.filter(pk=1)
    form = Account_form(initial={'name_user_field': user[0].name_user_field,
                                 'surname_user_field': user[0].surname_user_field,
                                 'email_user_field': user[0].email_user_field,
                                 'password_user_field': user[0].password_user_field,
                                 'city_user_field': user[0].city_user_field,
                                 'phone_user_field': user[0].phone_user_field})

    data['form'] = form
    return render(request, 'flower/form_pages/account_user_data.html', context=data)

#----------------------------------- 404 ----------------------------------------

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#---------------------------- additional material ----------------------------------------
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
    print('-----------------------------------------------------------------')
    context = {'header': Header().getData(),
               'footer': Footer().getData(),
               'content_data': 'js - is ready'}
    print('----------------------------------------------------------------- end')
    return JsonResponse(context)
