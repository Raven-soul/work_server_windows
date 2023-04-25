from django import forms
from .models import *

class RegistrationPostForm (forms.Form):
    name = forms.CharField(max_length=255, label="Имя пользователя")
    email = forms.CharField(max_length=255, label="Адрес электронной почты")
    password = forms.CharField(max_length=255, label="Пароль пользователя")