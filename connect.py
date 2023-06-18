from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL Users
mysql = MySQL(app)
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'LinuxKU13'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'jublia'

mysql.init_app(app)