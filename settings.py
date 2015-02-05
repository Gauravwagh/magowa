"""
Django settings for magowa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3s9(b5w!yxd9-e)#wtyfxnu-ii_za*k)#)qiw2#q7c)(vp^vo7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'easy_pdf',
)
OUR_APPS = (
            'home',
            
)
INSTALLED_APPS +=OUR_APPS
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR+'/sqlite.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

MEDIA_ROOT = BASE_DIR+'/templates/media'

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
                 BASE_DIR+'/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static/')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (

                         BASE_DIR + '/templates',

)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Magowa Enterprise',
    'HEADER_DATE_FORMAT': 'l, j. F Y', # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',       # 18:42
    'SHOW_REQUIRED_ASTERISK': True,
    
    'SEARCH_URL': '/admin/user',

    # Parameter also accepts url name
    'SEARCH_URL': 'admin:auth_user_changelist',

    # Set to empty string if you want to hide search from menu
    'SEARCH_URL': '',
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        },
    'MENU': (

        # Keep original label and models
        'sites',

        # Rename app and set icon
        {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},

        # Reorder app models
        {'app': 'auth', 'models': ('user', 'group')},

        # Custom app, with models
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},

        # Cross-linked models with custom name; Hide default icon
        {'label': 'Custom', 'icon':None, 'models': (
            'auth.group',
            {'model': 'auth.user', 'label': 'Staff'}
        )},

        # Custom app, no models (child links)
        {'label': 'Users', 'url': 'auth.user', 'icon':'icon-user'},

        # Separator
        '-',

        # Custom app and model with permissions
        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        ]},
    )
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'waghgaurav.g@gmail.com'
EMAIL_HOST_PASSWORD = 'Taj@everycrave'
EMAIL_USE_TLS = True

ACCOUNT_ACTIVATION_DAYS = 2
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/home/home/'