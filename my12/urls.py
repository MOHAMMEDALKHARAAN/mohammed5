from django.contrib import admin
from django.urls import path, include  # ← لإضافة include لتضمين روابط التطبيقات

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🧩 روابط التطبيقات الداخلية
    path('', include('core.urls')),           # الصفحة الرئيسية والمحتوى العام
    path('store/', include('store.urls')),    # المتجر والمنتجات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول والحسابات
]
