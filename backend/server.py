from flask import Flask, request
from models import connect_to_db
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

@app.route("/data")
def home():
    try:
        query = ("SELECT * FROM books")
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
    except mysql.connector.Error as err:
        print(err)
    return {"data": data}

@app.route("/connection_checker")
def checker():
    conn = connect_to_db()
    cursor = conn.cursor()
    return "Hey"

@app.route("/insert", methods=["GET","POST"])
def insert_to_db():
    title = request.json["title"]
    author = request.json["author"]
    price = request.json["price"]
    pages = request.json['pages']
    review = request.json["review"]
    contact = request.json["contact"]
    category = request.json["category"]

    print(title, author, price, pages, review, contact, category)
    try:
        query = ("INSERT INTO books (title, author, price, pages, review, contact, category) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        query_vals = (title, author, price, pages, review, contact, category)
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query, query_vals)
        conn.commit()
        print("Inserted successfully")
    except mysql.connector.Error as err:
        print(err) 
    
    return {"message": "Check your database"}

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    title = request.json["title"]
    author = request.json["author"]
    price = request.json["price"]
    pages = request.json['pages']
    review = request.json["review"]
    contact = request.json["contact"]
    category = request.json["category"]

    print(title, author, price, pages, review, contact, category)
    
    try:
        query = ("UPDATE books SET title=%s, author=%s, price=%s, pages=%s, review=%s, contact=%s, category=%s WHERE book_id=%s")
        query_vals = (title, author, price, pages, review, contact, category, id)
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query, query_vals)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)

    return {"message": "Check your database"}

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = ("DELETE FROM books WHERE book_id = %s")
        query_vals = (id, )
        cursor.execute(query, query_vals)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)
    return { "message": "Check your DB" }

if __name__=="__main__":
    app.run(debug=True, port=7001)