# microservices-django-scaffold
Barebones Python with Django Microservices

[![Build Status](https://travis-ci.org/python-microservices/microservices-django-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-django-scaffold)
[![Coverage Status](https://coveralls.io/repos/github/python-microservices/microservices-django-scaffold/badge.svg?branch=master)](https://coveralls.io/github/python-microservices/microservices-django-scaffold?branch=master)
[![Requirements Status](https://requires.io/github/python-microservices/microservices-django-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-django-scaffold/requirements/?branch=master)
[![Updates](https://pyup.io/repos/github/python-microservices/microservices-django-scaffold/shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-django-scaffold/)
[![Python 3](https://pyup.io/repos/github/python-microservices/microservices-django-scaffold/python-3-shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-django-scaffold/)


# Docker

Create and push the image

    docker build -t templatedjango -f Dockerfile .

Test the image:

    docker run -d -p 8000:8000 templatedjango