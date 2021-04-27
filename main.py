import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

num_states_guessed = 0

state_data = pandas.read_csv("50_states.csv")

state_names = state_data.state.to_list()

# print(state_names)

answer_state = screen.textinput(title=f"Guess a State - {num_states_guessed}/50", prompt="What's another state name?")

if answer_state in state_names:
    print('Wow DAWG it WORKTH')
    num_states_guessed += 1
    print('Do some turtle magic')


print(answer_state)


turtle.mainloop()


























# screen.exitonclick()