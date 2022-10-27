import turtle

import pandas
import pandas as pd
from board_states import states_names

screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.DataFrame(pd.read_csv("50_states.csv"))
states = data["state"]

statess = states.tolist()
states_upper = [stat.upper() for stat in statess]


guessed = []

game = True
while game:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    missing = list(set(statess) - set(guessed))
    missing_df = pd.DataFrame(missing)
    # if answer_state == "Exit":
    #     with open("missing_state.csv", "w") as file:
    #         missing_pd = missing_df.to_csv(file)
    # if answer_state in statess:
    #     guessed.append(answer_state)
    #     states_names((int(data[data["state"] == answer_state]["x"]), int(data[data["state"] == answer_state]["y"])),
    #                  data[data["state"] == answer_state]["state"].item())

    if answer_state == "Exit":
        missing_states = []
        for state in statess:
            if state not in guessed:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        missing = [x for x in statess if x not in guessed]


