from flask import *
from flask_login import *
from app import app, db


@app.login_manager.user_loader
def load_user(user_id):
    return User_info.query.get(user_id)

@app.route('/')
def index():
    return jsonify({"content": "あいうえお"})

