import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from Staff_panel.driverpanel import getset_driver
from Staff_panel.driverdb import driverstatuschanger
from Trip_panel.tripdb import assignTrips, activeDrivers, allPendingTrips
from Trip_panel.trip_panel import getset_Trip

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class AdminClass:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Welcome Admin")
        self.parent.geometry("1280x720")
        self.parent.resizable(False, False)
        # self.parent['background'] = '#292421'

        # Assign Driver
        # self.frame_1 = Frame(self.parent, width=1280, height=560, bg="brown")
        # self.frame_1.place(x=0, y=50)


        self.banner_frame = customtkinter.CTkFrame(master=self.parent,
                                                   width=1300,
                                                   height=120,
                                                   corner_radius=5,
                                                   bg_color="#FFFFFF",
                                                   )
        self.banner_frame.place(x=0, y=0)
        assign_driver_txt = Entry(self.banner_frame)

        label = customtkinter.CTkLabel(master=self.banner_frame, text="Welcome to Admin Panel",
                                       font=("barabara", 60))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.frame_1 = customtkinter.CTkFrame(master=self.parent,
                                              width=300,
                                              height=350,
                                              corner_radius=40,
                                              bg_color="#BF3EFF",
                                              fg_color="#E3CF57")
        self.frame_1.place(x=70, y=210)

        self.frame_2 = customtkinter.CTkFrame(master=self.parent,
                                              width=700,
                                              height=370,
                                              corner_radius=40,
                                              bg_color="#BF3EFF",
                                              fg_color="#E3CF57")
        self.frame_2.place(x=490, y=210)
        self.btnframe_3 = customtkinter.CTkFrame(master=self.parent,
                                                 width=300,
                                                 height=100,
                                                 corner_radius=40,
                                                 bg_color="#BF3EFF",
                                                 fg_color="#E3CF57")
        self.btnframe_3.place(x=70, y=555)

        def assign_new_booking():
            tid = TIDtxt.get()
            did = assign_driver_txt.get()
            status = 'booked'
            get_data = getset_Trip(TID=tid, DID=did, booking_status=status)
            result = assignTrips(get_data)
            statusdriver = 'inactive'
            driver_status_change = getset_driver(DID=did, driver_status=statusdriver)
            result = driverstatuschanger(driver_status_change)
            if result == True:
                messagebox.showinfo('taxi', 'assigned success')
                my_booking_table1.delete(*my_booking_table1.get_children())
                table()

            else:
                messagebox.showerror('taxi', 'failed to change status')

        def viewactivedriver():
            activeResult = activeDrivers()
            combine_data = [r for r, in activeResult]
            assign_driver_txt.configure(values=combine_data)
            assign_driver_txt.place(x=500, y=400)

        assign_driver_txt = ttk.Combobox(self.btnframe_3, font=('Helvatical bold', 12),textvariable=assign_driver_txt)
        viewactivedriver()
        assign_driver_txt.place(x=55, y=43)

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

        customtkinter.CTkLabel(self.frame_2, text="Admin Review Table", text_color="black",
                               font=('Arial', 20, 'bold')).place(x=250, y=0)

        my_booking_table1 = ttk.Treeview(self.frame_2)
        my_booking_table1['columns'] = ('TID', 'Payment', 'Pickup', 'Dropoff', 'Time', 'Date')

        my_booking_table1.column("#0", width=0, anchor=CENTER, stretch=NO)
        my_booking_table1.column("TID", width=50, anchor=CENTER, stretch=NO)
        my_booking_table1.column("Payment", width=50, anchor=CENTER)
        my_booking_table1.column("Pickup", width=100, anchor=CENTER)
        my_booking_table1.column("Dropoff", width=100, anchor=CENTER)
        my_booking_table1.column("Time", width=100, anchor=CENTER)
        my_booking_table1.column("Date", width=100, anchor=CENTER, )

        my_booking_table1.heading("#0", text="", anchor=CENTER)
        my_booking_table1.heading("TID", text="Trip ID", anchor=CENTER)
        my_booking_table1.heading("Payment", text="Payment", anchor=CENTER)
        my_booking_table1.heading("Pickup", text="Pickup", anchor=CENTER)
        my_booking_table1.heading("Dropoff", text="Dropoff", anchor=CENTER)
        my_booking_table1.heading("Time", text="TIME", anchor=CENTER)
        my_booking_table1.heading("Date", text="DATE", anchor=CENTER)

        def table():

            viewbook = getset_Trip(booking_status='Pending')
            tripsRes1 = allPendingTrips()

            for row in tripsRes1:
                my_booking_table1.insert(parent='', index='end',
                                                values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        table()

        def getfromtable(a):

            TIDtxt.delete(0, END)
            Paymenttxt.delete(0, END)
            Pickuptxt.delete(0, END)
            Dropofftxt.delete(0, END)
            Timetxt.delete(0, END)
            Datetxt.delete(0, END)
            itemSelect = my_booking_table1.selection()[0]
            TIDtxt.insert(0, my_booking_table1.item(itemSelect)['values'][0])
            Paymenttxt.insert(0, my_booking_table1.item(itemSelect)['values'][1])
            Pickuptxt.insert(0, my_booking_table1.item(itemSelect)['values'][2])
            Dropofftxt.insert(0, my_booking_table1.item(itemSelect)['values'][3])
            Timetxt.insert(0, my_booking_table1.item(itemSelect)['values'][4])
            Datetxt.insert(0, my_booking_table1.item(itemSelect)['values'][5])

        my_booking_table1.bind('<<TreeviewSelect>>', getfromtable)

        my_booking_table1.place(x=95, y=90)

        def Logout():
            self.parent.destroy()
            from Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()

        logbtn = customtkinter.CTkButton(self.parent, text='logout', corner_radius=20,border_width=4,border_color="#54FF9F",command=Logout, font=('overstrike', 20, 'bold'),hover_color="red",bg_color="#1E1E1E",fg_color="#8B0000",text_color="white")
        logbtn.place(x=1100, y=35)
        assignbutton = customtkinter.CTkButton(self.btnframe_3, text='Assign', command=assign_new_booking, font=('Arial', 20, 'bold'),hover_color="#FFA500",fg_color="#71C671",text_color="white")
        assignbutton.place(x=75, y=5)


if __name__ == '__main__':
    parent = Tk()
    AdminClass(parent)
    parent.mainloop()
