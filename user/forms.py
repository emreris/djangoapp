from django import forms
from django.contrib import messages
from  django.contrib.auth.models import User
from django.db.models.expressions import Exists
from django.http import request

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget= forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=50, label = "E-mail")
    username = forms.CharField(max_length= 40,label= "Kullanıcı Adı")
    password = forms.CharField(max_length=20,label= "Parola",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor!")
        
        if User.objects.filter(username__iexact=username):
            raise forms.ValidationError('Bu kullanıcı adı kullanılıyor...')
            

        values = {
            "username" : username,
            "password" : password,

        }


