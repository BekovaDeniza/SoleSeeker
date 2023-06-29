# Установка базового образа Python
FROM python:3.9

# Установка переменной среды PYTHONUNBUFFERED для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории внутри контейнера
WORKDIR /SoleSeeker

# Копирование файла requirements.txt в контейнер
COPY requirements.txt /SoleSeeker/

# Установка зависимостей проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта в контейнер
COPY . /SoleSeeker/

# Запуск команды collectstatic при сборке контейнера
RUN python manage.py collectstatic --noinput

# Открытие порта для веб-сервера Django
EXPOSE 8000

# Запуск команды для запуска сервера Django
CMD python manage.py runserver 0.0.0.0:8000
