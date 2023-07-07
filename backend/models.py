import mysql.connector as mysql

class ConnectDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self):
            try:
                db = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                print("Connected Successfully")
            except mysql.Error == "NameError":
                print(f"Check your connection credentials")
            else:
                print("Connection NOT successful")
            return {"message": "Guess it's connected!!"}