from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from config import URL_DATABASE

app = Flask(__name__)

app.secret_key = 'secret key'

app.config["SQLALCHEMY_DATABASE_URI"] = (
    URL_DATABASE
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

app.register_blueprint(contacts)
