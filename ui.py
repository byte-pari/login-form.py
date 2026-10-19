from tkinter import *
from tkinter import messagebox
from db import database

win = Tk()
win.geometry('500x400')
win.title('Login form')
win.config(bg="#a097e5")
db=database('E:\proj1\mydata')
#func======
def clear():
    ent_password.delete(0,END)
    ent_email.delete(0,END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
def sign_up():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if not email or not password:
        messagebox.showerror('error','email and password are required!')
    db.add_users(fname,lname,email,password)
    messagebox.showinfo('success','registered!')
    clear()

    

def open_wellcome():
    new_win = Toplevel(win)
    new_win.title('wellcome')
    new_win.geometry('300x300')
    lable1 = Label(new_win , text='wellcome back')
    lable1.pack(pady=30)

def sign_in():
    password=ent_password.get()
    email=ent_email.get()
    if not email or not password:
        messagebox.showerror('error','email or password are required!')
        return
    users = db.find(email,password)
    if users:
        open_wellcome()
    else:
        messagebox.showerror('error','usere not find or wrong password')
    
#widget====
lbl_fname = Label(win,text='fname:',font='arial 15 bold',bg='#a097e5')
lbl_fname.place(x=20,y=30)
ent_fname=Entry(win, width = 55)
ent_fname.place(x=130,y= 35)
lbl_lname = Label(win,text='Lname:',font='arial 15 bold',bg='#a097e5')
lbl_lname.place(x=20,y=70)
ent_lname=Entry(win, width = 55)
ent_lname.place(x=130,y= 75)
lbl_email = Label(win,text='Email:',font='arial 15 bold',bg='#a097e5')
lbl_email.place(x=20,y=110)
ent_email=Entry(win, width = 55)
ent_email.place(x=130,y= 115)
lbl_stare = Label(win,text='*',fg='red',bg='#a097e5')
lbl_stare.place(x=120,y=110)
lbl_password = Label(win,text='Password:',font='arial 15 bold',bg='#a097e5')
lbl_password.place(x=20,y=150)
ent_password=Entry(win, width = 55,show='*')
ent_password.place(x=130,y= 155)
lbl_stare = Label(win,text='*',fg='red',bg='#a097e5')
lbl_stare.place(x=120,y=150)
btn_sign = Button(win,text='sign up',font='arial 10 bold',width=15,command=sign_up)
btn_sign.place(x=100,y=250)
btn_signin = Button(win,text='sign in',font='arial 10 bold',width=15,command=sign_in)
btn_signin.place(x=250,y=250)
win.mainloop()