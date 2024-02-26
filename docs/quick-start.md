## Quick Start Installation

You can run Robert's Rental Bikes at home. Follow the instructions below on an Ubuntu Linux server.

![Robert's Bike Rental](http://104.248.100.154/static/img/bike-shop-concept-with-bicycles.jpg)

### SQLite database

you will need to start a SQLite database running before starting the app. A SQLite database is used for backend storage.

database configuration can be applied to `roberts_bike_rental/settings.py`.

The SQLite database uses docker compose to run:

```yaml
version: "3"

services:
  roberts-bike-rentals-sqlite:
    container_name: roberts-bike-rentals-sqlite
    image: python:3.9-alpine  # Using Python image with SQLite support
    restart: always
    command: >
      /bin/sh -c "python manage.py migrate &&
                  python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    volumes:
      - ./roberts-bike-rentals:/app  # Mount your Django project directory
    environment:
      - DJANGO_SECRET_KEY=your_secret_key_here
      - DJANGO_DEBUG=True  # Set to False in production
      - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
      - DJANGO_DB_ENGINE=django.db.backends.sqlite3
      - DJANGO_DB_NAME=/app/db.sqlite3  # Path to SQLite database file           
```

running the docker-compose script to start the database.

```bash
docker-compose up -d
```

see the running docker containers on the linux server.

```bash
docker ps
```
### clone the repo

get the code from github.

```bash
git clone https://github.com/Gomsur/roberts-bike-rentals.git
```

enter the repo directory.

```bash
cd roberts-bike-rentals
```

### update os packages

update apt packages.

```bash
sudo apt-get update;
```

### install pip

install pip a tool for installing and managing python packages.

```bash
sudo apt install -y python3-pip;
```

### install python packages

install python packages using pip.

```bash
set -xe \
     && pip install 'Django<4.0' \
     && pip install djangorestframework \
     && pip install django-cors-headers \
     && pip install psycopg2-binary \
     && pip install Pillow \
     && pip install django-rest-auth-forked
```

### make migrations

```bash
python3 manage.py makemigrations
```

### apply migrations

```bash
python3 manage.py migrate
```

### start the app

```bash
python3 manage.py runserver 0.0.0.0:8000
```

### create super user

```bash
python3 manage.py createsuperuser
```

### open the app in the browser

Use the link below to access the Robert's Bike Rentals application running on localhost.

The server is running at the following ip address: `http://localhost:8000/`

[Robert's Rental Bikes (localhost)](http://localhost:8000/)
