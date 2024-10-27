from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
word = None
translated_word = None

# Read the word file and extract the words

try:
    word_infos= pd.read_csv("words_to_learn.csv")
    french_words = word_infos["French"].to_list()
    english_words = word_infos["English"].to_list()
except FileNotFoundError:
    word_infos= pd.read_csv("french_words.csv")
    french_words = word_infos["French"].to_list()
    english_words = word_infos["English"].to_list()



window= Tk()
window.title("Learn_French")
window.config(bg=BACKGROUND_COLOR)

img1 = PhotoImage(file="card_front.png")
img2 = PhotoImage(file="right.png")
img3 = PhotoImage(file="wrong.png")
img4 = PhotoImage(file="card_back.png")

# Basement setup
front = Canvas(height=400, width=400,highlightthickness=0)
front_img = front.create_image(200, 200, image= img1)
title1 = front.create_text(180, 150, text="", font=("Arial", 12, "italic"))
title2 = front.create_text(180, 200, text="", font=("Arial", 20, "bold"))
front.grid(row=0, column=0, columnspan=2,padx=20, pady=20)

def new_word () :
    global word

    right_btn.config(state= "disabled")
    wrong_btn.config(state= "disabled")

    # Fetching a French word randomly
    word = choice(french_words)
    front.itemconfig(front_img, image= img1)
    front.itemconfig(title1, text="French")
    front.itemconfig(title2, text= word)

    # Console the ans after 3s
    window.after(3000, func=console_ans)


def console_ans () :
    global translated_word

    front.itemconfig(front_img, image= img4)
    front.itemconfig(title1, text= "English")

    # Fetching the english meaning of the randomly selected word
    translated_word = word_infos[word_infos["French"] == word].English.item()
    front.itemconfig(title2, text= translated_word)

    right_btn.config(state= "normal")
    wrong_btn.config(state= "normal")

  
def correct () :
    # Removing words marked as known
    french_words.remove(word)
    english_words.remove(translated_word)

    learn_words = {
        "French" : french_words,
        "English" : english_words
    }

    data = pd.DataFrame(learn_words)
    print(data)
    data.to_csv("words_to_learn.csv" , index=False)

    new_word()
    

right_btn = Button(height=50, width=50, image=img2,padx=20, pady=50, highlightthickness=0, command=correct)
right_btn.grid(column=0, row=1)

wrong_btn = Button(height=50, width=50, image=img3, highlightthickness=0, command=new_word)
wrong_btn.grid(column=1, row=1)

new_word()
window.mainloop()