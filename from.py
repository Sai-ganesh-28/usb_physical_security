from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector

def ok():
    fn=e1.get()
    ln=e2.get()
    pn=e3.get()
    ei=e4.get()
    pas=e5.get()
    conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
    my_cursor=conn.cursor()
    sql="INSERT INTO user(Fname,Lname,Pno,eid,password) VALUES (%s ,%s, %s, %s, %s)"
    val=(fn,ln,pn,ei,pas)
    my_cursor.execute(sql,val)
    conn.commit()
    messagebox.showinfo("","the data is stored")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    conn.close()
    root.destroy()

root=Tk()
root.title("login page")
root.geometry("300x300")
global e1
global e2
global e3
global e4
global e5
Label(root, text="USB PHYSICAL SECURITY REGISTER PAGE" ,font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=10, y=10)
Label(root, text="First Name").place(x=10, y=60)
Label(root, text="Last Name").place(x=10, y=80)
Label(root, text="Phone number").place(x=10, y=100)
Label(root, text="Email Id").place(x=10, y=120)
Label(root, text="Password").place(x=10, y=140)

e1 = Entry(root)
e1.place(x=140,y=60)

e2 = Entry(root)
e2.place(x=140,y=80)

e3 = Entry(root)
e3.place(x=140,y=100)

e4 = Entry(root)
e4.place(x=140,y=120)

e5 = Entry(root)
e5.place(x=140,y=140)
e5.config(show="*")

Button(root, text="Login",command=ok, height = 1, width = 13).place(x=150, y=160)
root.mainloop()
import login
