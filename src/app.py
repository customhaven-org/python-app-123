from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route("/api/v1/details")
def details():
    return "<h1>Hello World!</h1>"

@app.route('/api/v1/infos')
def infos():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! I am the robot coming for you!',
        "another message": "Another message for you!",
        "third message": "More message!",
        "forth message": "yet another message",
        "fifth message": "five messages",
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "deployed_on": "kubernetes",
        "env": "dev",
        "app_name": "python-app-123"
    })

@app.route('/api/v1/healthz')
def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")