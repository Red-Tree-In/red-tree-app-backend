from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from the backend by N!'})

if __name__ == '__main__':
    app.run()