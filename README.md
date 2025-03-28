# 🚀 Mini Query Engine

## 📌 Overview
Mini Query Engine is a lightweight backend service that simulates an AI-powered data query system. It converts natural language queries into SQL-like statements and provides mock responses for basic data queries.

## ✨ Features
✅ Accepts natural language queries via REST API  
✅ Translates queries into pseudo-SQL  
✅ Provides mock responses from an in-memory database  
✅ Includes basic authentication  
✅ Endpoints for query execution, explanation, and validation  

## 🌍 Live Deployment
🎯 The API is deployed on Render and can be accessed at:  
🔗 [https://mini-query-engine.onrender.com](https://mini-query-engine.onrender.com)

## 📡 API Endpoints
### 1️⃣ `/query` (POST)
🔹 **Description:** Accepts a natural language query and returns the SQL equivalent with mock data.  
📤 **Request Example:**
```json
{
  "query": "how many employees"
}
```
📥 **Response Example:**
```json
{
  "query": "how many employees",
  "sql": "SELECT COUNT(*) FROM employees",
  "result": [[6]]
}
```

### 2️⃣ `/explain` (POST)
🔹 **Description:** Returns the SQL translation of a natural language query.  
📤 **Request Example:**
```json
{
  "query": "list all employees"
}
```
📥 **Response Example:**
```json
{
  "query": "list all employees",
  "sql_translation": "SELECT * FROM employees"
}
```

### 3️⃣ `/validate` (POST)
🔹 **Description:** Checks if a natural language query can be processed.  
📤 **Request Example:**
```json
{
  "query": "average salary"
}
```
📥 **Response Example:**
```json
{
  "query": "average salary",
  "valid": true
}
```

## 🔑 Authentication
🔒 All requests must include a Bearer token in the `Authorization` header:
```
Authorization: Bearer securetoken123
```

## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vika0408/Mini-Query-Engine.git
cd Mini-Query-Engine
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python app.py
```
### 4️⃣ Test with Postman or Curl
📌 Use Postman or the following curl command to test:
```bash
curl -X POST "https://mini-query-engine.onrender.com/query" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer securetoken123" \
     -d '{"query": "how many employees"}'
```

## 🏗️ Technologies Used
- 🐍 **Backend:** Python (Flask)
- 🗄️ **Database:** SQLite (in-memory storage)
- 🚀 **Deployment:** Render

## 🤝 Contributing
💡 Feel free to fork this repository and submit pull requests with improvements.



