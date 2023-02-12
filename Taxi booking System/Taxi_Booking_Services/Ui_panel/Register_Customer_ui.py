import sys
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import re
import mysql.connector
import customtkinter
from Customer_panel.customerdb import saveCustomer
from Customer_panel.customerpanel import getset_Cust

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class Signup_Customer_Class:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("login_page")
        self.parent.geometry("1280x720")
        # self.parent.state('zoomed')
        self.parent.resizable(False, False)
        # background_colour
        # self.parent['background'] = '#63C5DA'
        MAin_Frame_1 = Frame(self.parent, width=1280, height=720, bg='black')
        MAin_Frame_1.place(x=0, y=0)

        self.banner_frame = customtkinter.CTkFrame(master=self.parent,
                                                   width=1300,
                                                   height=120,
                                                   corner_radius=5,
                                                   bg_color="#FFFFFF",
                                                   )
        self.banner_frame.place(x=0, y=0)

        label = customtkinter.CTkLabel(master=self.banner_frame, text="Customer Registration",
                                       font=("barabara", 60))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.frame_1 = customtkinter.CTkFrame(master=self.parent,
                                              width=400,
                                              height=500,
                                              corner_radius=40,
                                              bg_color="#BF3EFF",
                                              fg_color="#E3CF57")
        self.frame_1.place(x=450, y=150)
        label = customtkinter.CTkLabel(master=self.frame_1, text="Registration Form", text_color="black",
                                       font=("Minion Pro", 30))
        label.place(x=95,y=5)


        def save():

            name = txt_name.get()
            address = txt_address.get()
            email = txt_email.get()
            contact = txt_contact.get()
            age = txt_age.get()
            password = txt_password.get()

            customerInfo = getset_Cust(CID='', Name=name, Address=address, Email=email, Phone=contact, Age=age,
                                    Password=password)
            saveCustomer(customerInfo)
            self.parent.destroy()
            from Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()


        def back_btn():
            self.parent.destroy()
            from Ui_panel.Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()

        # send to login function


        # validation of customerbackend register
        def Validate():
            result = False
            # name validation
            tmpname = txt_name.get()

            # address validation
            validate_Address = txt_address.get()
            addressRegex = re.compile("^[a-zA-Z]+,[a-zA-Z]")  # match

            # email validation
            validate_Email = txt_email.get()
            emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

            # mobile validation
            validateMobile = txt_contact.get()
            mobileRegex = re.compile("^98[0-9]+$")  # match

            # age verification
            validate_Age = txt_age.get()
            ageRegex = re.compile('^(?:1[01][0-9]|120|1[8-9]|[2-9][0-9])$')  # match

            # password validation
            validatePassword = txt_password.get()
            passwordRegex = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

            # confirm writtern password
            validateRePassword = txt_repassword.get()
            if validateRePassword == validatePassword:
                 result = True
            else:
                result = False
                messagebox.showinfo("Title", "error re-enter password")

            if tmpname != "" and re.match(addressRegex, validate_Address) and re.fullmatch(emailRegex,
                                                                                           validate_Email) and re.fullmatch(
                mobileRegex, validateMobile) and re.fullmatch(ageRegex, validate_Age) and re.fullmatch(
                passwordRegex, validatePassword) and validateRePassword == validatePassword:
                save()
            else:
                messagebox.showwarning("Title", "Please enter correctly")

        # def customer_registration_function():

        def driverregister():
            self.parent.destroy()
            from Ui_panel.Register_Driver_ui import Signup_driver_class
            parent = Tk()
            Signup_driver_class(parent)
            parent.mainloop()

        # label_name
        # lblname = customtkinter.CTkLabel(self.frame_1, text="Name: ",  font=("Verdana", 15),
        #                                          fg_color="black")
        # lblname.place(x=70, y=90)

        txt_name = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#912CEE", font=("Verdana", 15),placeholder_text="Enter your Username",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_name.place(x=110, y=90)

        txt_address = customtkinter.CTkEntry(self.frame_1, placeholder_text_color="#912CEE",font=("Verdana", 15),placeholder_text="Enter Your Address",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_address.place(x=110, y=140)

        txt_email = customtkinter.CTkEntry(self.frame_1, placeholder_text_color="#912CEE",font=("Verdana", 15),placeholder_text="Enter Your Email",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_email.place(x=110, y=190)

        txt_contact = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#912CEE", font=("Verdana", 15),placeholder_text="Enter Mobile.no.",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_contact.place(x=110, y=240)

        txt_age = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#912CEE", font=("Verdana", 15),placeholder_text="Enter Your Age",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_age.place(x=110, y=290)

        txt_password = customtkinter.CTkEntry(self.frame_1, placeholder_text_color="#912CEE",font=("Verdana", 15),placeholder_text="Enter Your Password",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_password.place(x=110, y=340)

        txt_repassword = customtkinter.CTkEntry(self.frame_1, placeholder_text_color="#912CEE",font=("Verdana", 15),placeholder_text="Confirm Your Password",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        txt_repassword.place(x=110, y=390)

        driver_SignupBtn = customtkinter.CTkButton(self.parent,text="Register as Driver!!",command=driverregister,hover_color="#27408B", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        driver_SignupBtn.place(x=35, y=35)

        btn_Exit = customtkinter.CTkButton(self.frame_1, text="Cancel", command=exit,  font=("Verdana", 13),hover_color="#CD0000", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        btn_Exit.place(x=200, y=440)

        btn_save = customtkinter.CTkButton(self.frame_1, text="Save", command=Validate,  font=("Verdana", 13),hover_color="#2E8B57", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        btn_save.place(x=40, y=440)

        btn_login = customtkinter.CTkButton(self.parent, text="LOGIN", command=back_btn, font=("Verdana", 13),hover_color="#54FF9F", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        btn_login.place(x=1100, y=35)

        self.parent.mainloop()

if __name__ == '__main__':
    parent = Tk()
    Signup_Customer_Class(parent)
    parent.mainloop()

