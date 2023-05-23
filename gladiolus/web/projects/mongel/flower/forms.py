from django import forms
from .models import *

from django.core.exceptions import ValidationError

class Login_form (forms.Form):
    email_user_field = forms.CharField(required=True, label='Логин')
    password_user_field = forms.CharField(required=True, label='Пароль', widget=forms.TextInput(attrs={'type':"password"}))

    def clean_email_user_field(self):
        users = User.objects.all()
        email = self.cleaned_data['email_user_field']

        tempCheck = False

        for user in users:
            if user.email_user_field == self.cleaned_data['email_user_field']:
                tempCheck = True
        
        if tempCheck is False:
            raise ValidationError('Пользователя с данным email не существует')
        return email
    
    def clean_password_user_field(self):
        password = self.cleaned_data['password_user_field']
        if len(password) < 5:
            raise ValidationError('Пароль должен содержать больше 5 символов')
    
        return password

class RegistrationPostForm (forms.Form):
    name_register_field = forms.CharField(required=True, label='Имя пользователя')
    email_register_field = forms.CharField(required=True, label='Логин')
    password_first_register_field = forms.CharField(required=True, label='Пароль', widget=forms.TextInput(attrs={'type':"password"}))
    password_second_register_field = forms.CharField(required=True, label='Повторите пароль', widget=forms.TextInput(attrs={'type':"password"}))

    def clean(self):
        password_1 = self.cleaned_data['password_first_register_field']
        password_2 = self.cleaned_data['password_second_register_field']
        if len(password_1) < 5:
            raise ValidationError('Пароль должен содержать больше 5 символов')
        if password_1 != password_2:
            raise ValidationError('Пароли должны совпадать')
    
    def clean_email_register_field(self):
        email = self.cleaned_data['email_register_field']
        users = User.objects.all()
        
        for user in users:
            if email == user.email_user_field:
                raise ValidationError('Пользователь с таким email уже зарегестрирован')
            
        return email
    
class Account_form (forms.Form):
    name_user_field = forms.CharField(required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'readonly-field', 'readonly': ''}))
    surname_user_field = forms.CharField(required=False, label='Фамилия пользователя')
    email_user_field = forms.CharField(required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'readonly-field', 'readonly': ''}))
    password_user_field = forms.CharField(required=True, label='Пароль', widget=forms.TextInput(attrs={'class': 'readonly-field', 'readonly': ''}))
    city_user_field = forms.ModelChoiceField(queryset=Cities.objects.all(), label='Город', required=False)
    phone_user_field = forms.CharField(required=False, label='Номер телефона')

class Comment_form (forms.Form):
    user = forms.CharField(required=True, label='Пользователь')
    product = forms.CharField(required=False, label='Товар')
    grade = forms.CharField(required=True, label='Оценка')
    comment = forms.CharField(required=True, label='Комментарий')

class Order_form (forms.Form):
    #----------------отправитель------------------------------
    user_phone = forms.CharField(required=True, label='Номер телефона отправителя', widget=forms.TextInput(attrs={'class': 'text-area'}))
    user_email = forms.CharField(required=False, label='Email отправителя', widget=forms.TextInput(attrs={'class': 'readonly-field text-area', 'readonly': ''}))
    user_name = forms.CharField(required=False, label='Имя отправителя', widget=forms.TextInput(attrs={'class': 'readonly-field text-area', 'readonly': ''}))

    #----------------получатель-------------------------------
    receiver_name = forms.CharField(required=False, label='Имя получателя', widget=forms.TextInput(attrs={'class': 'text-area'}))
    receiver_phone = forms.CharField(required=False, label='Номер телефона получателя', widget=forms.TextInput(attrs={'class': 'text-area'}))
    receiver_additional_info = forms.CharField(required=False, label='Уточнение адреса доставки', widget=forms.TextInput(attrs={'class': 'text-area'}))

    #-------------дата и время заказа-------------------------
    order_date = forms.DateField(required=False, label='Дата заказа', widget=forms.TextInput(attrs={'class': 'input-area'}))
    order_time = forms.TimeField(required=False, label='Время заказа', widget=forms.TextInput(attrs={'class': 'input-area'}))

    #--------------адрес доставки-----------------------------
    order_city = forms.ModelChoiceField(queryset = Cities.objects.all(), empty_label=None, required=False, label='Город доставки')
    order_address = forms.CharField(required=True, label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'input-area'}))
    
    ## номер заказа
    ## пользователь, в данном случае отправитель
    ## товары, в списке покупок будут иметь отдельные данные о номере заказа
