from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'topics-detail.html')

def TopicsListing(request):
    return render(request, 'topics-listing.html')



# USER 
def Register(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        surname = request.POST.get("surname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        user = User.objects.create_user(first_name = name, last_name = surname, username=username, email=email, password=password)
        user.save()
        return redirect('index')
    return render(request, 'User/register.html')

def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # yapanfatih78@gmail.com
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

    return render(request, 'User/login.html')

def Logout(request):
    logout(request)
    return redirect('index')