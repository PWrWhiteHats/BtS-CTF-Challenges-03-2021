FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install -y mariadb-server \
        php php-mysql apache2 \
    && apt-get clean

ENV MYSQL_DATABASE test_db
ENV MYSQL_USER devuser
ENV MYSQL_PASSWORD devpass
ENV MYSQL_ROOT_PASSWORD root

WORKDIR /var/www/html
RUN rm index.html

COPY php/* ./
COPY db_init.sql /db_init.sql
COPY flag.txt /tmp/f
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod 700 /entrypoint.sh

EXPOSE 80
CMD /entrypoint.sh