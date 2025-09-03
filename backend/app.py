# ~/backend_project/app.py
#from flask import Flask, jsonify

#app = Flask(__name__)

#@app.route('/status')
#def status():
#    return jsonify({"status": "Backend is running", "author": "Ahmed Abuzaid"})

#@app.route('/db')
#def db_check():
#    return jsonify({"db_status": "Not connected yet"})  # Will integrate later

#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port=5000)

from flask_cors import CORS
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
CORS(app)


# DB connection config
db_config = {
    'host': 'db-vm',     # IP of db-vm
    'user': 'ahmed',
    'password': 'ahmed',               # Empty by default for MariaDB
    'database': 'myapp'
}

@app.route('/status')
def status():
    return jsonify({"status": "Backend is running"})

@app.route('/users')
def get_users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

