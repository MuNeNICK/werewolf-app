from flask import *
from flask_login import *
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import json
import datetime
import time
from app import app, db


@app.login_manager.user_loader
def load_user(user_id):
    return User_info.query.get(user_id)

@app.route('/')
def index():
    return jsonify({"content": "あいうえお"})

@app.route('/chat')
def chat():
    return render_template('index.html')

@app.route('/pipe')
def pipe():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            time.sleep(1)
            message = ws.receive()
            if message is None:
                break
            datetime_now = datetime.datetime.now()
            data = {
                'time': str(datetime_now),
                'message': message
            }
            ws.send(json.dumps(data))
            print(message)
            print(data)
    return
