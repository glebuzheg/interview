# interview

клонировать репозиторий и перейти в папку
если не установлен pipenv выполнить в командной строке

создать базу данных postgresql и в settings_local изменить данные на свои
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
Далее установить зависимости.
pip instal pipenv

pipenv shell
pipenv install

python manage.py migrate

создать пользователя 
python manage.py createsuperuser

Запустить сервер.
python manage.py runserver


документация находится http://localhost:8000/docs/





