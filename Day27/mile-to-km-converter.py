from tkinter import *


def button_clicked():
    miles = float(input.get())
    conversion = 1.6093435
    kilometers = float((miles * conversion))
    my_label3["text"] = round(kilometers, 2)
    return kilometers


# setting up window GUI
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=250, pady=30)  # adding padding between widgets


# entry
input = Entry(width=10)
input.get()
input.grid(column=2, row=1)


# label
my_label = Label(text='Miles', font=("Arial", 18, "bold"))
my_label.grid(column=3, row=1)

my_label2 = Label(text='is equal to', font=("Arial", 18, "bold"))
my_label2.grid(column=0, row=2)

my_label3 = Label(text='0', font=("Arial", 18, "bold"))
my_label3.grid(column=2, row=2)

my_label4 = Label(text='Km', font=("Arial", 18, "bold"))
my_label4.grid(column=3, row=2)

# button
button = Button(text='Calculate', command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()