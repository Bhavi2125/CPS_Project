from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ast
import os
from app import run_app


window = Tk()
window.title('Login')
window.state('zoomed')
window.configure(bg="#fff")

bgimg = ImageTk.PhotoImage(Image.open("qwerty.jpg"))
bgimg_label = Label(image = bgimg, bg = 'white').place(x = 100, y= 110)


def signin():
    username = user.get()
    password = code.get()

    file = open('Users.txt','r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        run_app(username)

    else:
        messagebox.showerror('Invalid', 'Invalid Username or Password')

def signup():
    os.system('SignUp.py')


frame = Frame( window, width = 500, height = 600, bg = 'white')
frame.place(x = 900, y = 100)
heading = Label(frame, text = "Sign in", fg = '#57a1f8', bg = 'white', font = ('arial', 30, 'bold'))
heading.place(x=180, y=60)


def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')
        
user = Entry(frame, width = 26, fg = 'black', border = 0, bg = 'white', font = ('arial', 15))
user.place(x = 100, y = 190)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x=100, y=220)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')
        
code = Entry(frame, width = 26, fg = 'black', border = 0, bg = 'white', font = ('arial', 15))
code.place(x = 100, y = 290)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x=100, y=320)


Button(frame, width = 27, pady = 7, text = 'Login', bg = '#57a1f8', fg = 'white', border = 0, font = ('arial', 15), command = signin).place(x = 100, y =380)
label = Label(frame, text = "Don't have an account?", fg = 'black', bg = 'white', font = ('arial', 13)).place(x = 100, y = 450)
sign_up = Button(frame, width = 6, text = 'Sign up', border = 0, bg = 'white', cursor = 'hand2', fg ='#57a1f8', font = ('arial', 13), command = signup).place(x = 340, y = 450)

window.mainloop()
