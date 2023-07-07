from flask import Flask
from models import ConnectDB
from dotenv import load_dotenv

load_dotenv()
import os

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

app = Flask(__name__)

@app.route("/")
def home():
    return {"page": "Home"}

@app.route("/connection_checker")
def checker():
     connector = ConnectDB(host=host, user=user, password=password, database=database)
     return connector.connection()
     

if __name__=="__main__":
    app.run(debug=True, port=7001)