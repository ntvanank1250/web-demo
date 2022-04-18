from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Blog, Comment
from django.contrib import messages

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}  
        return render(request, 'main/home.html', param)
    else:
       return redirect('main:login')


def signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        repwd=request.POST.get('repwd')

        if User.objects.filter(username=uname).count()>0:
           return render(request, 'main/signup.html', {'error_message': 'Username already exists'})
        if pwd!=repwd:
            return render(request, 'main/signup.html', {'error_message1': 'password and repassword not same'})
        if uname=='':
            return render(request, 'main/signup.html', {'error_message2': 'User is must enter a username'})

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

def changepass(request):
    current_user = request.session['user']
    param = {'current_user': current_user}
    if request.method == "POST":
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        repass = request.POST.get('repass')
        check_user = User.objects.filter(username=current_user, password =oldpass)
        
        if newpass==repass:
            if check_user:
                new_pass=User.objects.get(username=current_user)
                new_pass.password=newpass
                new_pass.save()
                return redirect('main:home')
            else:
                return render(request, 'main/changepass.html', {'error_message':'old password incorrect'})

        else:
            return render(request, 'main/changepass.html', {'error_message':'password and repassword not same'})

    return render(request, 'main/changepass.html', param)

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


      

def blog(request):
    current_user = request.session['user']
    param = {'current_user': current_user}
    if 'user' in request.session:
        current_user = request.session['user']
        blogs = Blog.objects.order_by('-date')[:5]
        param = {'blogs':blogs,
        'current_user': current_user}
        return render(request, 'main/blog.html', param)
    else:
        return   redirect('main:home')
    

def blog_i(request,id):
    if 'user' in request.session:
        current_user = request.session['user']
        
        blog = Blog.objects.get(pk=id)
        comments = blog.comments.all().order_by('-date')[:10]
        param = {'comments':comments,'blog':blog,'current_user': current_user,}
        if request.method == "POST":
            _author=User.objects.get(username=current_user)
            _comment=request.POST.get('comment')
            comment_new = Comment(id_blog=blog, author = _author, comment = _comment)
            comment_new.save()
        return render(request, 'main/blog_i.html', param)
    else:
        return   redirect('main:login')


def add_blog(request):
    current_user = request.session['user']
    param = {'current_user': current_user}
    _author = User.objects.get(username=current_user)
    if request.method == "POST":
        _title = request.POST.get('title')
        _description = request.POST.get('description')
        _content=request.POST.get('content')
        if _title =='':
            return render(request,param,'main/add_blog.html', {'error_message': ' The title is not empty. '})
        else:
            blog = Blog(title =_title,author=_author, description = _description,content=_content )
            blog.save()
            return redirect('main:blog')
    else:
        return render(request,'main/add_blog.html',param)
