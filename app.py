from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

# Basic authentication (static token for simplicity)
AUTH_TOKEN = "securetoken123"

# Import modules
from database import init_db, get_db_connection
from query_processor import convert_to_sql
from authentication import authenticate

# Initialize database
init_db()

@app.route("/")
def home():
    return "Mini Query Engine is running!", 200


# /query endpoint
@app.route("/query", methods=["POST"])
def query():
    auth_error = authenticate()
    if auth_error:
        return auth_error
    
    data = request.get_json()
    nl_query = data.get("query")
    
    if not nl_query:
        return jsonify({"error": "Missing query parameter"}), 400
    
    sql_query = convert_to_sql(nl_query)
    if not sql_query:
        return jsonify({"error": "Unsupported query"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.close()
    
    return jsonify({"query": nl_query, "sql": sql_query, "result": result})

# /explain endpoint
@app.route("/explain", methods=["POST"])
def explain():
    auth_error = authenticate()
    if auth_error:
        return auth_error
    
    data = request.get_json()
    nl_query = data.get("query")
    sql_query = convert_to_sql(nl_query)
    
    if not sql_query:
        return jsonify({"error": "Unsupported query"}), 400
    
    return jsonify({"query": nl_query, "sql_translation": sql_query})

# /validate endpoint
@app.route("/validate", methods=["POST"])
def validate():
    auth_error = authenticate()
    if auth_error:
        return auth_error
    
    data = request.get_json()
    nl_query = data.get("query")
    sql_query = convert_to_sql(nl_query)
    
    if sql_query:
        return jsonify({"query": nl_query, "valid": True})
    else:
        return jsonify({"query": nl_query, "valid": False})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)