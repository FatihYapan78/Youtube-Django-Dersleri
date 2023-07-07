from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    users = User.objects.all() # for döngüsü kullan
    # user = User.objects.filter(first_name="fatih")  for döngüsü kullan
    # user = User.objects.get(id=1)  for döngüsü kullanmana gerek yok çünkü sadece bir bilgi çekiceksin.
    context={
        'users':users,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'topics-detail.html')

def TopicsListing(request):
    return render(request, 'topics-listing.html')





# USER 
def sendMail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        userinfo = Userinfo.objects.get(user=user)
        subject = 'PAROLA HATIRLATMA'
        message = "Merhaba :" + userinfo.user.first_name + " " + userinfo.user.last_name +  '\nPAROLAN: ' + userinfo.password
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('login')
    else:
        return render(request, 'user/şifreunutma.html')


def UserDeatil(request,uid):
    user = User.objects.get(id=uid)
    context={
        'user':user,
    }
    return render(request, 'User/Detay.html', context)







def Register(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        surname = request.POST.get("surname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            BuyukHarf = False
            Numara = False
            OzelKarakter = False
            for i in password:
                if i.isupper():
                    BuyukHarf = True
                if i.isnumeric():
                    Numara = True
            if BuyukHarf and Numara and len(password) >= 6:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(first_name = name, last_name = surname, username=username, email=email, password=password)
                        user.save()
                        userinfo = Userinfo(user=user, password=password)
                        userinfo.save()
                        return redirect('index')
                    else:
                        messages.warning(request, 'Bu E-Mail Kullanılıyor!!')
                        return redirect('register')
                else:
                    messages.warning(request, 'Bu Kullanıcı Adı Kullanılıyor!!')
                    return redirect('register')
            else:
                messages.warning(request, 'Şifreniz Büyük Harf veya Numara veya 6 karakterden kısadır!!')
                return redirect('register')
        else:
            messages.warning(request, 'Şifreleriniz Uyumsuz. Tekrar Deneyin!!')
            return redirect('register')
    return render(request, 'User/register.html')

def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        etisareti = False
        for i in username:
            if i == "@":
                etisareti = True
        if username[-4:] == ".com" and etisareti:
            try:
                user = User.objects.get(email=username)
                username = user.username
            except: 
                return redirect('login')
            
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı Adı veya E-Posta Adresi veya Şifreniz Yanlış!!!')
            return redirect('login')
    return render(request, 'User/login.html')

def Logout(request):
    logout(request)
    return redirect('index')