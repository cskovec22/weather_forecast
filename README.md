# Проект "Прогноз погоды"

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)

## Описание проекта "Прогноз погоды"

Проект "Прогноз погоды" — сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

API для погоды: https://open-meteo.com/.

Образ на DockerHub: cskovec22/weather_forecast_backend.

## Запуск проекта локально

- Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:cskovec22/weather_forecast.git
cd weather_forecast
```

- Установите и активируйте виртуальное окружение:

  - Для Linux/macOS:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

  - Для Windows:

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

- Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Создайте файл .env в папке проекта, пример представлен в файле .env-example


- Перейдите в папку с файлом manage.py


- Примените миграции:
```
python manage.py makemigrations
python manage.py migrate
```

- Создайте суперпользователя:
```
python manage.py createsuperuser
```

- Запустите проект:
```
python manage.py runserver
```

### Автор:  
*Васин Никита*  
**email:** *cskovec22@yandex.ru*  
**telegram:** *@cskovec22*  
