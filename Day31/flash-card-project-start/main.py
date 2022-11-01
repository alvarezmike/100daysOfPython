import random
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv("data/french_words.csv")
my_dict = df.to_dict(orient="records")

# ---------Functions-------------
def next_card():
    value = random.choice(list(my_dict))
    value["French"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=value["French"])

# --------------------------------


# window set up
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# canvas set up
canvas = Canvas(width=800, height=526)
logo_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
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
known_button = Button(image=check_image, border=0, highlightthickness=0,command=next_card)
known_button.grid(row=1, column=1)


next_card()
window.mainloop()
