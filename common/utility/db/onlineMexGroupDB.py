import os

import mysql.connector
from mysql.connector import Error

connection = None
cursor = None


class DatabaseUtility:

    @staticmethod
    def db_connection(query):
        global connection, cursor
        try:
            connection = mysql.connector.connect(host=os.environ.get('DB_HOST'),
                                                 database=os.environ.get('DB_NAME'),
                                                 user=os.environ.get('DB_USER'),
                                                 password=os.environ.get('DB_PASSWORD'))
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query)
                record = cursor.fetchone()
                return record

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
