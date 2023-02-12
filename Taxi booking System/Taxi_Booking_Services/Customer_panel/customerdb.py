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

def saveCustomer(customerInfo):
    conn = None
    sql = """Insert INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values = (customerInfo.getCID(), customerInfo.getName(), customerInfo.getAddress(), customerInfo.getEmail(), customerInfo.getPhone(), customerInfo.getAge(), customerInfo.getPassword())
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print("error!:", sys.exc_info())
    finally:
        del values
        del sql
        del conn


def searchCustomer(info):
    conn = None
    sql = """SELECT * FROM customers WHERE email=%s AND password=%s"""
    customer = None
    values = (info.getEmail(),info.getPassword())
    print(values)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        customer = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return customer

def updateCustomer(customerInfo):
    conn = None
    sql = """UPDATE customers set Email=%s,Password=$s WHERE CID=%s"""
    values = (customerInfo.getCID, customerInfo.getName, customerInfo.getAddress, customerInfo.getEmail, customerInfo.getPhone, customerInfo.getAge, customerInfo.getPassword)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn


def deleteCustomer(customerInfo):
    conn = None
    sql = """DELETE FROM WHERE CID=%s"""
    values = (customerInfo.getCID,)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn


def allCustomer():
    conn = None
    sql = """SELECT * FROM customers"""
    customers = None
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, )
        customers = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del sql
        del conn
        return customers

def searchCustomer1(email):
        conn = None
        sql = """SELECT * FROM customers WHERE email=%s"""
        customer = None
        values = (email)
        print(values)
        try:
            conn = db_syncronise()
            cursor = conn.cursor()
            cursor.execute(sql)
            cusId= conn.cursor.fetchone()[0]
            print(cusId)
        except:
            print("Error:", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return customer