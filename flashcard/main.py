import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import time
from controller import *
from random import choice
import pandas as pd

try:
    dict2 = pd.read_csv("word_to_learn.csv")
    dict = [v.dropna().to_dict() for k,v in dict2.iterrows() ]


except FileNotFoundError:
    dfdict = pd.read_csv("french_words.csv") \
             .to_dict(orient="records")
    dict = [{dfdict[i]['French']: dfdict[i]['English']} for i in range(0, len(dfdict))]


def getNextWord():
    return choice(dict)

word = ""

def switch_english():
    global word
    language_label.config(text="English", font=("Ariel", 30, "italic"), bg="aquamarine4", fg="white")
    word_label.config(text=list(word.values()), font=("Ariel", 40, "bold"), bg="aquamarine4", fg="white")
    canvas.create_rectangle(0, 0, 800, 526, fill="aquamarine4", outline="grey")

def switch():
    global word
    word = getNextWord()

    language_label.config(text="French", font=("Ariel", 30, "italic"), bg="white", fg="black")
    word_label.config(text=list(word.keys()), font=("Ariel", 40, "bold"), bg="white", fg="black")
    canvas.create_rectangle(0, 0, 800, 526, fill="white", outline="grey")

    dict.remove(word)

    df = pd.DataFrame(dict)
    print(df)
    df.to_csv("word_to_learn.csv", index=FALSE)

    window.after(3000, switch_english)

def switch2():
    global word
    word = getNextWord()

    language_label.config(text="French", font=("Ariel", 30, "italic"), bg="white", fg="black")
    word_label.config(text=list(word.keys()), font=("Ariel", 40, "bold"), bg="white", fg="black")
    canvas.create_rectangle(0, 0, 800, 526, fill="white", outline="grey")


    window.after(3000, switch_english)




def start_game():
    start_button.destroy()

    green_button = Button(image=green_img, highlightthickness=0, bg="aquamarine4", command=switch)
    green_button.grid(row=1, column=1)

    red_button = Button(image=red_img, highlightthickness=0, bg="aquamarine4", command=switch2)
    red_button.grid(row=1, column=2)


##### graphic
window = Tk()
window.title("Flashcard  game")
window.config(padx=50, pady=50, bg="aquamarine4")

#Load all images
green_img = PhotoImage(file="green_chekc.png")
red_img = PhotoImage(file="red_check.png")

canvas = Canvas(height=566, width=800, bg="aquamarine4", highlightthickness=0)
canvas.create_rectangle(0, 0, 800, 526, fill="white", outline="grey")
canvas.grid(row=0, column=1, columnspan=2)

language_label = Label(text="French", font=("Ariel", 30, "italic"), bg="white")
language_label.place(x=400, y=150, anchor=CENTER)

word_label = Label(text="Word", font=("Ariel", 40, "bold"), bg="white")
word_label.place(x=400, y=280, anchor=CENTER)

start_button = Button(text="start", bg="aquamarine4", command=start_game)
start_button.grid(row=1, column=1, columnspan=3)

window.mainloop()
