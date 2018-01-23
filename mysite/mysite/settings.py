"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-65s7k_r(af_fw!mfa%v1fu_ih#2m*wxdgh3%h^efl7f8km%t*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'donations.apps.DonationsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'mysite.urls'
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
		'social_django.context_processors.login_redirect',
	     ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
	#'social_core.backends.twitter.TwitterOAuth',
	'social_core.backends.facebook.FacebookOAuth2',
        #'social_core.backends.google.GoogleOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'mysite.wsgi.application'

AUTH_PROFILE_MODULE = 'donations.Profile'

# Social Authorization Keys

#SOCIAL_AUTH_TWITTER_KEY = 'yET3py5GJ1vGBLJ0QSax2qo7T'
#SOCIAL_AUTH_TWITTER_SECRET = '0UiyIRipax1TEeMMsaP3965rC7ySJ3oH0TcX8OoaZNgTdcm7ov'
SOCIAL_AUTH_FACEBOOK_KEY = '1994789397476438'
SOCIAL_AUTH_FACEBOOK_SECRET = '7c2c828ac8a71b6b1bb285291648003a'
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '384425961651-hojg1n8u23vlkrsv6eomu2cusndeqhod.apps.googleusercontent.com'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HSFa-jn9_s8CID8LZiYODcwq'

LOGIN_URL = 'login'
LOGOUT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/donations/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/donations/' #connect_to_profile/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

#SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#'https://www.googleapis.com/auth/userinfo.email',
#'https://www.googleapis.com/auth/userinfo.profile'
#]

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'public_profile',
    'user_birthday',
    'user_location'
]

#SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
#SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'donations.pipeline.connect_to_profile',
    'donations.pipeline.update_user_social_data',
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'charity_db',
        'USER': 'admin',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


#Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
