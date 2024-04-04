import mysql.connector


class MySQLDBConnection:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = None

    
    def create_connection(self):
        print("in create_connection")
        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                    host=self.host,
                                    database=self.database)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
    def close_connection(self):
        if self.cnx:
            self.cnx.close()
            print("connection is closed")
        else:
            print("not currently connected")
