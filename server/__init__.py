from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

@app.route('/api/create-account', methods = 'POST')
def create_account():
    data = request.json
    print("payload received", data)

    username = data.get('username')
    password = data.get('password')

    if username and password:
        return jsonify(
            {
            "message": f"Account for {username} created successfully.",
            "received_payload": data
            })
    else:
        return jsonify({"error": "Invalid input"}), 400    

@app.route('/api/login', methods = 'POST')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Invalid input"}), 400
    
    if username == 'user' and password == 'password':
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)