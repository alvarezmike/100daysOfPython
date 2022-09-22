from tkinter import *


def button_clicked():
    print("I got clicked")


# setting up window GUI
window = Tk()
window.title("My first GUI program using Tkinter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)  # adding padding between widgets

# label
my_label = Label(text='Im a label', font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)


# button
new_button = Button(text="New Button")
new_button.grid(column=3, row=1)

button = Button(text="click me", command=button_clicked)
button.grid(column=2, row=2)


# entry
input = Entry(width=10)
input.get()
input.grid(column=4, row=4)


window.mainloop()