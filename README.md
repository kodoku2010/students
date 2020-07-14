### Students
#### Technologies: Python, Django
###### Сайт для регистрации абитуриентов. Cостоит из 2 страниц: список зарегистрированных абитуриентов (главная страница) и форма ввода информации о студенте.
Для запуска приложения: открываем терминал, переходим в дерикторию проекта и выполняем следующие команды:

`pip install -r requirements.txt`

`python3 students/manage.py migrate --run-syncdb`

`python3 students/manage.py makemigrations`

`python3 students/manage.py runserver`

Далее открываем в браузере следующую страницу http://127.0.0.1:8000/.