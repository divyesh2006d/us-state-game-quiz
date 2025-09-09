import pandas as pd
from turtle import Turtle, Screen

# Setup screen

s = Screen()
s.setup(width=725, height=491)
s.bgpic("blank_states_img.gif")

# Load CSV into DataFrame
file = pd.read_csv("50_states.csv")

# print(file)
# Get user input

guss = []

while len(guss) < 50:

    answer_state = s.textinput(title="US State Game", prompt="Enter a state:").title()

    if answer_state is None:
        break

    if answer_state == "Exit":
        missing = []
        for st in file.state:
            if st not in guss:
                missing.append(st)
        n = pd.DataFrame(missing)
        n.to_csv("missing.csv")
        print(n)
        break


    # If the state exists in CSV
    if answer_state in file.state.values and answer_state not in guss:
        guss.append(answer_state)
        # Get row for that state
        state_data = file[file.state == answer_state]

        # Create a turtle to write the name
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))   # move to state coordinates
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

# s.exitonclick()
