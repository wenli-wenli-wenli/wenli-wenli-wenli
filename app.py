from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# 允许跨域，你的网页是github.io域名，后台是render域名，必须开
socketio = SocketIO(app, cors_allowed_origins="*")

# 收到前端发来的chat消息，广播给全部人
@socketio.on('chat')
def handle_chat(text):
    print("收到消息：", text)
    socketio.emit('chat', text, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
