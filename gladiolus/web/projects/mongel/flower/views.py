from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404 #перехват исключения

#-------------главные страницы сайта --------------------------
from .pages.main import Main_page
from .pages.info_pages_data.info_pages import *
from .pages.forms.login import Login_page
from .pages.forms.registration import Registration_page
from .pages.detail import Detail_page
from .pages.basket import Basket_page
from .pages.main_cats.category import *
from .pages.main_cats.occasion import *
from .pages.main_cats.season import *
from .pages.main_cats.type import *

from .models import * #база данных

#------------------ main_pages --------------------------

def index(request):
    data = Main_page().getDict()
    return render(request, 'flower/main/main_content.html', context=data)

def product_details(request, prod_id):
    data = Detail_page(prod_id).getDict()
    return render(request, 'flower/main/detail_content.html', context=data)

def basket(request):
    data = Basket_page().getDict()
    return render(request, 'flower/main/basket_content.html', context=data)

def login(request):
    data = Login_page(request).getDict()
    return render(request, 'flower/form_pages/login.html', context=data)

def registration(request):
    data = Registration_page(request).getDict()
    return render(request, 'flower/form_pages/login.html', context=data)

#--------------- main_cats_pages --------------------------

def show_category(request, cat_id):
    data = Main_category_page(cat_id).getDict()
    return render(request, 'flower/main/main_content.html', context=data)

def show_occasion(request, occ_id):
    data = Main_occasion_page(occ_id).getDict()
    return render(request, 'flower/main/main_content.html', context=data)

def show_season(request, sea_id):
    data = Main_season_page(sea_id).getDict()
    return render(request, 'flower/main/main_content.html', context=data)

def show_type(request, typ_id):
    data = Main_type_page(typ_id).getDict()
    return render(request, 'flower/main/main_content.html', context=data)

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


#----------------------------------- 404 ----------------------------------------

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
