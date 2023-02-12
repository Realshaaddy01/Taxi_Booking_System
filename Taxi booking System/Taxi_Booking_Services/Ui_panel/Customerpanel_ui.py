from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
from tktimepicker import AnalogPicker, AnalogThemes, constants
from tkcalendar import DateEntry
import tkinter as tk
from Trip_panel.tripdb import updateTrip, deleteTrip, saveTrip, allTrips
from Trip_panel.trip_panel import getset_Trip
import GlobalVar

# customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class CustomerClass:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Welcome Customer")
        self.parent.geometry("1280x720")
        self.parent.resizable(False, False)

        MAin_Frame_1 = Frame(self.parent, width=1280, height=720, bg='black')
        MAin_Frame_1.place(x=0, y=0)

        self.banner_frame = customtkinter.CTkFrame(master=self.parent,
                                              width=1300,
                                              height=120,
                                              corner_radius=5,
                                              bg_color="#FFFFFF",
                                              )
        self.banner_frame.place(x=0, y=0)

        label = customtkinter.CTkLabel(master=self.banner_frame, text="Welcome to Customer Panel", font=("barabara", 60))
        label.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

        cidd = Entry(self.parent)
        cidd.insert(0, GlobalVar.globalCustomer[0])
        # customer_frame = Frame(self.parent, width=1280, height=560, bg="brown")
        # customer_frame.place(x=0, y=50)

        self.frame_1 = customtkinter.CTkFrame(master=self.parent,
                                       width=300,
                                       height=350,
                                       corner_radius=40,
                                       bg_color="#BF3EFF",
                                       fg_color="#E3CF57")
        self.frame_1.place(x=70, y=230)

        self.frame_2= customtkinter.CTkFrame(master=self.parent,
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


        def editFunction():
            Payment = Paymenttxt.get()
            Pickup = Pickuptxt.get()
            Dropoff = Dropofftxt.get()
            Time = Timetxt.get()
            Date = Datetxt.get()
            Tid = TIDtxt.get()
            trip = getset_Trip(TID=Tid, Payment=Payment, Pickup=Pickup, Dropoff=Dropoff, Time=Time, Date=Date,
                                   CID=cidd.get(), booking_status='pending')
            req_result = updateTrip(trip)
            if req_result == True:
                messagebox.showinfo("taxi", " request successful")
            else:
                messagebox.showerror("taxi", "error booking")
            self.parent.destroy()
            parent = Tk()
            CustomerClass(parent)
            parent.mainloop()

        btnEdit = customtkinter.CTkButton(self.btnframe_3, text='EDIT',width=12, command=editFunction, font=("Verdana", 12), hover_color="#1E90FF",border_color="#F4A460",fg_color="#030303")
        btnEdit.place(x=30, y=35)

        def deleteFunction():
            TID = TIDtxt.get()
            deleteTrip(TID)
            messagebox.showinfo("taxi", " delete successful")
            self.parent.destroy()
            parent = Tk()
            CustomerClass(parent)
            parent.mainloop()

        btnDelete = customtkinter.CTkButton(self.btnframe_3,width=12, text='DELETE', command=deleteFunction, font=("Verdana", 12), hover_color="#FF3030",border_color="#F4A460",fg_color="#030303")
        btnDelete.place(x=195, y=35)

        customtkinter.CTkLabel(self.frame_2, text="Customer Booking Table", text_color="black",
              font=('Arial', 20, 'bold')).place(x=250,y=0)

        Booking_Table_cust = ttk.Treeview(self.frame_2)
        Booking_Table_cust['columns'] = ('TID', 'Payment', 'Pickup', 'Dropoff', 'Time', 'Date')

        Booking_Table_cust.column("#0", width=0, anchor=CENTER, stretch=NO)
        Booking_Table_cust.column("TID", width=50, anchor=CENTER, stretch=NO)
        Booking_Table_cust.column("Payment", width=50, anchor=CENTER)
        Booking_Table_cust.column("Pickup", width=100, anchor=CENTER)
        Booking_Table_cust.column("Dropoff", width=100, anchor=CENTER)
        Booking_Table_cust.column("Time", width=100, anchor=CENTER)
        Booking_Table_cust.column("Date", width=100, anchor=CENTER, )

        Booking_Table_cust.heading("#0", text="", anchor=CENTER)
        Booking_Table_cust.heading("TID", text="Trip ID", anchor=CENTER)
        Booking_Table_cust.heading("Payment", text="Payment", anchor=CENTER)
        Booking_Table_cust.heading("Pickup", text="Pickup", anchor=CENTER)
        Booking_Table_cust.heading("Dropoff", text="Dropoff", anchor=CENTER)
        Booking_Table_cust.heading("Time", text="TIME", anchor=CENTER)
        Booking_Table_cust.heading("Date", text="DATE", anchor=CENTER)

        def table():

            print(cidd.get())
            viewbook= getset_Trip(CID=cidd.get(), booking_status='pending')
            tripsRes = allTrips( viewbook)
            print(tripsRes)

            for row in tripsRes:
                Booking_Table_cust.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        table()
        def getfromtable(a):

            TIDtxt.delete(0, END)
            Paymenttxt.delete(0, END)
            Pickuptxt.delete(0, END)
            Dropofftxt.delete(0, END)
            Timetxt.delete(0, END)
            Datetxt.delete(0, END)
            # selected = Booking_Table_cust.focus()
            # values = Booking_Table_cust(selected, 'values')
            itemSelect = Booking_Table_cust.selection()[0]
            TIDtxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][0])
            Paymenttxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][1])
            Pickuptxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][2])
            Dropofftxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][3])
            Timetxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][4])
            Datetxt.insert(0, Booking_Table_cust.item(itemSelect)['values'][5])

        Booking_Table_cust.bind('<<TreeviewSelect>>', getfromtable)

        Booking_Table_cust.place(x=91, y=90)

        def newBookingsave():
            Payment = Paymenttxt.get()
            Pickup = Pickuptxt.get()
            Dropoff = Dropofftxt.get()
            Time = Timetxt.get()
            Date = Datetxt.get()
            trip = getset_Trip('', Payment=Payment, Pickup=Pickup, Dropoff=Dropoff, Time=Time, Date=Date,
                                   CID=cidd.get(), booking_status='pending')
            req_result = saveTrip(trip)
            if req_result == True:
                messagebox.showinfo("taxi", " request successful")
            else:
                messagebox.showerror("taxi", "error booking")
            self.parent.destroy()
            parent = Tk()
            CustomerClass(parent)
            parent.mainloop()

        btnnewBook = customtkinter.CTkButton(self.btnframe_3, text="SAVE",width=12, command=newBookingsave, font=("Verdana", 12), hover_color="#00CED1",border_color="#F4A460",fg_color="#030303")
        btnnewBook.place(x=112, y=35)
        # name = Label(self.parent, text="Welcome to Customer Panel!!!",
        #                 font=('Arial', 29, 'bold'))
        # name.place(x=350, y=180)

        def totime():
            top = tk.Toplevel(self.frame_1)
            time_picker = AnalogPicker(top, type=constants.HOURS12)
            time_picker.pack(expand=True, fill="both")

            theme = AnalogThemes(time_picker)
            theme.setDracula()
            # theme.setNavyBlue()
            # theme.setPurple()

            ok_btn = tk.Button(top, text="ok", width=8, bg="#FFa127", borderwidth=4, activebackground="#000",
                               activeforeground="#fff", command=lambda: updatetime(time_picker.time()))
            ok_btn.pack()
            exit_button = Button(top, text="Exit", width=8, bg="#FF6347", activebackground="#f00",
                                 activeforeground="#fff",
                                 borderwidth=4, command=top.destroy)
            exit_button.pack(pady=20)

        def updatetime(time):
            Timetxt.insert(0, str('{}:{} {}'.format(*time)))

        time = ()
        TIDtxt = Entry(self.frame_1)
        TIDtxt.place(x=140, y=50)
        Paymenttxt = Entry(self.frame_1)
        Paymenttxt.place(x=140, y=100)

        Pickuptxt = Entry(self.frame_1)
        Pickuptxt.place(x=140, y=150)

        Dropofftxt = Entry(self.frame_1)
        Dropofftxt.place(x=140, y=200)
        Timetxt = customtkinter.CTkEntry(self.frame_1,width=65,fg_color="white",text_color="black",corner_radius=0,border_width=0,border_color="black",font=('Arial', 12))
        time_btn = Button(self.frame_1, text= 'set time', command = totime, width=6, bg="green", borderwidth=2)
        time_btn.place(x=220,y=300)
        Timetxt.place(x=140, y=300)
        Datetxt = DateEntry(self.frame_1, width=16,background='darkblue',foreground='white', borderwidth=2, year=2023)
        Datetxt.place(x=140, y=250)

        TIDlbl = Label(self.frame_1, text="TID")
        TIDlbl.place(x=30, y=50)
        Paymentlbl = Label(self.frame_1, text="Payment")
        Paymentlbl.place(x=30, y=100)
        Pickuplbl = Label(self.frame_1, text="Pickup")
        Pickuplbl.place(x=30, y=150)
        Dropofflbl = Label(self.frame_1, text="Dropoff")
        Dropofflbl.place(x=30, y=200)
        Timelbl = Label(self.frame_1, text="Time")
        Timelbl.place(x=30, y=300)
        Datelbl = Label(self.frame_1, text="Date")
        Datelbl.place(x=30, y=250)
        def Logout():
            self.parent.destroy()
            from Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()
        log_btn = customtkinter.CTkButton(self.parent, text='LOGOUT', command=Logout, border_color="#6959CD",fg_color="#FF4040", font=('Arial', 20, 'bold'),hover_color="#FF0000")
        log_btn.place(x=1110, y=630)

if __name__ == '__main__':
    parent = Tk()
    CustomerClass(parent)
    parent.mainloop()
