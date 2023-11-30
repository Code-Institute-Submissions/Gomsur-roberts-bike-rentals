# Robert's Bike Rentals

Welcome to Robert's Bike Rental. We have bikes of all sizes and accessories for you and your loved ones. Explore the local neighborhood in style & comfort on our bikes.

![Robert's Bike Rental](http://104.248.100.154/static/img/bike-shop-concept-with-bicycles.jpg)

Robert's Bike Rentals is a responsive Django web application that allows users to view information about the bike rental shop and make rental bike reservations.

Robert's Bike Rentals is hosted in the Digital Ocean Cloud for public use.

Click the link below to access Robert's Bike Rentals and the bike collection.

[Access Robert's Rental Bikes](http://104.248.100.154/)

## Robert's Bike Rentals Tech Stack

robert's rental bikes is built with the following technologies.

* `hosting` { digital-ocean ubuntu }

    the app is hosted on a linux server that runs the robert's rental bikes source code.

* `database` { postgres pgadmin4 }

    the app uses a postgres database. pgadmin is used to monitor and manage the postgres database.

* `backend` { django4 } 

    the app backend is django mvc.

* `interface` { html bootstrap bootswatch liquid }

    the app user interface is built html pages customized with liquid templating to render backend content.

## Robert's Bike Rentals Features & Goals

### Bike Rental Customer Goals

Features for end users of the robert's rental bikes django application:

    [`store info`] Guests can see bike rental store information

    [`store info`] Guests can see rental bike accessories

    [`accounts`] Guests can register a new account to reserve rental bikes

    [`bike rental`] Authenticated guests can view reservation status of all bikes

    [`bike rental`] Authenticated guests can reserve a rental bike

    [`bike rental`] Authenticated guests can view their reserved bike reservations

    [`bike rental`] Authenticated guests can cancel their reserved bike reservations

### Bike Rental Employee Goals

Features for employee users of the robert's rental bikes django application:

    [`crud`] Can manage rental bikes in the system

    [`crud`] Can manage bike reservations in the system

### Bike Rental Site Administrator Goals

Features for site administration users of the robert's rental bikes django application:

    [`cloud`] Can manage the resources in the digital ocean cloud

    [`linux`] Can manage the system processes on the linux server

    [`manage.py`] Can manage the store employee users in the django system

## Robert's Bike Rentals User Stories




### Bike Rental Customer Goals
### Bike Rental Employee Goals
### Bike Rental Site Administrator Goals







### Registered User Stories

### Authenticated User Stories

### Unregistered User Stories
### Administrative User Stories


### User Experience Stories

* As a **user** I can **want the site to be responsive** so that **I can view on different devices**.




    * As a **manager of the site** I can **login to the admin panel** so that **I can manage the site**.

    * As an **admin** I can **edit bike-reservations**


    * As an **unregistered user** I can **easily find out what the site is about** so that **I can decide if I want to explore further**.

    * As a **user** I can **view a home page** so that **I can understand what the site is about**.
    * As a **user** I can **view an about page** so that **I can see what the site is about**.

    * As a **user** I can **click a link on the reserve page** so that **I can make a reservation of a bike**.

    * As a **user** I can **make a reservation** so that **the reservation is saved**.
    * As a user I want to see what the site is about
    * As a user I want to easily navigate and find what im looking for

## Known Bugs

the following are bugs currently known within the robert's rental bikes application.

### new accounts can not view bikes to rent

on the first login for a new user, there are no bikes available to view or reserve.

Solution: The new user has to log out and then log back in. Then the bikes are available to view and manage.

## Deployment Digital Ocean Linux Server

Robert's Rental Bikes is hosted on an ubuntu linux server in the `Digital Ocean` cloud.

### Ubuntu Linux Server

The Ubuntu Linux Server has the following specs:

    ip address / 104.248.100.154

    os / ubuntu linux 22.04

    ram / 2 GiB

    cpu / 1 vCPU

    disk / 50 GiB

### Postgres Database

A postgress database is used for backend storage.

The postgress database uses docker compose to run:

```yaml
roberts-bike-rentals-postgres:
    container_name: roberts-bike-rentals-postgres
    image: postgres:14.1-alpine
    user: root
    environment:
        - POSTGRES_USER=robertsrentals
        - POSTGRES_DB=robertsbikerentals
        - POSTGRES_PASSWORD=roberts!bike!rentals
    ports:
        - "5432:5432"
```

running the docker-compose script to start the database.

```bash
docker-compose up
```

see the running docker containers on the linux server.

```bash
docker ps
```

### Deploying Robert's Rental Bike Application

The robert's rental bikes application is executed by pulling the robert's rental bikes source code from GitHub and executing the `quick-start.sh` script using the linux terminal.

```bash
sudo nohup ./quick-start.sh &
```

nohup runs the application in the background after disconnecting from the terminal. if you don't put nohup, then the app closes when you disconnect.

## Credits

image attribution

tutorials

bootswatch

dddd
## Quick Start Robert's Rental Bikes 

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
