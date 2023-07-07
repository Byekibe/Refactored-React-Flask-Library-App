import mysql.connector
from mysql.connector import errorcode
import os


def connect_to_db():
    try:
        conn = mysql.connector.connect(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            connect_timeout=28800
        )
        print(f"Connected to {os.getenv('DATABASE')} successfuly")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Connected...Please close connection if you are not using it!!")
    
    return conn  
                  
     