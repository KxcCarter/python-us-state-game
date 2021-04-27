from turtle import Turtle

FONT = ('Courier', 10, 'normal')

class Title(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def pin_title_to_map(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, False, align="center", font=FONT)