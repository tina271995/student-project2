from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flaskdb'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)