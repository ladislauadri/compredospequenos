"""
Django settings for compredospequenos project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qlbowqum_#094z5q5g1i=k*b%w@u-l*-g4#0+=9&$h=m2^csqt'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','31.220.53.16','localhost','pequenosemcrise.com.br','www.pequenosemcrise.com.br','api.pequenosemcrise.com.br', 'condominiosevizinhanca.com.br', 'api.condominiosevizinhanca.com.br']


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'model_clone',



    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    

    'django_extensions',
    'django_comments',
    'widget_tweaks',
    'crispy_forms',
    'django_select2',
    'smart_selects',
    'ckeditor' ,
    'ckeditor_uploader',
    'fontawesome_5',
    'django_gravatar',
    'bootstrap_datepicker_plus',
    'taggit',
    'taggit_selectize',
    'django_filters',
    'rest_framework',
    'corsheaders',
    'cloudinary',
    'ipware',
    'mptt',
    'ads',
    'django_node_assets',

    'api',
    'locais',
    'homepage',
    'hitcount',
    'contas',
    'localidades',
    'dashboard',
    'paginas',
    'blog',
    'issueTracker',
    'condominiosevizinhanca',
    'accounts',
    'posts',
]

SITE_ID = 0


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',



]
MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)


ROOT_URLCONF = 'compredospequenos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'compredospequenos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'vmedia',
        'USER': 'viviremedia',
        'PASSWORD': 'packperry',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static" ),
]
STATICFILES_FINDERS = [
    'django_node_assets.finders.NodeModulesFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL =  'home'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    # … default cache config and others
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "default"

CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_ALLOW_NONIMAGE_FILES = False


TAGGIT_TAGS_FROM_STRING = 'taggit_selectize.utils.parse_tags'
TAGGIT_STRING_FROM_TAGS = 'taggit_selectize.utils.join_tags'

TAGGIT_SELECTIZE = {
    'MINIMUM_QUERY_LENGTH': 2,
    'RECOMMENDATION_LIMIT': 10,
    'CSS_FILENAMES': ("taggit_selectize/css/selectize.django.css",),
    'JS_FILENAMES': ("taggit_selectize/js/selectize.js",),
    'DIACRITICS': True,
    'CREATE': True,
    'PERSIST': True,
    'OPEN_ON_FOCUS': True,
    'HIDE_SELECTED': True,
    'CLOSE_AFTER_SELECT': False,
    'LOAD_THROTTLE': 300,
    'PRELOAD': False,
    'ADD_PRECEDENCE': False,
    'SELECT_ON_TAB': False,
    'REMOVE_BUTTON': False,
    'RESTORE_ON_BACKSPACE': False,
    'DRAG_DROP': False,
    'DELIMITER': ','
}


CKEDITOR_CONFIGS = {
    'default': {
        #'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'Embed',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'uploadimage', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        #             {
        #     'name': 'VideoDetector',
        #     'items': ['videodetector',]
        # },
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'embed',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            # 'videodetector',
        ]),
    }
}

CLOUDINARY = {
    'cloud_name' : 	'viviremedia',
    'api_key' : '276821978118549',
    'api_secret': 'hOcrKtVAlDyP54dxzq1mixqiwU0'
}
CORS_ORIGIN_ALLOW_ALL = False # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3001',
] # If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:3001', 
]

IPWARE_META_PRECEDENCE_ORDER = (
    'HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR',  # <client>, <proxy1>, <proxy2>
    'HTTP_CLIENT_IP',
    'HTTP_X_REAL_IP',
    'HTTP_X_FORWARDED',
    'HTTP_X_CLUSTER_CLIENT_IP',
    'HTTP_FORWARDED_FOR',
    'HTTP_FORWARDED',
    'HTTP_VIA',
    'REMOTE_ADDR',
)


ADS_GOOGLE_ADSENSE_CLIENT = None  # 'ca-pub-xxxxxxxxxxxxxxxx'

ADS_ZONES = {
    'header': {
        'name': _('Header'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        },
        'google_adsense_slot': None,  # 'xxxxxxxxx',
        'google_adsense_format': None,  # 'auto'
    },
    'content': {
        'name': _('Content'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        },
        'google_adsense_slot': None,  # 'xxxxxxxxx',
        'google_adsense_format': None,  # 'auto'
    },
    'sidebar': {
        'name': _('Sidebar'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        }
    }
}

ADS_DEFAULT_AD_SIZE = '720x150'

ADS_DEVICES = (
    ('xs', _('Extra small devices')),
    ('sm', _('Small devices')),
    ('md', _('Medium devices (Tablets)')),
    ('lg', _('Large devices (Desktops)')),
    ('xl', _('Extra large devices (Large Desktops)')),
)

ADS_VIEWPORTS = {
    'xs': 'd-block img-fluid d-sm-none',
    'sm': 'd-none img-fluid d-sm-block d-md-none',
    'md': 'd-none img-fluid d-md-block d-lg-none',
    'lg': 'd-none img-fluid d-lg-block d-xl-none',
    'xl': 'd-none img-fluid d-xl-block',
}


AUTH_USER_MODEL = 'accounts.CustomUser'


NODE_PACKAGE_JSON = '/var/django/compredospequenos/package.json'
NODE_MODULES_ROOT = '/var/django/compredospequenos/node_modules'
NODE_PACKAGE_MANAGER_EXECUTABLE = '/usr/local/bin/npm'
