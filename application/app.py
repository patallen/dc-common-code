from flask import Flask, jsonify
from common.message import generate_message

app = Flask(__name__)

@app.route('/')
def index():
    message = generate_message("application")
    return jsonify({"message": message})