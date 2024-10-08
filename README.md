## Django-Postgres-Docker basic-startproject example
---

__Open CLI__
```
cd <project-directory>
```
``` 
git clone https://github.com/grbeno/django-postgres-docker.git
```

__Create .env into the project directory__
```
# .env

SSL_REQUIRED=False
DEBUG=True
SECRET_KEY=  # $ python -c 'import secrets;print(secrets.token_urlsafe(38))'
``` 
__Build the docker file__
```
docker-compose build .
```
__Run in -d detached mode__
```
docker-compose up -d  
```
__See the logs if something went wrong__
```
docker-compose logs
```
__Migrate the accounts models to database__
```
docker-compose exec web python manage.py makemigrations accounts
```
__Create superuser to log into django admin__
```
docker-compose exec web python manage.py createsuperuser
```
__Stop docker-compose, if you are finished__
```
docker-compose down
```

### Developing the project using Docker
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Install packages/libs in the scope of the activated virtual environment!\
  `pip/pipenv install <any-package/library>`
- Update the dependency list
```
pip freeze > requirements.txt
```
```
docker-compose up -d
```
### Developing locally _(independently from Docker)_
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Set `DATABASE_URL=postgres://postgres:<DB_PASSWORD>@localhost:5432/<DB_NAME>`
    - Installing postgres
    - Create database using CLI or pgAdmin
