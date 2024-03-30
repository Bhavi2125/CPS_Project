from tkinter import *
from tkinter import messagebox
import time
import re


def view(username, main_frame):
    filename = "User_Posts.txt"

    try:
        with open(filename, "r") as user_file:
            post_content = user_file.read()
            if not post_content:
                messagebox.showinfo("No Posts", "You do not have any posts.")
                return
            else:
                messagebox.showinfo("Your Posts", "Your posts will be displayed.")
                display_posts(post_content, main_frame)
    except FileNotFoundError:
        messagebox.showinfo("No Posts", "You do not have any posts.")


def display_posts(post_content, main_frame):
    posts = post_content.split("---%^&*()---") 
    posts.reverse()  

    for widget in main_frame.winfo_children():
        widget.destroy()

    posts_frame = Frame(main_frame, bg ='#F8EFBA' )
    lb = Label(posts_frame, text="All Posts", font=('Bold', 30), bg ='#F8EFBA').pack()
    
    posts_frame.pack(pady=20)

    scrollbar = Scrollbar(posts_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    post_listbox = Listbox(posts_frame, yscrollcommand=scrollbar.set, width=150, height=30)
    post_listbox.pack(side=LEFT, fill=BOTH)

    for post in posts:
        if post.strip():
            post_listbox.insert(END, post.strip())
            post_listbox.insert(END, '-' * 20)

    scrollbar.config(command=post_listbox.yview)


obscene_keywords = ["obscene_word1", "obscene_word2", "obscene_phrase1", "obscene_phrase2"]

def detect_obscene_language(text):
    for keyword in obscene_keywords:
        if re.search(keyword, text, re.IGNORECASE):
            return True    
    return False  


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    matches = []

    i = 0  
    j = 0  

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def create_post(main_frame, username):

    def post_content():     
        post_content = post_text.get("1.0", "end-1c")
        
        kmp_start_time = time.time()
        kmp_matches = kmp_search(post_content, "obscene_word1")  
        kmp_time = time.time() - kmp_start_time

        naive_start_time = time.time()
        naive_matches = [m.start() for m in re.finditer(re.escape("obscene_word1"), post_content)]  
        naive_time = time.time() - naive_start_time

       
        print("KMP Execution Time:", kmp_time)
        print("Naive Execution Time:", naive_time)

       
        if kmp_matches or naive_matches or detect_obscene_language(post_content):
            messagebox.showwarning("Obscene Language", "Your post contains obscene language. Please refrain from using inappropriate language.")
            
        else:

            filename = "User_Posts.txt"
            with open(filename, "a") as user_file:
                user_file.write(username + " : " + post_content + "\n---%^&*()---\n")
            messagebox.showinfo("Post Created", "Post created successfully!")

    for widget in main_frame.winfo_children():
        widget.destroy()
        
    create_frame = Frame(main_frame)
    lb = Label(create_frame, text="Create your Post", font=('Bold', 30), bg ='#F8EFBA').pack()

    create_frame.pack(pady=20)
    post_text = Text(main_frame, height=10, width=100)
    post_text.pack(pady=20)

    post_button = Button(main_frame, text="Post", width = 20, cursor = 'hand2', bg = '#1B9CFC', font = ('arial', 15),  command=post_content)
    post_button.pack(pady = 10)

def run_app(username):
    
    root = Tk()
    root.title("App")
    root.state('zoomed')
    root.configure(bg="#fff")

    user = username
    print(user)
    option_frame = Frame(root, bg='#1B9CFC')
    option_frame.pack(side=LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=300, height=1000)

    main_frame = Frame(root, highlightbackground='black', highlightthickness=2, bg ='#F8EFBA')
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=1000, width=1234)
    
    def home():
        for widget in main_frame.winfo_children():
            widget.destroy()
            
        home_frame = Frame(main_frame)
        lb = Label(home_frame, text="Home Page", font=('Bold', 30), bg = '#F8EFBA').pack()

        home_frame.pack(pady=20)
        

    def create():
        create_post(main_frame, username)

    def view_page():
        view(username_label.cget("text"), main_frame)

    home_btn = Button(option_frame, text='Home', font=('Bold', 15), fg='#F8EFBA', bg='#1B9CFC', bd=0, command=home)
    home_btn.place(x=40, y=100)


    create_btn = Button(option_frame, text='Create Post', font=('Bold', 15), fg='#F8EFBA', bg='#1B9CFC', bd=0, command=create)
    create_btn.place(x=40, y=180)


    view_btn = Button(option_frame, text='View Posts', font=('Bold', 15), fg='#F8EFBA', bg='#1B9CFC', bd=0, command=view_page)
    view_btn.place(x=40, y=260)


    username_label = Label(root, text=f"Welcome, {username}!", font=('arial', 15, 'bold'),fg = '#F8EFBA', bg='#1B9CFC')
    username_label.place(x=100, y=25)

    root.mainloop()

if __name__ == "__main__":
    run_app()
