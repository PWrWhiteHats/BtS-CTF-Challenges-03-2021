from flask import Flask, render_template, request

import os

application = Flask(__name__)

@application.route('/', methods=['POST', 'GET'])
def index(source=None):
    if request.method == "POST":
        return "Nope"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=7331)