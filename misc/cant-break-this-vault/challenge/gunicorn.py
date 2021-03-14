import multiprocessing
import os

DEBUG = bool(os.getenv('DEBUG')) or False
HOST = os.getenv('FLASK_HOST') or '127.0.0.1'
PORT = os.getenv('FLASK_PORT') or 50000

bind = f"{HOST}:{PORT}"
# reload gunicorn after changes
reload = not(DEBUG)
# set number of workers based on CPU - good for production; for dev - 1
workers = 1 if DEBUG else (multiprocessing.cpu_count() * 2) + 1
worker_connections = 1000

accesslog = "-"
access_log_format = '%(t)s [GUNICORN] %(h)s %(l)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
loglevel = "debug" if DEBUG else "info"
capture_output = True
enable_stdio_inheritance = True