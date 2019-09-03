from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.educate05.ru']

DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.mysql',
        	'NAME': config('DB_NAME'),
        	'USER': config('DB_USER'),
        	'PASSWORD':config('DB_PASSWORD'),
        	'HOST':config('DB_HOST'),
    		}
	}

STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'