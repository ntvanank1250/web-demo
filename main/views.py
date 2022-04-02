from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        print(current_user)
        return render(request, 'main/home.html', param)
    else:
       return render(request, 'main/login.html')
def superadmin(request):
    if request.session['user'] =='admin':
        return render(request, 'main/superadmin.html')
    else:
        return render(request, 'main/home.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=uname).count()>0:
           return render(request, 'main/signup.html', {'error_message': 'Username already exists'})
        else:
            user = User(username=uname, password = pwd )
            user.save()
            return redirect('main:login')
    else:
        return render(request,'main/signup.html')

def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        check_user = User.objects.filter(username=uname, password =pwd)
        if check_user:
            request.session['user'] = uname
            param = {'current_user': uname}
            return render(request, 'main/home.html',param)
        else:
            return render(request, 'main/login.html', {'error_message':'Please enter valid Username or Password'})

    return render(request, 'main/login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return render(request, 'main/login.html')
    return render(request, 'main/login.html')

def music(request):
    try:
        if 'user' in request.session:
            current_user = request.session['user']
            param = {'current_user': current_user}
            return render(request, 'main/music.html', param)
        else:
            return render(request, 'main/login.html')
    except:
        return render(request, 'main/home.html')