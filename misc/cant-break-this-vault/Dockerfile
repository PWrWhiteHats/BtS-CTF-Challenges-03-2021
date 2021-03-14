FROM python:3.8-slim as builder
COPY requirements.txt /app/requirements.txt
RUN useradd --create-home --shell /bin/false ctfuser \
    && chown ctfuser:ctfuser /app \
    && chown ctfuser:ctfuser /home/ctfuser
USER ctfuser
WORKDIR /app
RUN pip install --user -r requirements.txt
COPY ./challenge/ /app

FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install python3 gunicorn -y \
    && apt-get clean
COPY --from=builder /app /app
COPY --from=builder /home/ctfuser/.local /home/ctfuser/.local
RUN useradd --create-home --shell /bin/false ctfuser \
    && chown ctfuser:ctfuser /app \
    && chown ctfuser:ctfuser /home/ctfuser
USER ctfuser
ENV PATH=/home/ctfuser/.local/bin:$PATH
ENV PYTHONPATH=/home/ctfuser/.local/lib/python3.8/site-packages
ENV FLASK_HOST='0.0.0.0'
ENV FLASK_PORT=7331
EXPOSE 7331
WORKDIR /app
ENTRYPOINT gunicorn -c gunicorn.py app