# Django app for Scotia Bank Hackaton

This is a basic application [Django - Python](https://www.djangoproject.com/) example
for [Google App Engine Flexible Environment](https://cloud.google.com/appengine) to administrate a providers inventory.

## Running locally

You can run locally using django's `manage.py`:

    $ python manage.py runserver

## Deployment & how the application runs on Google App Engine.

Follow the standard deployment instructions in
[the top-level README](../README.md). Google App Engine runs the application
using [gunicorn](http://gunicorn.org/) as defined by `entrypoint` in
[`app.yaml`](app.yaml). You can use a different WSGI container if you want, as
long as it listens for web traffic on port `$PORT` and is declared in
[`requirements.txt`](requirements.txt).

## Preliminaries

First, verify your python3 version

    $ python3 --version

if no version defined, then you need to install it. See (https://djangoforbeginners.com/initial-setup/) as an example.

## How this was created

This project was created using standard Django commands and pipenv:

    $ pip3 install pipenv
    $ pipenv shell
    $ pipenv install Django==2.0.3
    $ pipenv install djangorestframework
    $ pipenv install django-suit
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

In order to deploy to Google App Engine, we created a simple
[`app.yaml`](app.yaml).

## Database notice

This sample project uses Django's default sqlite database. This isn't suitable
for production as your application can run multiple instances and each will
have a different sqlite database. Additionally, instance disks are ephemeral,
so data will not survive restarts.

For production applications running on Google Cloud Platform, you have
the following options:

* Use [Cloud SQL](https://cloud.google.com/sql), a fully-managed MySQL database.
  There is a [Flask CloudSQL](../cloudsql) sample that should be straightfoward
  to adapt to Django.
* Use any database of your choice hosted on
  [Google Compute Engine](https://cloud.google.com/compute). The
  [Cloud Launcher](https://cloud.google.com/launcher/) can be used to easily
  deploy common databases.
* Use third-party database services, or services hosted by other providers,
  provided you have configured access.
