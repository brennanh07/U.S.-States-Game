from turtle import Screen
import pandas as pd
from state import State

screen = Screen()
screen.setup(width=725, height=500)
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states = list(data.state)
coordinates = list(zip(list(data.x), list(data.y)))

score = 0

play_game = True
while play_game:
    answer = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's the name of another state?").title()
    if answer in states:
        state = State()
        state.write_state(coordinate=coordinates[states.index(answer)], state=answer)

        coordinates.remove(coordinates[states.index(answer)])
        states.remove(answer)

        score += 1

    if score == 50:
        play_game = False

screen.exitonclick()






