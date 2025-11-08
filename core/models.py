from django.db import models

class SiteSetting(models.Model):
    """إعدادات عامة للموقع"""
    site_name = models.CharField(max_length=150, verbose_name="اسم المتجر")
    logo = models.ImageField(upload_to='logo/', null=True, blank=True, verbose_name="شعار المتجر")
    contact_email = models.EmailField(verbose_name="البريد الإلكتروني للتواصل", blank=True)
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف", blank=True)
    address = models.CharField(max_length=255, verbose_name="العنوان", blank=True)
    about_text = models.TextField(verbose_name="عن المتجر", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name
