from flask import Flask, template_rendered
from decouple import config
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(user = config('USER_DB'), passwd = config('PASSWD_DB'), db = config('DB'))
sql = db.cursor()
app.config.from_object('config')

from .routes import index, users