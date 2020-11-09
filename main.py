from flask_socketio import SocketIO
from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('home.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><h3>You have entered a wrong URL.</h3>", 404


if __name__ == '__main__':
    socketio.run(app, debug=True)


