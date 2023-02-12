import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import GlobalVar
import customtkinter
from Staff_panel.driverpanel import getset_driver
from Staff_panel.driverdb import driverstatuschanger, allTrips5
from Trip_panel.tripdb import assignTrips
from Trip_panel.trip_panel import getset_Trip


class DriverClass:
    def __init__(self, parent):
        self.parent=parent
        self.parent.title("welcome driver")
        self.parent.geometry("1280x720")
        self.parent.resizable(False, False)
        driverdid = Entry(self.parent)
        driverdid.insert(0, GlobalVar.globalDriver[0])
        print(driverdid.get())
        # self.parent['background'] = '#f54021'


        self.banner_frame = customtkinter.CTkFrame(master=self.parent,
                                                   width=1280,
                                                   height=120,
                                                   corner_radius=5,
                                                   bg_color="#FFFFFF",
                                                   )
        self.banner_frame.place(x=0, y=0)

        label = customtkinter.CTkLabel(master=self.banner_frame, text="Welcome to Staff Panel",
                                       font=("barabara", 60))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.frame_1 = customtkinter.CTkFrame(master=self.parent,
                                              width=300,
                                              height=350,
                                              corner_radius=40,
                                              bg_color="#BF3EFF",
                                              fg_color="#E3CF57")
        self.frame_1.place(x=70, y=230)

        self.frame_2 = customtkinter.CTkFrame(master=self.parent,
                                              width=700,
                                              height=370,
                                              corner_radius=40,
                                              bg_color="#BF3EFF",
                                              fg_color="#E3CF57")
        self.frame_2.place(x=490, y=230)
        self.btnframe_3 = customtkinter.CTkFrame(master=self.parent,
                                                 width=300,
                                                 height=100,
                                                 corner_radius=40,
                                                 bg_color="#BF3EFF",
                                                 fg_color="#E3CF57")
        self.btnframe_3.place(x=70, y=575)
        def completeBooking():

            tid=TIDtxt.get()
            did=GlobalVar.globalDriver[0]
            status='completed'
            namee=getset_Trip(TID=tid, DID=did, booking_status=status)
            result=assignTrips(namee)
            statusdriver = 'active'
            driverstatuschange = getset_driver(DID=did, driver_status=statusdriver)
            result = driverstatuschanger(driverstatuschange)
            messagebox.showinfo("Title", "Booking Completed Successfully")

        TIDtxt = Entry(self.frame_1)
        TIDtxt.place(x=140, y=50)
        Paymenttxt = Entry(self.frame_1)
        Paymenttxt.place(x=140, y=100)
        Pickuptxt = Entry(self.frame_1)
        Pickuptxt.place(x=140, y=150)
        Dropofftxt = Entry(self.frame_1)
        Dropofftxt.place(x=140, y=200)
        Timetxt = Entry(self.frame_1)
        Timetxt.place(x=140, y=250)
        Datetxt = Entry(self.frame_1)
        Datetxt.place(x=140, y=300)

        TIDlbl = Label(self.frame_1, text="TID")
        TIDlbl.place(x=30, y=50)
        Paymentlbl = Label(self.frame_1, text="Payment")
        Paymentlbl.place(x=30, y=100)
        Pickuplbl = Label(self.frame_1, text="Pickup")
        Pickuplbl.place(x=30, y=150)
        Dropofflbl = Label(self.frame_1, text="Dropoff")
        Dropofflbl.place(x=30, y=200)
        Timelbl = Label(self.frame_1, text="Time")
        Timelbl.place(x=30, y=250)
        Datelbl = Label(self.frame_1, text="Date")
        Datelbl.place(x=30, y=300)

        customtkinter.CTkLabel(self.frame_2, text="Trip Details Table", text_color="black",
                               font=('Arial', 20, 'bold')).place(x=250, y=0)

        Booking_Table_staff = ttk.Treeview(self.frame_2)
        Booking_Table_staff['columns'] = ('TID', 'Payment', 'Pickup', 'Dropoff', 'Time', 'Date')

        Booking_Table_staff.column("#0", width=0, anchor=CENTER, stretch=NO)
        Booking_Table_staff.column("TID", width=50, anchor=CENTER, stretch=NO)
        Booking_Table_staff.column("Payment", width=50, anchor=CENTER)
        Booking_Table_staff.column("Pickup", width=100, anchor=CENTER)
        Booking_Table_staff.column("Dropoff", width=100, anchor=CENTER)
        Booking_Table_staff.column("Time", width=100, anchor=CENTER)
        Booking_Table_staff.column("Date", width=100, anchor=CENTER)

        Booking_Table_staff.heading("#0", text="", anchor=CENTER)
        Booking_Table_staff.heading("TID", text="Trip ID", anchor=CENTER)
        Booking_Table_staff.heading("Payment", text="PAYMENT", anchor=CENTER)
        Booking_Table_staff.heading("Pickup", text="PICKUP_ADD", anchor=CENTER)
        Booking_Table_staff.heading("Dropoff", text="DROPOFF_ADD", anchor=CENTER)
        Booking_Table_staff.heading("Time", text="TIME", anchor=CENTER)
        Booking_Table_staff.heading("Date", text="DATE", anchor=CENTER)

        def table():

            viewbook = getset_Trip(DID=GlobalVar.globalDriver[0], booking_status='booked')
            tripsRes5 = allTrips5(viewbook)


            for row in tripsRes5:
                Booking_Table_staff.insert(parent='', index='end',
                                                values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        table()

        def getfromtable(a):
            TIDtxt.delete(0, END)
            Paymenttxt.delete(0, END)
            Pickuptxt.delete(0, END)
            Dropofftxt.delete(0, END)
            Timetxt.delete(0, END)
            Datetxt.delete(0, END)
            itemSelect = Booking_Table_staff.selection()[0]
            TIDtxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][0])
            Paymenttxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][1])
            Pickuptxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][2])
            Dropofftxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][3])
            Timetxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][4])
            Datetxt.insert(0, Booking_Table_staff.item(itemSelect)['values'][5])

        Booking_Table_staff.bind('<<TreeviewSelect>>', getfromtable)
        Booking_Table_staff.place(x=91, y=90)

        complete_btn = customtkinter.CTkButton(self.btnframe_3,text='completeBooking',command=completeBooking, hover_color="#00C957",fg_color="#00EEEE")
        complete_btn.place(x=82, y=35)

        def Logout():
            self.parent.destroy()
            from Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()


        logbtn = customtkinter.CTkButton(self.parent, text='Logout', command=Logout,corner_radius=20,bg_color="#030303", hover_color="#FF4500",fg_color="#DC143C")
        logbtn.place(x=1100, y=35)


if __name__=='__main__':
    parent=Tk()
    DriverClass(parent)
    parent.mainloop()
