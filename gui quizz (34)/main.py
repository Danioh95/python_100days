from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


parameter = {"amount": 10,
             "type": "boolean"}

x = requests.get("https://opentdb.com/api.php", params=parameter)

ar = x.json()


question_bank = []
for question in range(len(ar["results"])):
    question_text = ar["results"][question]["question"]
    question_answer = ar["results"][question]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
