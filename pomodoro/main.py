from time import sleep
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20

pattern = [("Working time", RED, WORK_MIN),
           ("Working time", RED, SHORT_BREAK_MIN),
           ("Working time", RED, WORK_MIN),
           ("Working time", RED, SHORT_BREAK_MIN),
           ("Working time", RED, WORK_MIN),
           ("Working time", RED, SHORT_BREAK_MIN),
           ("Working time", RED, WORK_MIN),
           ("Working time", RED, LONG_BREAK_MIN)]
reps = 0
checkmar = ""
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    count_down(pattern[reps][2])

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check
    global checkmar
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    label = Label(text=pattern[reps][0], bg=YELLOW, fg=pattern[reps][1], font=(FONT_NAME, 45))
    label.grid(column=2, row=1)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        window.after(1000, count_down, count -1)
    else:
        reps += 1
        if (reps % 2) == 0:
            checkmar = checkmar + "✓"
            check = Label(text=checkmar, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18))
            check.grid(column=2, row=4)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


label2 = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
label2.grid(column=2, row=1)

check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18))
check.grid(column=2, row=4)

button = Button(text="Start", command=start_timer)
button.grid(column=1, row=3)

button = Button(text="Reset")
button.grid(column=3, row=3)

window.mainloop()