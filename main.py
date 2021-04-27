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

state_data = pandas.read_csv("50_states.csv")

state_names = state_data.state.to_list()

while game_is_on:

    answer_state = screen.textinput(title=f"Guess a State - {num_states_guessed}/50", prompt="What's another state name?")

    for state in state_names:
        if answer_state.title() == state:
            num_states_guessed += 1
            print('Do some turtle magic')
            x_cor = state_data[state_data.state == state]
            # y_cor =
            print(x_cor.x)
            title = Title()
            title.pin_title_to_map(150, 150, 'Hey girl')




turtle.mainloop()


























# screen.exitonclick()