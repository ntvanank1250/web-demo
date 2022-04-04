from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        if current_user=='admin11':
            mode_user="admin11"
            param = {'current_user': current_user,
                "mode_user":mode_user}
        else:
            param = {'current_user': current_user}
        print(current_user)
        return render(request, 'main/home.html', param)
    else:
       return render(request, 'main/login.html')
def superadmin(request):
    try:
        if 'user' in request.session:
            current_user = request.session['user']
           
            param = {'current_user': current_user}
            return render(request, 'main/superadmin.html', param)
        else:
            return render(request, 'main/login.html')
    except:
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
            return redirect('main:home')
        else:
            return render(request, 'main/login.html', {'error_message':'Please enter valid Username or Password'})

    return render(request, 'main/login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('main:login')
    return redirect('main:login')

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

def game(request):
    try:
        if 'user' in request.session:
            current_user = request.session['user']
            param = {'current_user': current_user}
            return render(request, 'main/game.html', param)
        else:
            return render(request, 'main/login.html')
    except:
        return render(request, 'main/home.html')

def gamesnake(request):
    try:
        if 'user' in request.session:
            current_user = request.session['user']
            param = {'current_user': current_user}
            return render(request, 'main/gamesnake.html', param)
        else:
            return render(request, 'main/login.html')
    except:
        return render(request, 'main/game.html')

def chatbox(request):
    try:
        if 'user' in request.session:
            current_user = request.session['user']
            param = {'current_user': current_user}
            return render(request, 'main/movies.html', param)
        else:
            return render(request, 'main/login.html')
    except:
        return render(request, 'main/home.html')
