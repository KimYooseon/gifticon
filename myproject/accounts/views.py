from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from .models import Profile

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],email=request.POST['email'])
            auth.login(request,user)

            return redirect('home') #redirect로 바꿔
    return render(request,'signup.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home') #redirect로 바꿔
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')


@csrf_exempt
def logout(request):
    request.method = 'POST'
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home') #redirect로
    return render(request,'login.html')

@csrf_exempt
def change_pw(request):
    context={}
    if request.method == "POST":
        current_password = request.POST.get("origin_pw")
        user = request.user
        
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            print("############3")
            print(new_password)
            print(password_confirm )
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("home")
            else:
                context.update({'error': "새로운 비밀번호를 다시 확인해주세요"})
        else:
            context.update({'error': "현재 비밀번호가 일치하지 않습니다"})
    
    return render(request, 'change_pw.html',context)