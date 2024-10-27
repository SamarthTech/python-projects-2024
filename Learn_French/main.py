from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
word_dict = None
word_lib = {}


# Read the word file and extract the words
try:
    word_infos= pd.read_csv("words_to_learn.csv")
    word_lib = word_infos.to_dict(orient="records")
    
    
except FileNotFoundError:
    word_infos= pd.read_csv("french_words.csv")
    word_lib = word_infos.to_dict(orient="records")
    



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
    global word_dict

    right_btn.config(state= "disabled")
    wrong_btn.config(state= "disabled")

    # Fetching a French word randomly
    word_dict = choice (word_lib)
    word_fr = word_dict["French"]
    front.itemconfig(front_img, image= img1)
    front.itemconfig(title1, text="French")
    front.itemconfig(title2, text= word_fr)

    # Console the ans after 3s
    window.after(3000, func=console_ans)


def console_ans () :
    front.itemconfig(front_img, image= img4)
    front.itemconfig(title1, text= "English")

    # Fetching the english meaning of the randomly selected word
    
    word_en = word_dict["English"]
    front.itemconfig(title2, text= word_en)

    right_btn.config(state= "normal")
    wrong_btn.config(state= "normal")


def correct () :
    # Removing words marked as known
    
    word_lib.remove(word_dict)



    data = pd.DataFrame(word_lib)
    print(data)
    data.to_csv("words_to_learn.csv" , index=False)

    new_word()
    

right_btn = Button(height=50, width=50, image=img2,padx=20, pady=50, highlightthickness=0, command=correct)
right_btn.grid(column=0, row=1)

wrong_btn = Button(height=50, width=50, image=img3, highlightthickness=0, command=new_word)
wrong_btn.grid(column=1, row=1)

new_word()
window.mainloop()