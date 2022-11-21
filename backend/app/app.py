from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
import pymysql
from flask_login import LoginManager, login_user

app = Flask(__name__)

app.config.from_object('config')


db = SQLAlchemy(app)

from models import user

login_manager = LoginManager()
login_manager.init_app(app)

import views

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
