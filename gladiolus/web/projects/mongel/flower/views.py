from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse, Http404 #перехват исключения
from django.views.generic import ListView
from .forms import *
from .utils import *
from .models import * #база данных
import json
import datetime

#------------- главные страницы сайта --------------------------
from .pages.detail import Detail_page
from .pages.basket import Basket_page
from .pages.ordering import Ordering_page
from .pages.payment import Payment_main_page

#------------- пользовательские страницы сайта --------------------------
from .pages.forms.account import Account_page
from .pages.forms.account_lists import AccountlistsPages

#------------- дополнительные страницы сайта --------------------------
from .pages.info_pages_data.info_pages import *
from .pages.empty import Empty_page
from .pages.review import Review_page
from .pages.short_pages.city_stroke import City_stroke

#------------- Классы для работы с пользователем и продуктами --------------------------
from .pages.common_data.authorisation import Authorization
from .pages.common_data.definitionProduct import DefinitionProduct

#------------------ main_pages --------------------------

class FlowerHome(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main.html'
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
    return render(request, 'flower/main/detail.html', context=data)

def basket(request):
    if not request.session.session_key:
        request.session.create()

    auth = Authorization(request)
    if auth.isAuthorized() == False:
        return redirect('/account/login')

    data = Basket_page(request).getDict()
    if len(data['products']) == 0:
        empty_data =  Empty_page(request=request).getDict()
        empty_data['context'] = 'Корзина пуста'
        return render(request, 'flower/main/complex_templates/empty_page.html', context=empty_data)
    else:
        return render(request, 'flower/main/basket.html', context=data)

def ordering(request):
    if not request.session.session_key:
        request.session.create()

    auth = Authorization(request)
    isCreation = True
    if auth.isAuthorized() == False:
        return redirect('/account/login')

    user = auth.getAuthorizedUser()

    if SelectedProducts.objects.filter(user=user).exists():
        if SelectedProducts.objects.last().order_code != None and Order.objects.filter(sender_user=user).exists():
            if SelectedProducts.objects.last().order_code == Order.objects.filter(sender_user=user).last().pk:
                isCreation = False
        else:
            isCreation = True
    else:
        return redirect('/basket')

    data = Ordering_page(request).getDict()

    if request.method == 'POST':
        form = Order_form(request.POST)
        if form.is_valid():
            if isCreation:
                order = Order(
                    sender_phone = form.cleaned_data['user_phone'],
                    sender_email = user.email_user_field,
                    sender_user = user,
                    receiver_name = form.cleaned_data['receiver_name'],
                    receiver_phone = form.cleaned_data['receiver_phone'],
                    receiver_additional_info = form.cleaned_data['receiver_additional_info'],
                    order_date = form.cleaned_data['order_date'],
                    order_time = form.cleaned_data['order_time'],
                    order_city = form.cleaned_data['order_city'],
                    order_address = form.cleaned_data['order_address']
                )
                order.save()
                orderCode = Order.objects.last().pk
                SelectedProducts.objects.filter(user=user).update(
                    order_code = orderCode
                )
            else:
                order = Order.objects.filter(user).last()
                order.sender_phone = form.cleaned_data['user_phone']
                order.sender_email = user.email_user_field
                order.sender_user = user
                order.receiver_name = form.cleaned_data['receiver_name']
                order.receiver_phone = form.cleaned_data['receiver_phone']
                order.receiver_additional_info = form.cleaned_data['receiver_additional_info']
                order.order_date = form.cleaned_data['order_date']
                order.order_time = form.cleaned_data['order_time']
                order.order_city = form.cleaned_data['order_city']
                order.order_address = form.cleaned_data['order_address']
                order.save()

            if user.phone_user_field != form.cleaned_data['user_phone']:
                user.phone_user_field = form.cleaned_data['user_phone']
                user.save(update_fields=["phone_user_field"])
            return redirect('/payment')
    else:
        form = Order_form(initial={
            'user_name': user.name_user_field,
            'user_email': user.email_user_field,
            'user_phone': user.phone_user_field,
            'order_date': datetime.date.today,
            'order_time': datetime.time,
            'order_city': user.city_user_field})

    data['form'] = form
    return render(request, 'flower/main/ordering.html', context=data)

def payment(request):
    if not request.session.session_key:
        request.session.create()

    auth = Authorization(request)
    if auth.isAuthorized() == False:
        return redirect('/account/login')
    
    if SelectedProducts.objects.filter(user=auth.getAuthorizedUser()).exists() == False:
        return redirect('/basket')

    data = Payment_main_page( request).getDict()
    return render(request, 'flower/main/payment.html', context=data)

#--------------- main_cats_pages --------------------------

class FlowerShowCategory(DataMixin, ListView):
    model = Flower
    template_name = 'flower/main/main.html'
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
    template_name = 'flower/main/main.html'
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
    template_name = 'flower/main/main.html'
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
    template_name = 'flower/main/main.html'
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
                    if form.cleaned_data['email_user_field'] == user.email_user_field:
                        if form.cleaned_data['password_user_field'] == user.password_user_field:
                            User.objects.filter(pk=user.pk).update(sessionUNQid=request.COOKIES["csrftoken"])
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

    #------------------------------------------------------------------------------- logout
    elif section_name == 'logout':
        if auth.isAuthorized() == False:
            return redirect('/account/login')
        
        auth.logout()
        return redirect('/account/login')
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def review(request, product_id):    
    data = Review_page(request, product_id).getDict()
    user = Authorization(request).getAuthorizedUser()
    if request.method == 'POST':
        form = Review_form(request.POST)
        if form.is_valid():
            newReview = Review(
                grade = form.cleaned_data['grade'],
                description = form.cleaned_data['description'],
                author = user,
                product = Flower.objects.get(pk=product_id)
            )
            newReview.save()

            return redirect('/account/order')
    else:
        form = Review_form(initial={
            'user': user.name_user_field,
            'grade': 4
        })
    data['form'] = form
    return render(request, 'flower/main/review.html', context=data)

#----------------------------------- 404 ----------------------------------------

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#---------------------------- ajax material ----------------------------------------
def append(request):
    auth = Authorization(request)
    JsonData = {}
    if auth.isAuthorized():
        defProd = DefinitionProduct(auth.getAuthorizedUser())
        if request.POST.get('typeRequest', '') == 'addToSelectList':
            defProd.appendToSelectedList(request.POST.get("user_id", "none"))
            if request.POST.get('isRedirect', '') != 'false':
                JsonData['redirect'] = '/basket'
                JsonData['isRedirect'] = True
        elif request.POST.get('typeRequest', '') == 'addToFavoriteList':
            defProd.appendToLikedList(request.POST.get("user_id", "none"))
    else:
        JsonData['redirect'] = '/account/login'
        JsonData['isRedirect'] = True
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

def setReview(request):
    stroke = '/review/' + request.POST.get('productId', '')
    JsonData = {'redirect': stroke}
    return JsonResponse(JsonData)

def accountLists(request):
    auth = Authorization(request)
    if auth.isAuthorized():
        if request.POST.get('typeRequest', '') == 'choosen_short':
            return render(request, 'flower/form_pages/short_account_temps/acc_order_choosen_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        elif request.POST.get('typeRequest', '') == 'liked_short':
            return render(request, 'flower/form_pages/short_account_temps/acc_order_liked_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        elif request.POST.get('typeRequest', '') == 'purchased_short':
            return render(request, 'flower/form_pages/short_account_temps/acc_order_purchased_short.html', context=AccountlistsPages(request.POST.get('typeRequest', ''), request).getDict())
        else:
            return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def setSity(request):
    auth = Authorization(request)
    if auth.isAuthorized():
        return render(request, 'flower/form_pages/short_main_templates/city_choosen_short.html', context=City_stroke(request.POST.get('cityId', ''), request).getDict())
    else:
        return render(request, 'flower/form_pages/short_main_templates/city_choosen_short.html', context=City_stroke(1, request).getDict())

def getSity(request):
    auth = Authorization(request)
    JsonData = {'cityCurent': auth.getAuthorizedUser().city_user_field.name}
    return JsonResponse(JsonData)

def basketConfirm(request):
    selected_products_stroke = request.POST.get('selected_products', '')
    selected_products = json.loads(selected_products_stroke)
    if selected_products != '':
        user = Authorization(request).getAuthorizedUser()
        for element in selected_products:
            data = SelectedProducts.objects.get(user=user, product=Flower.objects.get(pk=int(element['product_id'])))
            data.count = element['count']
            data.save(update_fields=["count"])
        JsonData = {'redirect': '/ordering'}
    return JsonResponse(JsonData)

def pay(request):
    user = Authorization(request).getAuthorizedUser()
    productList = SelectedProducts.objects.filter(user=user)
    payMethod = request.POST.get('method', '')

    for selectProduct in productList:
        purchProduct = PurchasedProducts(
            product = selectProduct.product,
            count = selectProduct.count,
            user = user,
            status = OrderStatus.objects.get(code=0),
            order_code = Order.objects.filter(sender_user=user).last(),
            pay_method = payMethod
        )
        purchProduct.save()

        stockProduct = Flower.objects.get(pk=selectProduct.product.pk)
        stockProduct.count = stockProduct.count - selectProduct.count
        stockProduct.save(update_fields=["count"])

    productList.delete()
    JsonData = {'redirect': '/'}
    return JsonResponse(JsonData)
