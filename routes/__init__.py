from flask import Flask, session, g, logging, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from passlib.hash import sha256_crypt
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
CORS(app)

# Production database_uri
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Import routes
from routes import base_urls