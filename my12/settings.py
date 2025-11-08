from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--gz&nmf&=pa95ownmr7bo&q0k1xrw77-hfxrl%co9+nx7j6n2t'

DEBUG = True

ALLOWED_HOSTS = []

# 🔹 تعريف التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🧩 تطبيقات المشروع الداخلية
    'core',
    'store',
    'accounts',
]

# 🔹 الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # لتفعيل الترجمة واللغة
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔹 إعداد ملف URL الرئيسي
ROOT_URLCONF = 'my12.urls'

# 🔹 إعداد القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # لتخزين القوالب العامة هنا
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🔹 إعداد WSGI
WSGI_APPLICATION = 'my12.wsgi.application'

# 🔹 إعداد قاعدة البيانات (SQLite افتراضيًا)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 إعداد اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True

# 🔹 إعداد المسارات للملفات الثابتة والإعلامية
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🔹 الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
