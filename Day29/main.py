from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(random.randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# creating file
f = open("data.txt", "a")

# function that activates when user press add button


def save():
    global f
# user can't leave fields empty
    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(message="oops", detail="Please make sure you don't have any field empty")
# if all fields all filled, proceed
    else:
        is_ok = messagebox.askokcancel(message=entry_website.get(),
                                       detail=f"These are the details entered: \nEmail: {entry_email.get()}"
                                               f"\nPassword: {entry_password.get()}"
                                               f"\nIs it ok to save? ")

        if is_ok:
            f.write(entry_website.get() + "|" + entry_email.get() + "|" + entry_password.get() + "\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


tk = Tk()
tk.title("Password Manager")
tk.config(padx=20, pady=20)

# creating canvas
canvas = Canvas(width=200, height=200)

# adding photo
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

canvas.grid(row=0, column=1)

# adding labels
lb_website = Label(tk, text="Website:")
lb_website.grid(row=1, column=0)
lb_email = Label(tk, text="Email/Username:")
lb_email.grid(row=2, column=0)
lb_password = Label(tk, text="Password:")
lb_password.grid(row=3, column=0)

# adding entries
entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")

entry_email = Entry(width=35)
entry_email.insert(0, "example@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="EW")

# adding buttons
btn_generatePassword = Button(tk, text="Generate Password", command=generate_password)
btn_generatePassword.grid(row=3, column=2, sticky="EW")
btn_add = Button(tk, width=36, text="Add", command=save)
btn_add.grid(row=4, column=1, columnspan=2, sticky="EW")


canvas.mainloop()

