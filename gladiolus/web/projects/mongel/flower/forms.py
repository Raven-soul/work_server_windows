from django import forms
from .models import *

from django.core.exceptions import ValidationError

class AuthorizationPostForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.TextInput(attrs={'style': 'color:red;', 'type': 'password' })
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise ValidationError('Пароль должен содержать больше 5 символов')
    
        return password

class RegistrationPostForm (forms.ModelForm):
    class Meta:
        model = Register_form
        fields = ['name', 'email', 'password_first', 'password_second']
        widgets = {
            'password_first': forms.TextInput(attrs={'type': 'password' }),
            'password_second': forms.TextInput(attrs={'type': 'password' })
        }

    def clean(self):
        password_1 = self.cleaned_data['password_first']
        password_2 = self.cleaned_data['password_second']
        if len(password_1) < 5:
            raise ValidationError('Пароль должен содержать больше 5 символов')
        if password_1 != password_2:
            raise ValidationError('Пароли должны совпадать')
    
        return password_1
    
    def clean_email(self):
        email = self.cleaned_data['email']
        users = User.objects.all()
        for user in users:
            if email == user.email:
                raise ValidationError('Пользователь с таким email уже зарегестрирован')
            
        return email