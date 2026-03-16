from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Backend API Running"}

@app.route("/db")
def db_test():
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )
    return {"database": "connected"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)