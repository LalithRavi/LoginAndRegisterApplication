'''
Created on Apr 10, 2020

@author: lalith
'''
import tkinter as tk
import random as rand
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox     

def register():
    global students
    register_screen = tk.Toplevel()
    register_screen.title("Registration")
    register_screen.geometry("500x500")
    register_screen.configure(bg = "#F8931D")
    
    global student_id
    student_id = rand.randint(1,100)
    id_label = tk.Label(register_screen, text = "Student ID: {}".format(student_id))    
    registration = tk.Label(register_screen, text = "REGISTRATION", font = ("Calibri", "35"), bg = "#F8931D")
    id_label.pack(anchor = NE)
    registration.pack()
    
    global user
    global passwd
    global conf    
    name = tk.Label(register_screen, text = "Name: ", bg = "#F8931D")
    password = tk.Label(register_screen, text = "Password: ", bg = "#F8931D")
    note = tk.Label(register_screen, text = "*NOTE: Password needs to contain letters and numbers*", bg = "#F8931D", fg = "red")
    confirm = tk.Label(register_screen, text = "Confirm Password: ", bg = "#F8931D")
    course_label = tk.Label(register_screen, text = "Course: ", bg = "#F8931D")
    user = tk.Entry(register_screen)
    passwd = tk.Entry(register_screen, show = "*")
    conf = tk.Entry(register_screen, show = "*")
    course_entry = ttk.Combobox(register_screen, width = 30, values = ['Accounting Payroll Administration', 'Automation Technology', 'CAD/CAM Technology', 'Computerized Accounting', 'Food Service Worker', 'Office Administration'])
        
    name.pack()
    user.pack()
    password.pack()
    passwd.pack()
    confirm.pack()
    conf.pack()
    course_label.pack()
    course_entry.pack()
    note.pack()
    def passwd_check():
        has_alpha = False
        has_num = False
        has_special = False
        special_chars = "`~!@#$%^&*()_+\|]}[{/?.>,<"
        for i in passwd.get():
            if i.isalpha():
                has_alpha = True
            if i.isdigit():
                has_num = True
            if i in special_chars:
                has_special = True
        return has_alpha and has_num and has_special
    
    def reg_analysis():
        
        def passwd_match():
            messagebox.showwarning("Registration Error", "Passwords do not match!")
        
        def alnumspecial_password():
            messagebox.showwarning("Registration Error", "Password needs to contain one letter, one number and one special character!")
        
        def exist_user():
            messagebox.showwarning("Registration Error", "Username already exists!")
        
        def success(user):
            messagebox.showinfo("Registration", "{} has been successfully registered".format(user))
        
        if os.path.exists("Students\{}.txt".format(user.get())) == False:
            if passwd_check():
                if conf.get() == passwd.get():
                    student = open("Students\{}.txt".format(user.get()), "w")
                    success(user.get())           
                    student.write("Username: {}".format(user.get()))
                    student.write("\n")
                    student.write("Password: {}".format(passwd.get()))
                    student.write("\n")
                    student.write("ID: {}".format(student_id))
                    student.write("\n")
                    student.write("Course: {}".format(course_entry.get()))
                    register_screen.destroy()
                    student.close()
                elif conf.get() != passwd.get():
                    register_screen.destroy()
                    passwd_match()
            else:
                register_screen.destroy()
                alnumspecial_password() 
        else:
            register_screen.destroy()
            exist_user()
    
    register = tk.Button(register_screen, text = "REGISTER", command = reg_analysis, bg = "#0B7CC0")
    register.pack()
    
    register_screen.mainloop()

def login():
    login_screen = tk.Toplevel()
    login_screen.title("Login")
    login_screen.geometry("500x500")
    login_screen.configure(bg = "#F8931D")

    for i in range(2):
        space = tk.Label(login_screen, text = "", bg = "#F8931D")
        space.pack()
    
    login = tk.Label(login_screen, text = "LOGIN", font = ("Calibri", "35"), bg = "#F8931D", underline = len("LOGIN") + 1)
    login.pack()
    
    space = tk.Label(login_screen, text = "", bg = "#F8931D")
    space.pack()
    
    global username
    global passwd
    
    name = tk.Label(login_screen, text = "Username *: ", bg = "#F8931D")
    password = tk.Label(login_screen, text = "Password *: ", bg = "#F8931D")
    username = tk.Entry(login_screen)
    passwd = tk.Entry(login_screen, show = "*")
    
    name.pack()
    username.pack()
    space = tk.Label(login_screen, text = "", bg = "#F8931D")
    space.pack()
    password.pack()
    passwd.pack()
    def login_analysis():
        
        def invalid_passwd():
            messagebox.showwarning("Login Error", "Invalid Password!")
        
        def invalid_user():        
            messagebox.showwarning("Login Error", "Invalid Username!")
        
        if username.get() != "" and passwd.get() != "":
            if os.path.exists("Students\{}.txt".format(username.get())) == True:
                students = open("Students\{}.txt".format(username.get()), "r")
                for i in students:
                    if username.get() in i:
                        for j in students:
                            if passwd.get() in j:
                                for k in students:
                                    if "ID" in k:
                                        for l in students:
                                            if "Course" in l:
                                                new = messagebox.showinfo("Login", "{}\nUsername: {}\n{}".format(k, username.get(), l))
                                                login_screen.destroy()
                                            else:
                                                continue
                            else:
                                login_screen.destroy()
                                invalid_passwd()                            
                    else:
                        login_screen.destroy()
                        invalid_user()
                students.close()
            else:
                login_screen.destroy()
                invalid_user()
        elif username.get() == "" and passwd.get() != "":
            login_screen.destroy()
            invalid_user()
        elif username.get() != "" and passwd.get() == "":
            login_screen.destroy()
            invalid_passwd()
    
    login = tk.Button(login_screen, text = "LOGIN", command = login_analysis, bg = "#0B7CC0")
    login.pack()
    
    login_screen.mainloop()    

def kill():
    confirm = messagebox.askyesno("Exit", "Are you sure that you want to exit the program?")
    if confirm == True:
        root.destroy()    
    
root = tk.Tk()
root.geometry("750x500")
root.title("Login & Register Form")
root.configure(bg = "#F8931D")
for i in range(2):
    space = tk.Label(root, text = "", bg = "#F8931D")
    space.pack()
title = tk.Label(root, text = "Welcome to Lalith's Login & Register Form", font = ("Calibri", "20"), bg = "#F8931D")
title.pack()
for i in range(3):
    space = tk.Label(root, text = "", bg = "#F8931D")
    space.pack()
login = tk.Button(root, text = "LOGIN", font = ("Calibri", "16"), width = 25, fg = "white", bg = "#0B7CC0", command = login)
login.pack()
space = tk.Label(root, text = "", bg = "#F8931D")
space.pack()  
register = tk.Button(root, text = "REGISTER", font = ("Calibri", "16"), width = 25, fg = "white", bg = "#0B7CC0", command = register)
register.pack()
space = tk.Label(root, text = "", bg = "#F8931D")
space.pack()
root.protocol("WM_DELETE_WINDOW", kill)
root.mainloop()
