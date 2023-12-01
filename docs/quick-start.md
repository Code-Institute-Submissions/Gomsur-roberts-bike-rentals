## Quick Start Installation

You can run Robert's Rental Bikes at home. Follow the instructions below on an Ubuntu Linux server.

### pre-requisite / postgres database

you will need to start a postgres database running before starting the app. 

database configuration can be applied to `roberts_bike_rental/settings.py`.

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

### open the app in the browser

Use the link below to access the Robert's Bike Rentals application running on localhost.

[Robert's Rental Bikes (localhost)](http://localhost:8000/)
