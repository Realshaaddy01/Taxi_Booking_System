import sys
import mysql.connector


def db_syncronise():
    conn=None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='bajeko_taxi_service')
    except:
        print("Error:", sys.exc_info())
    finally:
        return conn

def saveTrip(tripInfo):
    conn=None
    sql="""Insert INTO trips VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(tripInfo.getTID(),tripInfo.getPayment(), tripInfo.getPickup(), tripInfo.getDropoff(), tripInfo.getTime(), tripInfo.getDate(),tripInfo.getCID(),tripInfo.getDID(),tripInfo.getbooking_status())
    req_result=False
    try:
        conn=db_syncronise()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        req_result=True

    except:
        print("error!:",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return req_result
def searchTrip(tripInfo):
    conn=None
    sql="""SELECT * From trips Where CID = %s"""
    trip=None
    values=(tripInfo,)
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return trip


def updateTrip(tripInfo):
    conn=None
    sql="""UPDATE Trips set Payment=%s,Pickup=%s,Dropoff=%s,Time=%s,Date=%s WHERE TID=%s"""
    values=(tripInfo.getPayment(), tripInfo.getPickup(), tripInfo.getDropoff(), tripInfo.getTime(), tripInfo.getDate(),tripInfo.getTID())
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

def deleteTrip(tripInfo):
    conn=None
    sql="""DELETE  FROM trips WHERE TID=%s"""
    values=(tripInfo,)
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

def  allTrips(send):
    conn = None
    sql = """SELECT TID, Payment, Pickup, Dropoff, Time, Date FROM trips WHERE CID=%s AND booking_status=%s """
    values=(send.getCID(),send.getbooking_status())
    tripsRes=None
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        tripsRes=cursor.fetchall()
        print("Working")
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return tripsRes

def  allPendingTrips():
    conn = None
    sql = """SELECT TID, Payment, Pickup, Dropoff, Time, Date FROM trips WHERE booking_status='Pending'"""
    #values=(send.getbooking_status())
    tripsRes1=None
    try:
        conn = db_syncronise()
        cursor = conn.cursor()
        cursor.execute(sql,)
        tripsRes1=cursor.fetchall()
        print("Working")
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
       # del values
        del sql
        del conn
        return tripsRes1

def activeDrivers():
    conn=None
    sql="""SELECT DID FROM drivers WHERE driver_status='active'"""
    activeResult=None
    try:
        conn=db_syncronise()
        cursor=conn.cursor()
        cursor.execute(sql)
        activeResult=cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
       # del values
        del sql
        del conn
        return activeResult


def assignTrips(tripInfo):
    conn=None
    sql="""UPDATE Trips set DID=%s,booking_status=%s WHERE TID=%s"""
    values=(tripInfo.getDID(),tripInfo.getbooking_status(),tripInfo.getTID())
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
