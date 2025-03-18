import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="prtpass101020",
        database="agrihelpers"
    )