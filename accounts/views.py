from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserProfile


# 🧾 إنشاء حساب جديد
def signup(request):
    """إنشاء حساب مستخدم جديد مع ملف شخصي"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # ✅ التحقق من مطابقة كلمتي المرور
        if password1 != password2:
            return render(request, 'accounts-templates/signup.html', {
                'error': 'كلمتا المرور غير متطابقتين.'
            })

        # ✅ التحقق من تكرار اسم المستخدم
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts-templates/signup.html', {
                'error': 'اسم المستخدم مستخدم بالفعل.'
            })

        # ✅ إنشاء المستخدم
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # ✅ إنشاء ملف شخصي مرتبط بالمستخدم الجديد
        UserProfile.objects.create(user=user)

        # ✅ إعادة التوجيه إلى صفحة تسجيل الدخول بعد النجاح
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
            return redirect('home')  # يعيد المستخدم إلى الصفحة الرئيسية بعد تسجيل الدخول
        else:
            return render(request, 'accounts-templates/login.html', {
                'error': 'بيانات الدخول غير صحيحة.'
            })

    return render(request, 'accounts-templates/login.html')


# 🚪 تسجيل الخروج
def logout_view(request):
    """تسجيل خروج المستخدم"""
    auth_logout(request)
    return redirect('home')
