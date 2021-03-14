FROM python:3.8-slim as builder
COPY requirements.txt /app/requirements.txt
RUN useradd --create-home --shell /bin/false ctf \
    && chown ctf:ctf /app \
    && chown ctf:ctf /home/ctf
USER ctf
WORKDIR /app
RUN pip install --user -r requirements.txt
COPY ./challenge/ /app

FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install python3 gunicorn -y \
    && apt-get clean
RUN useradd --create-home --shell /bin/false ctf \
    && mkdir /app && chown ctf:ctf /app \
    && chown ctf:ctf /home/ctf
COPY --from=builder /app /app
COPY --from=builder /home/ctf/.local /home/ctf/.local
USER ctf
ENV PATH=/home/ctf/.local/bin:$PATH
ENV PYTHONPATH=/home/ctf/.local/lib/python3.8/site-packages
ENV FLASK_HOST='0.0.0.0'
ENV FLASK_PORT=7331
EXPOSE 7331
WORKDIR /app
COPY flag.txt /app/flag.txt
ENTRYPOINT gunicorn -c /app/gunicorn.py app
