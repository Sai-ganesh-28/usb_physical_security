import tkinter as tk
from tkinter import Label, messagebox
import subprocess
from PIL import Image ,ImageTk
from tkinter import Tk
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
def main():
  def pro_info():
      import webbrowser
      f=open("html file name","w")
      message='''
      <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 20px;
    }

    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }

    th {
      background-color: #f2f2f2;
    }

    tr:nth-child(even) {
      background-color: #f9f9f9;
    }

    tr:hover {
      background-color: #f5f5f5;
    }
  </style>
  <title>USB PHYSICAL SECURITY</title>
</head>
<body>
  <h2>PROJECT INFORMATION</h2>
  <table>
    <thead>
      <tr style="color: black;background-color:#green;">
        <th>Project details</th>
        <th>Info</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Project Name</td>
        <td>USB Physical Security</td>
      </tr>
      <tr>
        <td>Project Description</td>
        <td>The USB Physical Security refers to the set of mechanisms and techniques used to secure and control the access of devices to USB ports</td>
      </tr>
    </tbody>
  </table>
  
  </table>
</body>
</html>

      '''
      f.write(message)
      f.close()
      webbrowser.open_new_tab("html file name")
  root = tk.Tk()
  image = Image.open('image location')
  new_size=(200,200)
  b3=tk.Button(root, text="Project INFO" ,font=("Menlo" ,11), bg="red",fg="white",command=pro_info)
  b3.pack()
  project_label = tk.Label(root, text="***USB Physical Security***", font=("Arial", 18, "bold"), bg="white", fg="black")
  project_label.pack(pady=10)
  images=image.resize(new_size)
  tk_image=ImageTk.PhotoImage(images)
  label = tk.Label(root,image=tk_image)
  label.pack(pady=10)
  root.title("USB PHYSICAL SECURITY FOR SYSTEM")
  root.geometry('700x700')
  root.configure(bg='gray')
  button_frame=tk.Frame(root,bg='white')
  success_label=tk.Label(button_frame,text="",font=("Didot", 12),height=10, width=60,bg='black')
  success_label.pack()
  def b1_click():
      pass_open=tk.Toplevel(root)
      pass_open.title("enter the password to disable the usb")
      pass_open.geometry("400x300")
      pass_label=tk.Label(pass_open,text="enter the password")
      pass_label.pack()
      pass_enter=tk.Entry(pass_open, show="$")
      pass_enter.pack()
      def ok_btn():
            conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
            my_cursor=conn.cursor()
            res=pass_enter.get()
            sql="select passwords from why where passwords=%s and sno=%s"
            val=(res,1)
            my_cursor.execute(sql,val)
            results=my_cursor.fetchall()
            if results:
                command= r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 4 /f > nul'
                subprocess.call(command, shell=True)
                success_label.config(text="USB PORTS ARE DISABLE SUCCESS",bg='black',fg='white')
                res2=pass_enter.get()
                conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
                my_cursor=conn.cursor()
                sql1="delete from why where sno=%s and passwords=%s"
                val1=(1,res2)
                my_cursor.execute(sql1,val1)
                conn.commit()
                pass_enter.destroy()
            else:
                error_label.config(text="INCORRECT PASSWORD PLEASE TRY AGAIN",bg='black',fg='white')
                pass_enter.delete(0, tk.END)
      ok_btn=tk.Button(pass_open,text="ENTER" , command=ok_btn)
      ok_btn.pack()
      error_label = tk.Label(pass_open, text="" , font=("Didot",11), bg="#f2f2f2", fg="#ff0000")
      error_label.pack()
  def b2_click():
       pass_open=tk.Toplevel(root)
       pass_open.title("enter the password to enable the usb")
       pass_open.geometry("400x300")
       pass_label=tk.Label(pass_open,text="enter the enable password")
       pass_label.pack()
       pass_enter=tk.Entry(pass_open, show="$")
       pass_enter.pack()
       def ok_btn():
            conn=mysql.connector.connect(host="localhost", user="root", password="", database="database")
            my_cursor=conn.cursor()
            res=pass_enter.get()
            sql="select passwords from why where passwords=%s and sno=%s"
            val=(res,1)
            my_cursor.execute(sql,val)
            results=my_cursor.fetchall()
            if results:
                command= r'reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v "start" /t REG_DWORD /d 3 /f > nul'
                subprocess.call(command, shell=True)
                res1=pass_enter.get()
                success_label.config(text="USB PORTS ARE ENABLE SUCCESS",bg='black',fg='white')
                conn=mysql.connector.connect(host="localhost", user="root", password="", database="database")
                my_cursor=conn.cursor()
                sql1="delete from why where sno=%s and passwords=%s"
                val1=(1,res1)
                my_cursor.execute(sql1,val1)
                conn.commit()
                pass_enter.destroy()
            else:
                error_label.config(text="INCORRECT PASSWORD PLEASE TRY AGAIN",bg='black',fg='white')
                pass_enter.delete(0, tk.END)
       ok_btn=tk.Button(pass_open,text="ENTER" , command=ok_btn)
       ok_btn.pack()
       error_label = tk.Label(pass_open, text="" , font=("Didot",11), bg="#f2f2f2", fg="#ff0000")
       error_label.pack()
  b2=tk.Button(root, text="ENABLE USB PORT",font=("didot", 12),command=b2_click,bg="dark green",fg="white")
  b1=tk.Button(root, text="DISABLE USB PORT",font=("didot", 12),command=b1_click,bg="dark green",fg="white")
  b3=tk.Button(root, text="PROJECT INFO" ,font=("Menlo" ,11), bg="red",fg="white",command=pro_info)
  b1.pack(pady=10)
  b2.pack(pady=10)
  button_frame.pack()
  def reg():
          conn=mysql.connector.connect(host="localhost", user="root", password="", database="sup_database")
          my_cursor=conn.cursor()
          sql1="SELECT COUNT(*) FROM USER"
          my_cursor.execute(sql1)
          row = my_cursor.fetchone()[0]
          if row < 3:
            def ok():
              fn=e1.get()
              ln=e2.get()
              pn=e3.get()
              ei=e4.get()
              pas=e5.get()
              conn=mysql.connector.connect(host="localhost", user="root", password="", database="database")
              my_cursor=conn.cursor()
              sql="INSERT INTO user(Fname,Lname,Pno,eid,password) VALUES (%s ,%s, %s, %s, %s)"
              val=(fn,ln,pn,ei,pas)
              my_cursor.execute(sql,val)
              conn.commit()
              messagebox.showinfo("","the data is stored")
              e1.delete(0,tk.END)
              e2.delete(0, tk.END)
              e3.delete(0, tk.END)
              e4.delete(0, tk.END)
              e5.delete(0, tk.END)
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
            e1 = tk.Entry(root)
            e1.place(x=140,y=60)
            e2 = tk.Entry(root)
            e2.place(x=140,y=80)
            e3 = tk.Entry(root)
            e3.place(x=140,y=100)
            e4 = tk.Entry(root)
            e4.place(x=140,y=120)
            e5 = tk.Entry(root)
            e5.place(x=140,y=140)
            e5.config(show="*")
            tk.Button(root, text="Login",command=ok, height = 1, width = 13).place(x=150, y=160)
          else:
              messagebox.showinfo("","USER LIMIT REACHED")
  b4=tk.Button(root, text="REGISTRATION FORM" ,font=("Menlo" ,11), bg="dark blue",fg="white",command=reg)
  b4.pack(pady=10)
  b4.place(x=530,y=0)
  def log():
    global password
    def ok1():
      ei=e1.get()
      pas=e2.get()
      conn=mysql.connector.connect(host="localhost", user="root", password="", database="database")
      my_cursor=conn.cursor()
      sql="select * from user where eid=%s and password=%s"
      val=(ei,pas)
      my_cursor.execute(sql,val)
      results=my_cursor.fetchall()
      conn.close()
      if results:
          messagebox.showinfo("","login success check your email id for password")
          characters=string.ascii_letters + string.digits + string.punctuation
          password=''.join(random.choice(characters) for _ in range(8))
          a=password
          conn=mysql.connector.connect(host="localhost", user="root", password="", database="database")
          my_cursor=conn.cursor()
          sql="INSERT INTO why(passwords,sno) VALUES (%s, %s)"
          val=(a,1)
          my_cursor.execute(sql,val)
          conn.commit()
          conn.close()
          def send_email(to_email, subject, body):
            smtp_server = 'smtp-mail.outlook.com'
            smtp_port = 587
            sender_email = 'sender@outlook.com'
            sender_password = 'sender'
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
          root.destroy()
      else:
          messagebox.showinfo("","INCORRECT EMAIL ID OR PASSWORD")
          return False   
    root=Tk()
    root.title("login page")
    root.geometry("500x300")
    global e1
    global e2
    Label(root, text="USB PHYSICAL SECURITY USER CHECK" ,font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=10, y=10)
    Label(root, text="lEmai Id").place(x=10, y=60)
    Label(root, text="Password").place(x=10, y=80)
    e1 = tk.Entry(root)
    e1.place(x=140,y=60)
    e2 = tk.Entry(root)
    e2.place(x=140,y=80)
    e2.config(show="*")
    tk.Button(root, text="Login",command=ok1, height = 1, width = 13).place(x=150, y=100)
  b5=tk.Button(root, text="check user and generate password" ,font=("Menlo" ,11), bg="dark blue",fg="white",command=log)
  b5.pack(pady=10)
  root.mainloop()
main()
