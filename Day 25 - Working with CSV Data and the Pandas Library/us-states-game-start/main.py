import turtle as tu
import pandas as pd

screen = tu.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image)
tu.shape(image)

data = pd.read_csv("50_states.csv")
states = data["state"].tolist()

correct_count = 0
correct_states = []

while correct_count < 50:
    answer_state = str(screen.textinput(title=f"You guessed: {correct_count}/50", prompt="Enter State name."))\
        .capitalize()

    if answer_state.lower() == "exit":
        break
    elif answer_state in states:
        correct_count += 1
        t = tu.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        states.remove(answer_state)
        correct_states.append(answer_state)


final_dict = {
    "Missing States": states
}
df = pd.DataFrame(final_dict)
df.to_csv("missing_states.csv")


tu.mainloop()  # Alternative for screen.exitonclick()
