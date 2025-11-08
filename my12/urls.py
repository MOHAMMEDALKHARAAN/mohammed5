from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔐 لوحة التحكم
    path('admin/', admin.site.urls),

    # 🧩 روابط التطبيقات الداخلية
    path('', include('core.urls')),              # الصفحة الرئيسية والمحتوى العام
    path('store/', include('store.urls')),       # المتجر والمنتجات
    path('accounts/', include('accounts.urls')), # تسجيل الدخول والحسابات
]

# 🖼️ عرض ملفات الوسائط (media) والملفات الثابتة (static) أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
