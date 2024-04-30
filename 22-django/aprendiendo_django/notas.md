
## Notas

### Instalaciones necesarias
* brew install pyenv-virtualenv
* pyenv install 3.10.0
* pyenv virtualenv 3.10.0 env
* pip install Django==3.0.5

### activar enviroment virtual
* pyenv activate env

### levantar app Django
* python manage.py runserver

### django sqlite
* crear models
* python manage.py makemigrations
* python manage.py sqlmigrate miapp 0001 - (nombre de la app y número de migración)
* python manage.py migrate