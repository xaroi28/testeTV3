from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display():
    return render_template('display.html')

@socketio.on('send_text')
def handle_send_text(data):
    emit('receive_text', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
