from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# DB connection config
db_config = {
    'host': 'db-vm',       # DNS name of DB VM
    'user': 'ahmed',
    'password': 'ahmed',
    'database': 'myapp',
    'port': 3306
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
        users = cursor.fetchall()  # list of dicts
        cursor.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Flask listens on all interfaces
    app.run(host='0.0.0.0', port=5000)
