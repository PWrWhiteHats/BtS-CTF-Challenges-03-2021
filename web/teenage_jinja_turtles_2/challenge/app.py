from flask import Flask
from views.challenge import challenge
from views.errors import error
import os
import logging 

logging.getLogger('gunicorn.error')

IS_PROD = bool(os.getenv('PROD')) or False
HOST = os.getenv('FLASK_HOST') or '127.0.0.1'
PORT = os.getenv('FLASK_PORT') or 5000

application = Flask(__name__)
application.register_blueprint(challenge)
application.register_blueprint(error)

if __name__ == "__main__":
    application.run(debug=not(IS_PROD), port=PORT, host=HOST)