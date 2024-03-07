from tkinter import Tk, Label, messagebox, ttk
from customtkinter import *
import os

def create():
    f = Tk()
    f.geometry("500x500+300+0")
    f.config(bg="#F0F3F4")
    frame = CTkFrame(master=f,
                     fg_color="#FEFFFE",
                     width=400,
                     height=300,
                     corner_radius=10)
    frame.place(relx=0.1, rely=0.17)

    def acc():
        if os.path.exists("passwords"):
            pass
        else:
            os.mkdir("passwords")
            messagebox.showinfo("create", "passwords directory has been created")
        username = usr.get()
        password = passw.get()
        if username and password:
            file_name = f"passwords\\{username}.txt"

            if os.path.exists(file_name):
                messagebox.showinfo("sorry", "user already exists")
            else:
                with open(f"passwords\\{username}.txt", "w") as f:
                    f.write(f"{username}:{password}\n")
                messagebox.showinfo("added", "successfully account created")
        else:
            messagebox.showinfo("cant", "invalid username and password")

    usr = CTkEntry(frame, width=350, height=50, corner_radius=5, border_width=0.8, fg_color="black",
                   font=("Helvetica", 18), placeholder_text="Email or Phone number")
    usr.place(x=25, y=30)

    passw = CTkEntry(frame, corner_radius=5, width=350, height=50, border_width=0.8, fg_color="black",
                     font=("Helvetica", 18), placeholder_text="password", show="*")
    passw.place(x=25, y=95)

    button = CTkButton(frame, hover_color="#1877F2", width=350, border_width=2, height=50, fg_color="#1877F2",
                       text="submit", text_color="white", font=("Helvetica", 23, 'bold'), command=acc)
    button.place(x=25, y=165)

    f.mainloop()


from tkinter import messagebox

def login():
    username = usr.get()
    password = passw.get()
    if username and password:
        a = 'passwords'
        b = f'{username}.txt'

        file_name = os.path.join(a, b)

        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                stored_data = f.readline().strip().split(":")
                stored_username, stored_password = stored_data[0], stored_data[1]

                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Success", "Login successful.")
                else:
                    messagebox.showinfo("Error", "Invalid username or password.")
        else:
            messagebox.showinfo("Error", "User does not exist.")
    else:
        messagebox.showinfo("Error", "Invalid username or password.")


fb = Tk()
fb.geometry("1366x768")
fb.config(bg="#F0F3F4")

Label(fb, text="facebook", fg="#0966FE", bg='#F0F3F4', font=("Helvetica", 45, 'bold')).place(x=180, y=230)
Label(fb, text="Connect with friends and the world", fg="black", font=("Helvetica", 23)).place(x=180, y=310)
Label(fb, text="around you on Facebook.", fg="black", font=("Helvetica", 23)).place(x=180, y=350)

frame = CTkFrame(master=fb,
                 fg_color="#FEFFFE",
                 width=400,
                 height=380,
                 corner_radius=10)

frame.place(relx=0.6, rely=0.17)

usr = CTkEntry(frame, width=350, height=50, corner_radius=5, border_width=0.8, fg_color="white",
               font=("Helvetica", 18), placeholder_text="Email or Phone number")
usr.place(x=25, y=30)

passw = CTkEntry(frame, corner_radius=5, width=350, height=50, border_width=0.8, fg_color="white",
                 font=("Helvetica", 18), placeholder_text="password", show="*")
passw.place(x=25, y=95)

button = CTkButton(frame, hover_color="#1877F2", width=350, height=50, fg_color="#1877F2", text="Log in",
                   text_color="white", font=("Helvetica", 23, 'bold'), command=login)
button.place(x=25, y=165)

fbutton = CTkButton(fb, hover_color="white", fg_color="white", text="forgetten password?", text_color="#1877F2",
                    font=("Helvetica", 16,))
fbutton.place(x=950, y=360)

underline_label = ttk.Label(fb, text="forgetten password?", font=("Helvetica", 16), foreground="blue",
                            background="#F0F3F4")
underline_label.place(x=950, y=360)

underline_color = "blue"  # Change this to the desired underline color

def on_enter(event):
    underline_label.config(font=("Helvetica", 16, "underline"), foreground=underline_color)

def on_leave(event):
    underline_label.config(font=("Helvetica", 16), foreground="blue")  # Change "white" to the original text color

underline_label.bind("<Enter>", on_enter)
underline_label.bind("<Leave>", on_leave)

cbutton = CTkButton(fb, width=40, height=50, fg_color="#42B62B", hover_color="green", text="create new account",
                    text_color="white", font=("Helvetica", 19, 'bold'), command=create)
cbutton.place(x=935, y=430)
CTkFrame(frame, width=300, height=0, bg_color="#cccccc").place(x=60, y=270)
vbutton = CTkButton(fb, fg_color='#F0F3F4', hover_color='#F0F3F4', text="create a page", text_color="black",
                    font=("Helvetica", 14, 'bold'))
vbutton.place(x=850, y=525)
Label(text="for a celebrity, brand or business.", fg="black", font=("Helvetica", 10,)).place(x=971, y=526)
vbutton.bind("<Enter>", lambda event: event.widget.config(
    font=(event.widget.cget("font").split(' ')[0], event.widget.cget("font").split(' ')[1], "underline")))
vbutton.bind("<Leave>", lambda event: event.widget.config(
    font=(event.widget.cget("font").split(' ')[0], event.widget.cget("font").split(' ')[1])))

fb.mainloop()
