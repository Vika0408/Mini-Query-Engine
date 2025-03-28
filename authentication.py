from flask import request, jsonify

AUTH_TOKEN = "securetoken123"

def authenticate():
    token = request.headers.get("Authorization")
    if token != f"Bearer {AUTH_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    return None