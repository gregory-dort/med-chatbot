from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

#Connecting to SQLite Database
def get_db_connection():
    conn = sqlite3.connect('user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# Account Creation API
# Creates a hash to match with login credentials
@app.route('/api/create-account', methods = 'POST')
def create_account():
    data = request.json
    print("payload received", data)

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                       (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({
            "message": f"Account for {username} created successfully.",
            "received_payload": data
        })
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409

def add_user(username, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                   (username, hashed_password))
    conn.commit()
    conn.close()

# Login API
# Matches hashed password with info stored in SQLite database
@app.route('/api/login', methods = 'POST')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user['password'], password):
        return jsonify({"message": "Login Successful"})
    else:
        return jsonify({"message": "Invalid Credentials"}), 401

if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)