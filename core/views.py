from django.shortcuts import render

def home(request):
    """عرض الصفحة الرئيسية للموقع"""
    return render(request, 'home.html')
