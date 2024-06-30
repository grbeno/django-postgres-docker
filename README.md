## Django-Postgres-Docker basic-startproject example
---

- Open CLI
- `$ cd <project-directory>`
- `$ git clone https://github.com/grbeno/django-postgres-docker.git`
---
- Create .env into the project directory
    - Set variables: `SSL_REQUIRED=False` `DEBUG=True` `SECRET_KEY=<generate one with: $ python -c 'import secrets;print(secrets.token_urlsafe(38))'>`
---
- `$ docker build .`
- `$ docker-compose up -d`  # -d=detached mode; if something went wrong: `$ docker-compose logs` 
- `$ docker-compose exec web python manage.py makemigrations accounts`
- `$ docker-compose exec web python manage.py createsuperuser`  # create superuser to log into django admin
- `$ docker-compose down`  # stop docker-compose, if you are finished

### Developing the project
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Install packages/libs inside the activated virtual environment!
- `$ pip freeze > requirements.txt`  # update the dependency list
- `$ docker-compose up -d`
### Developing locally _(independently from docker)_
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Set `DATABASE_URL=postgres://postgres:<DB_PASSWORD>@localhost:5432/<DB_NAME>`  # 1. Installing postgres 2. Create database