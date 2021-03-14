from flask import Blueprint, abort
import logging as log

logging = log.getLogger('gunicorn.error')

error = Blueprint('error', __name__)

@error.app_errorhandler(400)
def handle_400(error):
    logging.warning(error)
    return error.description or 'Bad request mate'

@error.app_errorhandler(500)
def handle_500(error):
    logging.error(error)
    return \
        """
        <p class="alert alert-warning text-center " id="res">
            What did you do? I'm now dying...
        </p>
        """