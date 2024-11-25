from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)



if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)