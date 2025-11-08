from pathlib import Path

# 📁 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 المفتاح السري (احفظه سريًا)
SECRET_KEY = 'django-insecure--gz&nmf&=pa95ownmr7bo&q0k1xrw77-hfxrl%co9+nx7j6n2t'

# 🚧 وضع التطوير
DEBUG = True

# 🌐 أسماء النطاقات المسموح بها
ALLOWED_HOSTS = []


# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🧱 تطبيقات المشروع الداخلية
    'core.apps.CoreConfig',
    'store.apps.StoreConfig',
    'accounts.apps.AccountsConfig',
]


# ⚙️ الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # لتفعيل اللغة والترجمة
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🔗 ملف العناوين الرئيسي
ROOT_URLCONF = 'my12.urls'


# 🖼️ إعداد القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 📁 تعريف مجلد القوالب العام
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🌐 تطبيق WSGI
WSGI_APPLICATION = 'my12.wsgi.application'


# 🗃️ قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 إعداد اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# 🌐 دعم اللغات المتعددة
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]


# 🗺️ موقع ملفات الترجمة (في حال الترجمة اليدوية)
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# 🗂️ إعداد الملفات الثابتة (CSS / JS / Images)
STATIC_URL = '/static/'                      # رابط الوصول إلى الملفات الثابتة
STATICFILES_DIRS = [BASE_DIR / 'static']     # مجلد ملفات المشروع أثناء التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'       # مجلد التجميع النهائي (يُنشأ عند نشر المشروع)


# 🖼️ إعداد ملفات الوسائط (الصور / الفيديو / الملفات المرفوعة)
MEDIA_URL = '/media/'                        # رابط الوصول للملفات
MEDIA_ROOT = BASE_DIR / 'media'              # مجلد تخزين الوسائط المرفوعة


# ⚙️ الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
