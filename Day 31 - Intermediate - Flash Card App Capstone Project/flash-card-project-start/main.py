from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --------------------- READ DATA FROM CSV FILE --------------------
import pandas as pd
import random

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    canvas.itemconfig(canvas_image, image=card_front)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french = current_card["French"]
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french, fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    english = current_card["English"]
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=english, fill="white")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# --------------------- UI -------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images\card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0,column=0, columnspan=2)

language = canvas.create_text(400, 153, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word" ,font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()





window.mainloop()
