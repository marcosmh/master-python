
## Notas

### Instalaciones necesarias
* brew install pyenv-virtualenv
* pyenv install 3.10.0
* pyenv virtualenv 3.10.0 env
* pip install Django==3.0.5

### activar enviroment virtual
* pyenv activate env

### crear proyecto
* django-admin startproject proyecto_django

### crear apps
* python manage.py startapp mainapp

### levantar app Django
* python manage.py runserver

### django sqlite
* crear models
* python manage.py makemigrations
* python manage.py sqlmigrate pages 0001 - (nombre de la app y número de migración)
* python manage.py migrate

### consola django admin
* python manage.py createsuperuser

### instalar apps externas
* pip install django-ckeditor

### Configurar BD MYSQL
- brew link --force mysql-client
- echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.zshrc
- brew link --force mysql-client
- brew unlink mysql-client && brew link --force mysql-client
- echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.zshrc
- pip install mysqlclient