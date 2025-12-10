
"""
Django settings for prueba2 project.
"""
from pathlib import Path
import os
from os import getenv
from dotenv import load_dotenv
from urllib.parse import urlparse

# Cargar las variables de entorno
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Seguridad y depuración ---
# Azure: Usar variable de entorno
SECRET_KEY = os.getenv('SECRET_KEY')

# Azure: True para ver errores en desarrollo/pruebas. False en producción real.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Azure: Permitir todos los hosts
ALLOWED_HOSTS = ['*']

# --- Apps ---
# Azure: Dominio confiable para HTTPS
CSRF_TRUSTED_ORIGINS = [os.getenv("DOMINIO")]



# --- Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pruapp',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prueba2.urls'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Usa carpeta global 'templates' si la tienes
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'prueba2.wsgi.application'

# --- Base de datos ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Validación de contraseñas ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internacionalización ---
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# --- Static ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Azure: Almacenamiento comprimido de estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media ---
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Clave primaria por defecto ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Redirecciones de autenticación ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'usuarios'
LOGOUT_REDIRECT_URL = 'login'
