## Django-Postgres-Docker basic-startproject example
---

- Open CLI
```
cd <project-directory>
```
``` 
git clone https://github.com/grbeno/django-postgres-docker.git
```
---
- Create .env into the project directory

    ```
    # .env
    
    SSL_REQUIRED=False
    DEBUG=True
    SECRET_KEY=  # <generate one with: $ python -c 'import secrets;print(secrets.token_urlsafe(38))'>
    ```
---

- Build the docker file
```
docker build .
```
- If something went wrong to see the logs use -d detached mode.
```
docker-compose up -d  
```
- See the logs if not in detached mode
```
docker-compose logs
```
- Migrate the accounts models to database
```
docker-compose exec web python manage.py makemigrations accounts
```
- Create superuser to log into django admin
```
docker-compose exec web python manage.py createsuperuser
```
- Stop docker-compose, if you are finished
```
docker-compose down
```

### Developing the project
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Install packages/libs inside the activated virtual environment!
- Update the dependency list
```
pip freeze > requirements.txt
```
```
docker-compose up -d
```
### Developing locally _(independently from docker)_
---
- Set virtual environment to manage package and project dependencies: `venv` or `pipenv` ...
- Set `DATABASE_URL=postgres://postgres:<DB_PASSWORD>@localhost:5432/<DB_NAME>`  # 1. Installing postgres 2. Create database
