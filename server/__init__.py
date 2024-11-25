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

if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)