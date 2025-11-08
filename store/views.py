from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Product


# 🛍️ عرض جميع المنتجات
def product_list(request):
    """عرض قائمة جميع المنتجات المتاحة"""
    products = Product.objects.filter(is_active=True)
    context = {
        'products': products
    }
    return render(request, 'store-templates/product_list.html', context)


# 🛒 عرض تفاصيل المنتج
def product_detail(request, product_id):
    """عرض تفاصيل منتج محدد"""
    try:
        product = Product.objects.get(id=product_id, is_active=True)
    except Product.DoesNotExist:
        return render(request, 'store-templates/product_detail.html', {'error': 'المنتج غير موجود أو غير متاح.'})

    context = {
        'product': product
    }
    return render(request, 'store-templates/product_detail.html', context)
