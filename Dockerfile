FROM python:3.6.4-alpine3.7

RUN apk add --update curl gcc g++ git libffi-dev openssl-dev python3-dev \
    && rm -rf /var/cache/apk/*
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV PYTHONUNBUFFERED=1 ENVIRONMENT=pre APP_HOME=/microservice/
RUN mkdir $APP_HOME && adduser -S -D -H python

RUN chown -R python $APP_HOME
WORKDIR $APP_HOME
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install gevent==1.2.2 gunicorn==19.7.1
ADD . $APP_HOME

EXPOSE 8000
USER python

CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:8000", "project.wsgi"]