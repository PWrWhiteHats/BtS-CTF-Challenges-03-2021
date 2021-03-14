FROM python:3.8-slim as builder
RUN apt update \
    && apt install default-libmysqlclient-dev gcc -y
COPY challenge/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --user -r requirements.txt
COPY ./challenge/ /app
COPY ./flag.txt /app

FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install python3 mariadb-server gunicorn -y \
    && apt-get clean
COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local
COPY ./entrypoint.sh /entrypoint.sh
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/root/.local/lib/python3.8/site-packages
RUN chmod 700 /entrypoint.sh
EXPOSE 7331
ENTRYPOINT /entrypoint.sh
