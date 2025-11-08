from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='store-register'),
    path('login/', views.login_user, name='store-login'),
]
