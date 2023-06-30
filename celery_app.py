import os
from celery import Celery

# Установка переменной окружения, указывающей Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soleseeker.settings")

# Создание экземпляра Celery
app = Celery("soleseeker")

# Загрузка настроек из файла settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматическое обнаружение и регистрация задач в приложениях Django
app.autodiscover_tasks()
