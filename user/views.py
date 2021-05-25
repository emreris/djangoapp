from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        newUser = User(username =username,email = email)
        newUser.set_password(password)
        

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz.")

        return redirect("index")
    context = {
        "form" : form
    }

    return render(request,"register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı...")

            return render(request,"login.html",context)

        else:    
            messages.success(request,"Başarıyla giriş yapıldı")
            login(request,user)
            return redirect("index")
        

    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış yapıldı.")
    return redirect("index")


