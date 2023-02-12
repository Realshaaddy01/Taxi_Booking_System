import sys
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import tkinter as tk
import customtkinter
from Staff_panel.driverpanel import getset_driver
from Staff_panel.driverdb import saveDriver
from Ui_panel.Register_Customer_ui import Signup_Customer_Class

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class Signup_driver_class:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("login_page")
        self.parent.geometry("1280x720")
        # self.parent.state('zoomed')
        self.parent.resizable(False, False)
        # background_colour
        self.parent['background'] = '#63C5DA'
        # customer_register_frame
        MAin_Frame_1 = Frame(self.parent, width=1280, height=720, bg='black')
        MAin_Frame_1.place(x=0, y=0)

        self.banner_frame = customtkinter.CTkFrame(master=self.parent,
                                                   width=1300,
                                                   height=120,
                                                   corner_radius=5,
                                                   bg_color="#FFFFFF",
                                                   )
        self.banner_frame.place(x=0, y=0)

        label = customtkinter.CTkLabel(master=self.banner_frame, text="Driver Registration",
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
        label.place(x=95, y=5)

        def createDriver():
            name = name_txt.get()
            address = address_txt.get()
            email = email_txt.get()
            contact = contact_txt.get()
            license = Liscense_txt.get()
            Registration_num = Registration_txt.get()
            password = password_txt.get()
            driverInfo = getset_driver(DID='', Name=name, Address=address, Email=email, Phone=contact,
                                           License_num=license,
                                           Registration_num=Registration_num, Password=password)
            saveDriver(driverInfo)
            messagebox.showinfo("Title", "Sucessfully Registered")
            self.parent.destroy()
            parent = Tk()
            from Login_ui import Login_Menu
            Login_Menu(parent)
            parent.mainloop()

        def ValidateDriver():
            result = False
            # name validation
            tmpname = name_txt.get()

            # address validation
            validate_Address = address_txt.get()
            # addressRegex = re.compile("^[a-zA-Z]+,[a-zA-Z]")  # match

            # email validation
            validate_Email = email_txt.get()
            # emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

            # mobile validation
            validateMobile = contact_txt.get()
            # mobileRegex = re.compile("^9[0-9]+$")  # match

            # Liscense validation
            validate_Liscense = Liscense_txt.get()
            # licenseRegex = re.compile("\d{16}|\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}")

            # vehiche number registration
            validate_vehicleNumber = Registration_txt.get()
            # vehicleNumberRegex = re.compile("\d{4}")
            # password validation
            validatePassword = password_txt.get()
            # passwordRegex = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")


            # if tmpname != "" and re.match(addressRegex, validate_Address) and re.match(emailRegex,
            #                                                                            validate_Email) and re.match(
            #     licenseRegex, validate_Liscense) and re.match(vehicleNumberRegex,
            #                                                   validate_vehicleNumber) and re.match(
            #     mobileRegex, validateMobile) and re.match(
            #     passwordRegex, validatePassword):
            createDriver()
            # else:
            #     messagebox.showwarning("Title", "Please enter correctly")


        # label_name
        name_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your Username",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        name_txt.place(x=110, y=90)

        address_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your Address",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        address_txt.place(x=110, y=140)

        email_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your Email",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        email_txt.place(x=110, y=190)

        contact_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your MobileNo.",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        contact_txt.place(x=110, y=240)

        Liscense_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your lisecnseNo.",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        Liscense_txt.place(x=110, y=290)

        Registration_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your VehicleNo.",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        Registration_txt.place(x=110, y=340)

        password_txt = customtkinter.CTkEntry(self.frame_1,placeholder_text_color="#00FF7F", font=("Verdana", 15),placeholder_text="Enter your Password",bg_color="#FFFFFF",fg_color="#EEE5DE",width=180,text_color="black")
        password_txt.place(x=110, y=390)



        # send to login function
        def login():
            self.parent.destroy()
            from Login_ui import Login_Menu
            parent = Tk()
            Login_Menu(parent)
            parent.mainloop()

        def customerRegistration():
            self.parent.destroy()
            parent = Tk()
            Signup_Customer_Class(parent)
            parent.mainloop()

        validate_btn = customtkinter.CTkButton(self.parent, text="LOGIN", command=login, font=("Verdana", 13),hover_color="#54FF9F", fg_color="#191970", corner_radius=5,bg_color="#BF3EFF")
        validate_btn.place(x=1100, y=35)

        btn_Exit = customtkinter.CTkButton(self.frame_1, text="Cancel", command=exit,  font=("Verdana", 13),hover_color="#CD0000", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        btn_Exit.place(x=200, y=440)

        btn_save = customtkinter.CTkButton(self.frame_1, text="Save", command=ValidateDriver,  font=("Verdana", 13),hover_color="#3A5FCD", fg_color="#308014", corner_radius=5,bg_color="#BF3EFF")
        btn_save.place(x=40, y=440)

        customer_Signup_Btn = customtkinter.CTkButton(self.parent,text="Register as Customer!!",command=customerRegistration,hover_color="#54FF9F", fg_color="#191970", corner_radius=5,bg_color="#BF3EFF")
        customer_Signup_Btn.place(x=35, y=35)


        self.parent.mainloop()


if __name__ == '__main__':
    parent = Tk()
    Signup_driver_class(parent)
    parent.mainloop()

