from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

# إنشاء حساب جديد داخل المتجر
def register_user(request):
    """تسجيل عميل جديد في المتجر"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'store-templates/register.html', {'error': 'كلمتا المرور غير متطابقتين.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store-templates/register.html', {'error': 'اسم المستخدم موجود بالفعل.'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('store-login')

    return render(request, 'store-templates/register.html')


# تسجيل الدخول للمتجر
def login_user(request):
    """تسجيل دخول العميل"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'store-templates/login.html', {'error': 'بيانات الدخول غير صحيحة.'})

    return render(request, 'store-templates/login.html')
