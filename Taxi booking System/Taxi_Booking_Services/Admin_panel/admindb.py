import sys
import mysql.connector


def db_syncronise():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='bajeko_taxi_service')
    except:
        print("Error:", sys.exc_info())
    finally:
        return conn
def searchAdmin(email,password):
    conn = None
    sql = """SELECT * From admins Where email=%s AND password=%s"""
    admin = None
    values = (email,password)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        admin = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return admin
