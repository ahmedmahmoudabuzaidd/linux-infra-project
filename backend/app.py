# ~/backend_project/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"status": "Backend is running", "author": "Ahmed Abuzaid"})

@app.route('/db')
def db_check():
    return jsonify({"db_status": "Not connected yet"})  # Will integrate later

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

