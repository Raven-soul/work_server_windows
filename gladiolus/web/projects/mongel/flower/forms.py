from django import forms
from .models import *

from django.core.exceptions import ValidationError

class User_form (forms.ModelForm):
    class Meta:
        model = User
        fields = ['email_user_field', 'password_user_field']
        widgets = {
            'password': forms.TextInput(attrs={'style': 'color:red;', 'type': 'password' })
        }

    def clean_password_user_field(self):
        password = self.cleaned_data['password_user_field']
        if len(password) < 5:
            raise ValidationError('Пароль должен содержать больше 5 символов')
    
        return password

class RegistrationPostForm (forms.Form):
    email_register_field = forms.CharField(required=True, label='Логин')
    password_first_register_field = forms.CharField(required=True, label='Пароль')
    password_second_register_field = forms.CharField(required=True, label='Повторите пароль')

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
            if email == user.email:
                raise ValidationError('Пользователь с таким email уже зарегестрирован')
            
        return email