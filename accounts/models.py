from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """الملف الشخصي للمستخدم"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="المستخدم")
    phone = models.CharField(max_length=20, blank=True, verbose_name="رقم الجوال")
    address = models.CharField(max_length=255, blank=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, verbose_name="المدينة")
    postal_code = models.CharField(max_length=10, blank=True, verbose_name="الرمز البريدي")
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="الصورة الشخصية")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.user.username
