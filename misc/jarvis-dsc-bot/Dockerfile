FROM python:3.8-slim as builder
COPY requirements.txt /app/requirements.txt
RUN useradd --create-home --shell /bin/false ctf \
    && chown ctf:ctf /app \
    && chown ctf:ctf /home/ctf
USER ctf
WORKDIR /app
RUN pip install --user -r requirements.txt
COPY ./challenge/ /app
COPY ./flag.txt /app/flag.txt
WORKDIR /app
ENTRYPOINT python3 bot.py