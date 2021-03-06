"""
Django settings for demo project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zty*m5%vhs&odlx&!!_y63p^un(4!_31h5h@*tqt&4!&$rt0c#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'nlp',
    'demo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMP_ROOT = os.path.join(BASE_DIR, 'temp')

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['nlp.wordgames.gr', 'localhost', 'nlpbuddy.io', 'www.nlpbuddy.io']

# from commons
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'errorlog': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'error.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'errorlog',],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import spacy

# this is used to display the language name
LANGUAGE_MAPPING = {
        'el': 'Greek',
        'en': 'English',
        'de': 'German',
        'es': 'Spanish',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'fr': 'French',
        'it': 'Italian',
        'nl': 'Dutch',
        'lt': 'Lithuanian',
}

# load any spaCy models that are installed
# this takes some time to load so doing it here and hopefully this improves performance

SUPPORTED_LANGUAGES = ['de', 'el', 'en', 'es', 'fr', 'it', 'nl', 'pt']

AVAILABLE_LANGUAGE_MODELS = {}
AVAILABLE_LANGUAGE_MODELS['de'] = ('de_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['el'] = ('el_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['en'] = ('en_core_web_md', 'en_core_web_sm',)
AVAILABLE_LANGUAGE_MODELS['es'] = ('es_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['fr'] = ('fr_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['it'] = ('it_core_news_md', 'it_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['nl'] = ('nl_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['pl'] = ('pl_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['pt'] = ('pt_core_news_sm',)
AVAILABLE_LANGUAGE_MODELS['lt'] = ('lt_core_news_sm',)

LANGUAGE_MODELS = {}
for language in SUPPORTED_LANGUAGES:
    for model in AVAILABLE_LANGUAGE_MODELS[language]:
        try:
            LANGUAGE_MODELS[language] = spacy.load(model) # (language)
            break
        except OSError:
            print('Warning: model {} not found.'.format(model))
            continue

# this is used for language identification. Loading here to avoid importing many times
import langid as LANG_ID
LANG_ID.set_languages(LANGUAGE_MODELS.keys())
DEBUG = False

# whether to allow to import text from URLs
# library python-readability fetches text from a URL 
# and BeautifulSoup parses/removes tags
ALLOW_URL_IMPORTS = True

try:
    from demo.private import *
except:
    pass
