import random
from tkinter import *

import pandas
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
value = {}
my_dict= {}
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    my_dict=original_data.to_dict(orient="records")
else:
    my_dict = df.to_dict(orient="records")

# ---------Functions-------------
def next_card():
    global value
    global flip_timer
    window.after_cancel(flip_timer)
    value = random.choice(list(my_dict))

    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=value["French"],fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=value["English"],fill="white")

def is_known():
    my_dict.remove(value)
    data= pandas.DataFrame(my_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------------------


# window set up
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)

# canvas set up
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=front_img)
card_title=canvas.create_text(400,150,fill="black", text="", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400,263,fill="black", text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)

# wrong button set up
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, border=0, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

# right button set up
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, border=0, highlightthickness=0,command=is_known)
known_button.grid(row=1, column=1)


next_card()

window.mainloop()
