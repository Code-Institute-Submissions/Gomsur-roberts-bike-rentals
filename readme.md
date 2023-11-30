# Robert's Bike Rentals

Welcome to Robert's Bike Rental. We have bikes of all sizes and accessories for you and your loved ones. Explore the local neighborhood in style & comfort on our bikes.

![Robert's Bike Rental](http://104.248.100.154/static/img/bike-shop-concept-with-bicycles.jpg)

Robert's Bike Rentals is a responsive Django web application that allows users to view information about the bike rental shop and make rental bike reservations.

Robert's Bike Rentals is hosted in the Digital Ocean Cloud for public use.

[Access Robert's Rental Bikes](http://104.248.100.154/)

## Tech Stack

robert's rental bikes is built with the following technologies.

* `hosting` { digital-ocean ubuntu }

    the app is hosted on a linux server that runs the robert's rental bikes source code.

* `database` { postgres pgadmin4 }

    the app uses a postgres database. pgadmin is used to monitor and manage the postgres database.

* `backend` { django } 

    the app backend is django mvc.

* `interface` { html bootstrap bootswatch django-templating }

    the app user interface is built html pages customized with django templating to render backend content.

## User Stories

### Administrative User Stories

* As a **manager of the site** I can **login to the admin panel** so that **I can manage the site**.

* As an **admin** I can **edit bike-reservations**

### Registered User Stories

### Authenticated User Stories

### Unregistered User Stories

* As an **unregistered user** I can **easily find out what the site is about** so that **I can decide if I want to explore further**.


* As a **user** I can **view a home page** so that **I can understand what the site is about**.
* As a **user** I can **view an about page** so that **I can see what the site is about**.

* As a **user** I can **click a link on the reserve page** so that **I can make a reservation of a bike**.

* As a **user** I can **make a reservation** so that **the reservation is saved**.
* As a user I want to see what the site is about
* As a user I want to easily navigate and find what im looking for



### User Experience Stories

* As a **user** I can **want the site to be responsive** so that **I can view on different devices**.


## Known Bugs

[`seeing bikes with new account`] the first time a new user logs in, they do not see available bikes to manage. The new user has to log out and then log back in then the bikes are available to view and manage.

## Reserve A Bike Today!

http://104.248.100.154/static/img/close-up-bicycle-bell.jpg

Robert's Bike Rentals is online and ready for use.

Click the link below to access Robert's Bike Rentals and our bike collection.

[Robert's Rental Bikes](http://104.248.100.154/)

## Quick Start Robert's Rental Bikes 

You can run Robert's Rental Bikes at home. Follow the instructions below on an Ubuntu Linux server.

### pre-requisite / postgres database

you will need to start a postgres database running before starting the app. 

### clone the repo

get the code from github.

```bash
git clone https://github.com/Gomsur/roberts-bike-rentals.git
```

enter the repo directory.

```bash
cd directory-name
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

### install python deps

install python packages using pip.

```bash
sudo set -xe \
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

Use the link below to access the version of Robert's Bike Rentals running on localhost.

[Robert's Rental Bikes (localhost)](http://localhost:8000/)
