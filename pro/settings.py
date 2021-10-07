from pathlib import Path
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mnb+vf=6um&ivmxk6_fswoz7*+(96h*rcat(gl7ym9&vwhbd)2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'parler',
    'rest_framework',

]
from django.utils.translation import gettext_lazy as _
LANGUAGES=(
    ('uz',_("Uzbek")),
    ('en',_("English")),
    ('ru', _("Russia")),
)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
import os
ROOT_URLCONF = 'pro.urls'
TEMPLATE_DIR=os.path.join(BASE_DIR,"template")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'pro.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


PARLER_LANGUAGES={
    None:(
        {'code':'en'},
        {'code':'uz'},
        {'code': 'ru'},
    ),
    'default':{
        'fallbacks':['uz'],
        'hide_untranslated':False
    }
}



LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/' # URL для медии в шаблонах


STATIC_ROOT = os.path.join(BASE_DIR, 'static') # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/' # URL для шаблонов


STATICFILES_DIRS = (
os.path.join(BASE_DIR, 'staticfiles'),
)