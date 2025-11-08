from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile

# 🧾 إنشاء حساب جديد
def signup(request):
    """إنشاء حساب مستخدم جديد مع ملف شخصي"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts-templates/signup.html', {'error': 'كلمتا المرور غير متطابقتين.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts-templates/signup.html', {'error': 'اسم المستخدم مستخدم بالفعل.'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # إنشاء ملف شخصي مرتبط بالمستخدم
        UserProfile.objects.create(user=user)

        return redirect('accounts-login')

    return render(request, 'accounts-templates/signup.html')


# 🔐 تسجيل الدخول
def login_view(request):
    """تسجيل دخول المستخدم"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts-templates/login.html', {'error': 'بيانات الدخول غير صحيحة.'})

    return render(request, 'accounts-templates/login.html')
