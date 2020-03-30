from flask import Flask
from flask import *
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from flask import request
from flask_mail import Mail, Message
from random import *
from datetime import *
import time
import os
import string
import requests
from datetime import datetime

app = Flask(__name__)
mail = Mail(app)
app.secret_key = os.urandom(34)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'developer.websupp@gmail.com'
app.config['MAIL_PASSWORD'] = 'PRLvikramsarabhairoom'
app.config['MAIL_DEFAULT_SENDER'] = 'developer.websupp@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'portfolio'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
connection = mysql.connect()
	

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def portfolio():
	return render_template("portfolio.htm.j2")

@app.route('/login/')
def login():
	return 'Madhav'



app.jinja_env.cache = {}
if __name__ == '__main__':
	app.run(host='0.0.0.0',port='3030',debug = True)