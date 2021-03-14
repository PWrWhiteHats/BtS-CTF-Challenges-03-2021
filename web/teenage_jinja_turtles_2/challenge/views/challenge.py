from flask import Blueprint, render_template, render_template_string, request, abort
from geolocation import get_location_for
from ctf import Flag
import logging as log

logging = log.getLogger('gunicorn.error')

challenge = Blueprint('challenge', __name__)

@challenge.route("/")
def index():
    return render_template_string(render_template("app.html"))

@challenge.route("/location", methods=['PATCH'])
def weather():
    ip_unsanitized = request.args.get('ip') or None
    if ip_unsanitized is None:
        return abort(400, 'No ip parameter')
    else:
        ip = sanitize(ip_unsanitized)
        location = get_location_for(ip)
        try:
            template = render_template_string(render_template('results.html', ip=ip, location=location))
            return template
        except Exception as e:
            logging.error(e)
            abort(500)

# Just for debugging purposes TODO remove it
@challenge.route("/debug_it", methods=["DEBUG"])
def source():
    with open(__file__, 'r') as f:
        return f.read()

def sanitize(string):
    blacklist = ["__class__", "__subclasses__", "request[request.", "__", "|join", '[', ']' ] # Need to expand it, this is too dangerous
    for bad in blacklist:
        if bad in string:
            abort(400, f"No hacking here - { bad } is not allowed") 
    return string

# def check_object(ob):
#     if isinstance(ob, object):
#         return True
#     else
#         return False

# if __name__ == "__main__"
#     f = Flag()
#     print(check_object(f)) # Why is it true? Dunno, need to check it - TODO