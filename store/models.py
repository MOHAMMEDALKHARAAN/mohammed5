from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """فئات المنتجات"""
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name


class Product(models.Model):
    """المنتج"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="الفئة")
    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(default=0, verbose_name="المخزون")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")
    is_active = models.BooleanField(default=True, verbose_name="متاح للبيع")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class Order(models.Model):
    """الطلب"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="المستخدم")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="إجمالي السعر")
    status_choices = [
        ('pending', 'قيد المعالجة'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التسليم'),
        ('cancelled', 'ملغي'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending', verbose_name="الحالة")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


class OrderItem(models.Model):
    """عناصر الطلب"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر عند الطلب")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلبات"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
