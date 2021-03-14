from flask import Flask, render_template, request
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

def get_coupons(form):
    coupons = list()
    mydb = mysql.connector.connect(
        host=os.getenv('mysql_host'),
        user=os.getenv('mysql_user'),
        password=os.getenv('mysql_pwd'),
        database=os.getenv('mysql_db')
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM coupons WHERE code = /*" + str(form['cid']).replace('*/', '') + "*/ '1234'")
    myresult = mycursor.fetchall()
    for x in myresult:
        coupons.append({
            'code': x[1],
            'value': x[2]
        })
    mycursor.close()
    return coupons

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(source=None):
    if request.method == "POST":
        coupons = get_coupons(request.form)
        if coupons == []:
            return render_template('list.html', error="Sorry, you didn't win")
        else:
            return render_template('list.html', coupons=coupons)
    elif request.method == "GET":
        if request.args.get('source') == '7331' and 'localhost' in request.headers.get('host'):
            with open(__file__, 'r') as r:
                return r.read().strip()
        elif request.args.get('source') == '7331' and 'localhost' not in request.headers.get('host'): 
            return "You are not my local host", 403
        else:
            return render_template('base.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7331)