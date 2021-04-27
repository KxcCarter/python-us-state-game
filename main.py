import turtle
import pandas
from title_gen import Title

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
num_states_guessed = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while game_is_on:

    answer_state = screen.textinput(title=f"Guess a State - {num_states_guessed}/50", prompt="What's another state name?")

    if answer_state.title() in all_states:
        num_states_guessed += 1
        state_data = data[data.state == answer_state.title()]
        print(state_data.x)
        print(int(state_data.y))
        title = Title()
        title.pin_title_to_map(int(state_data.x), int(state_data.y), answer_state.title())

    if num_states_guessed == 50:
        game_is_on = False


turtle.mainloop()


# screen.exitonclick()