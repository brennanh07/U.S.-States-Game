from turtle import Turtle


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')

    def write_state(self, state, coordinate):
        self.goto(coordinate)
        self.write(state, align='center', font=('Arial', 8, 'bold'))

