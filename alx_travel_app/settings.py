# Celery Configuration
CELERY_BROKER_URL = "amqp://localhost"   # RabbitMQ default
CELERY_RESULT_BACKEND = "rpc://"

# Email Configuration (use console backend for testing)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "no-reply@alxtravel.com"

# Celery settings
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'rpc://'

# Email settings (using console backend for testing)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@alx-travel-app.com'

