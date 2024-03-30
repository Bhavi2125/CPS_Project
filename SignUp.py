from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast

window = Tk()
window.title('SignUp')
window.state('zoomed')
window.configure(bg = '#fff')
window.resizable(False, False)

bgimg = ImageTk.PhotoImage(Image.open("qwerty.jpg"))
Label(image = bgimg, bg = 'white').place(x = 100, y= 110)

frame = Frame( window, width = 500, height = 600, bg = 'white')
frame.place(x = 900, y = 100)

heading = Label(frame, text = "Sign Up", fg = '#57a1f8', bg = 'white', font = ('arial', 30, 'bold'))
heading.place(x=180, y=60)


def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('Users.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('Users.txt', 'a')
            w = file.write(str(r))

            messagebox.showinfo('Signup', 'successfully sign up')

        except:
            file = open('Users.txt', 'w')
            pp = str({'username':'password'})
            file.write(pp)
            file.close()
    else :
        messagebox.showerror('Invalid', 'Both password should match')


def sign():
    window.destroy()


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


def on_enter(e):
    confirm_code.delete(0, 'end')

def on_leave(e):
    name = confirm_code.get()
    if name == '':
        confirm_code.insert(0, 'Confirm Password')
        
confirm_code = Entry(frame, width = 26, fg = 'black', border = 0, bg = 'white', font = ('arial', 15))
confirm_code.place(x = 100, y = 390)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x=100, y=420)


Button(frame, width = 27, pady = 7, text = 'Register', bg = '#57a1f8', fg = 'white', border = 0, font = ('arial', 15), command = signup).place(x = 100, y =480)
label = Label(frame, text = "Already have an account?", fg = 'black', bg = 'white', font = ('arial', 13)).place(x = 100, y = 550)
sign_up = Button(frame, width = 6, text = 'Sign in', border = 0, bg = 'white', cursor = 'hand2', fg ='#57a1f8', font = ('arial', 13), command = sign).place(x = 340, y = 550)

window.mainloop()
