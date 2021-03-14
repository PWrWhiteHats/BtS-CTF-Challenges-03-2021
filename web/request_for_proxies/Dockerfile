FROM php:rc-apache
RUN mkdir /app
WORKDIR /app
COPY ./httpd.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./entrypoint.sh /app
COPY main_webapp /app/main_webapp
COPY flag_webapp /app/flag_webapp

EXPOSE 80
WORKDIR /app