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


def saveDriver(driverInfo):
    conn = None
    sql = """Insert INTO drivers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'active')"""
    values = (
    driverInfo.getDID(), driverInfo.getName(), driverInfo.getAddress(), driverInfo.getEmail(), driverInfo.getPhone(),
    driverInfo.getLicense_num(), driverInfo.getRegistration_num(), driverInfo.getPassword())
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


def searchDriver(email,password):
    conn = None
    sql = """SELECT * From drivers Where email=%s AND password=%s"""
    driver = None
    values = (email,password)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return driver


def updateDriver(driverInfo):
    conn = None
    sql = """UPDATE Drivers set Name=%s,License_num=$s WHERE DID=%s"""
    values = (
    driverInfo.getDID(), driverInfo.getName(), driverInfo.getAddress(), driverInfo.getEmail(), driverInfo.getPhone(),
    driverInfo.getLicense_num(), driverInfo.getRegistration_num())
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


def driverstatuschanger(tripInfo):
    conn=None
    sql="""UPDATE drivers set driver_status=%s WHERE DID=%s"""
    values=(tripInfo.getdriver_status(),tripInfo.getDID())
    result=False
    try:
        conn=db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True

    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result


def deleteDriver(driverInfo):
    conn = None
    sql = """DELETE FROM WHERE DID=%s"""
    values = (driverInfo.getDID,)
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


def allDrivers():
    conn = None
    sql = """DISPLAY * FROM drivers"""
    drivers = None
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, )
        drivers = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del sql
        del conn
        return drivers

def  allTrips5(send):
    conn = None
    sql = """SELECT TID, Payment, Pickup, Dropoff, Time, Date FROM trips WHERE DID=%s AND booking_status=%s """
    values=(send.getDID(),send.getbooking_status())
    tripsRes5=None
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        tripsRes5=cursor.fetchall()
        print("Working")
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return tripsRes5
