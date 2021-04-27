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

    def annouce_win(self):
        self.goto(0, 0)
        self.write("You Win!", False, align='center', font=('Courier', 30, 'bold'))