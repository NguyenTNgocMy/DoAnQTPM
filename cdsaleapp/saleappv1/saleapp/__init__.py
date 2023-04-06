from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = '#%^&(*$%^&(78678675$%&^&$^%*&^%&*^'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/qlhs?charset=utf8mb4"\
                                        % quote('123456')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app)

cloudinary.config(cloud_name='deiwcqxrm', api_key='739231495468361', api_secret='dXknXdb6z1zmek0t9xFsvehTibc')
