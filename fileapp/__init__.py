from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
#Establish database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from fileapp import routes