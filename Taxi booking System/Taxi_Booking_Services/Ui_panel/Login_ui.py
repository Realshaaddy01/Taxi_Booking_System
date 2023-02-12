import sys
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import tkinter as tk

from Admin_panel.admindb  import searchAdmin
from Customer_panel.customerpanel import getset_Cust
from Customer_panel.customerdb import searchCustomer
from Staff_panel.driverdb import searchDriver
import GlobalVar
# from taxi_book_assignment.userPart import GlobalVar
from Ui_panel.Adminpanel_ui import AdminClass
from Ui_panel.Customerpanel_ui import CustomerClass
from Ui_panel.Staffpanel_ui import DriverClass


class Login_Menu:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("login_page")
        self.parent.geometry("1280x720")
        # self.parent.state('zoomed')
        self.parent.resizable(False, False)
        # background_colour
        self.parent['background'] = '#63C5DA'

        # # insert_Photo
        # img_1 = tk.PhotoImage(file='./Images/taxims.png')
        # label = Label(parent, image=self.img_1, bg="white").place(x=50, y=50)
        photo = ImageTk.PhotoImage(file='./Images/taxims.png')
        l_img = Label(self.parent, image=photo)
        l_img.image = photo
        l_img.place(x=110, y=50, height= 720, width=1080)

        self.frame1 = tk.Frame(self.parent, width=350, height=350, bg='white')
        self.frame1.place(x=620, y=245)

        def showhidepassword():
            if text_password.cget('show') == "*":
                text_password.configure(show='')
            else:
                text_password.configure(show='*')

        showhide = tk.Checkbutton(self.frame1, text="Show password", command=showhidepassword)
        showhide.place(x=100, y=170)

        lbl_search = Label(self.frame1, text="LOGIN HERE", fg="#6495ED",bg="white",font=("Microsoft YaHei UI Light",25,'bold'))
        lbl_search.place(x=80, y=0)


        # email_box
        txt_email = customtkinter.CTkEntry(self.frame1,width=190,placeholder_text="Enter Your Email" ,border_width=0, bg_color="#F5FFFA",fg_color="#EEE0E5", text_color="black")
        txt_email.place(x=85, y=90)

        # password_box
        text_password = customtkinter.CTkEntry(self.frame1, width=190,show='*',placeholder_text="Enter Your Password" ,border_width=0, bg_color="#F5FFFA",fg_color="#EEE0E5", text_color="black")
        text_password.place(x=85, y=135)

        def logginFunction():

            email = txt_email.get()
            password = text_password.get()
            vlogin = getset_Cust(Email=email, Password=password)
            customer = searchCustomer(vlogin)

            driver = searchDriver(email, password)
            admin = searchAdmin(email, password)

            if driver != None:
                GlobalVar.globalDriver = driver
                messagebox.showinfo("driverbackend Login Sucessful ", "Welcome {}".format(txt_email.get()))
                self.parent.destroy()
                parent = Tk()
                DriverClass(parent)
                parent.mainloop()


            elif customer != None:
                GlobalVar.globalCustomer = customer
                messagebox.showinfo("Customer Login Sucessful", "Welcome {}".format(txt_email.get()))

                self.parent.destroy()
                parent = Tk()
                CustomerClass(parent)
                parent.mainloop()

            elif admin != None:
                GlobalVar.globalAdmin = admin
                messagebox.showinfo("adminbackend Login Sucessful ", "Welcome {}".format(txt_email.get()))
                self.parent.destroy()
                parent = Tk()
                object = AdminClass(parent)
                parent.mainloop()
            else:
                messagebox.showerror("Title", "Incorrect Username or Password")

        # show signup page
        def signup():
            self.parent.destroy()
            from Register_Customer_ui import Signup_Customer_Class
            parent = Tk()
            Signup_Customer_Class(parent)
            parent.mainloop()

        # save button
        btnExit = customtkinter.CTkButton(self.frame1, hover_color="#EE0000",text="Cancel", command=exit,font=("Verdana", 12),
                         fg_color="#1E1E1E")
        btnExit.place(x=190, y=235)

        btnLogin = customtkinter.CTkButton(self.frame1, hover_color="#00C957",text="Login", command=logginFunction,font=("Verdana", 12),
                        fg_color="#1E1E1E" )
        btnLogin.place(x=30, y=235)

        #signup btn
        lbl_signup = Label(self.frame1, text="Don't have an account?", bg="white", fg="black",
                           font=('Microsoft YaHi UI Light', 9))
        lbl_signup.place(x=70, y=300)
        signup_btn = Button(self.frame1, width=6, height=0, text="Sign up", border=0, bg="white", cursor="hand2",command=signup,
                            fg="#57a1f8")
        signup_btn.place(x=210, y=300)

        self.parent.mainloop()


if __name__ == '__main__':
    parent = Tk()
    Login_Menu(parent)
    parent.mainloop()
