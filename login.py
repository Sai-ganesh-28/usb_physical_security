from pydoc import tempfilepager
import tkinter as tk
from tkinter import Label, messagebox
import subprocess
from subprocess import call
from PIL import Image ,ImageTk
from tkinter import Tk,PhotoImage
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
def ok1():
    ei=e1.get()
    pas=e2.get()
    conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
    my_cursor=conn.cursor()
    sql="select * from user where eid=%s and password=%s"
    val=(ei,pas)
    my_cursor.execute(sql,val)
    results=my_cursor.fetchall()
    conn.close()
    if results:
        messagebox.showinfo("","login success")
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(8))
        print(password)
        a=password
        conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
        my_cursor=conn.cursor()
        sql="INSERT INTO why(passwords,sno) VALUES (%s ,%s)"
        val=(a,1)
        my_cursor.execute(sql,val)
        conn.commit()
        conn.close()
        def send_email(to_email, subject, body):
            smtp_server = 'smtp-mail.outlook.com'
            smtp_port = 587
            sender_email = 'a.dminusb@outlook.com'
            sender_password = 'admin2811'
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = to_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            with smtplib.SMTP(smtp_server, smtp_port) as server:
              server.starttls()
              server.login(sender_email, sender_password)
              server.sendmail(sender_email, to_email, message.as_string())
        recipient_email = e1.get() 
        email_subject = 'Your Random Password'
        email_body = f'Your randomly generated password is: {password}'
        send_email(recipient_email, email_subject, email_body)
        
root=Tk()
root.title("login page")
root.geometry("500x300")
global e1
global e2
Label(root, text="USB PHYSICAL SECURITY LOGIN PAGE" ,font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=10, y=10)
Label(root, text="Email Id").place(x=10, y=60)
Label(root, text="Password").place(x=10, y=80)

e1 = tk.Entry(root)
e1.place(x=140,y=60)
e2 = tk.Entry(root)
e2.place(x=140,y=80)
e2.config(show="*")
tk.Button(root, text="Login",command=ok1, height = 1, width = 13).place(x=150, y=100)
root.mainloop()