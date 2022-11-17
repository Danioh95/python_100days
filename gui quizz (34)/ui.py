THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quest = ""
        self.value_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300)
        self.website_label = Label(text=f"score: {self.quiz.score}", padx=20, pady=20, bg=THEME_COLOR, fg="white"
                                   , font=(12))
        self.website_label.grid(row=1, column=2)
        photo1 = PhotoImage(file="images/true.png")
        photo2 = PhotoImage(file="images/false.png")
        self.gree_button = Button(image=photo1, highlightthickness=0, command=self.truess)
        self.gree_button.grid(row=3, column=1)
        self.red_button = Button(image=photo2, highlightthickness=0, command=self.falsess)
        self.red_button.grid(row=3, column=2)
        self.question_label = self.canvas.create_text(
            150,
            125,
            width=280,
            text=self.quest,
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20, padx=20)

        self.change_quest()

        self.window.mainloop()

    def change_quest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
            self.website_label.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_label, text="You've reached the end of the quiz.")
            self.red_button.config(state="disabled")
            self.gree_button.config(state="disabled")

    def truess(self):
        self.answer = "True"
        self.give_feedback(self.quiz.check_answer(self.answer))


    def falsess(self):
        self.answer = "False"
        self.give_feedback(self.quiz.check_answer(self.answer))


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.change_quest)



