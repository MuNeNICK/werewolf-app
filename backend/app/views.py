from flask import *
from flask_login import *
from flask_socketio import SocketIO, send, emit
from app import app, db, socketio


@app.login_manager.user_loader
def load_user(user_id):
    return User_info.query.get(user_id)

@app.route('/')
def index():
    return jsonify({"content": "あいうえお"})

@app.route('/aaa')
def aaa():
    return render_template('index.html')

user_count = 0
text = ""


# ユーザーが新しく接続すると実行
@socketio.on('connect')
def connect(auth):
    global user_count, text
    user_count += 1
    # 接続者数の更新（全員向け）
    emit('count_update', {'user_count': user_count}, broadcast=True)
    # テキストエリアの更新
    emit('text_update', {'text': text})

# ユーザーの接続が切断すると実行
@socketio.on('disconnect')
def disconnect():
    global user_count
    user_count -= 1
    # 接続者数の更新（全員向け）
    emit('count_update', {'user_count': user_count}, broadcast=True)


# テキストエリアが変更されたときに実行
@socketio.on('text_update_request')
def text_update_request(json):
    global text
    text = json["text"]
    # 変更をリクエストした人以外に向けて送信する
    # 全員向けに送信すると入力の途中でテキストエリアが変更されて日本語入力がうまくできない
    emit('text_update', {'text': text}, broadcast=True, include_self=False)
