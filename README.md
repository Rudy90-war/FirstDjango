#FirstDjango_18052024
## Инструкция по развертыванию проекта
1. 'python3 -m venv django_venv'
2. 'source django_venv/bin/activate
3. 'pip install -r requirements.txt'
4. "python manage.py migrate

5. 'python manage.py runserver'
## Запуск ipython
python manage.py shell_plus --ipython

## Выгрузить данные из БД
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
## Загрузить данные из БД
python manage.py loaddata ./fixtures/items.json


##Дополнительно
1. Дополнение для шаблона Django
    install baptisteo
добавить в settings.json