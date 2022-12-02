import turtle
import pandas

correct_answers = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
check_continue = True
print(states_list)

while check_continue:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    answer_state_title = answer_state.title()
    for state in states_list:
        if answer_state_title == state:
            correct_answers += 1
            print(correct_answers)
            check_continue = True
            staty = turtle.Turtle()
            staty.hideturtle()
            staty.pu()
            row = data[data.state == answer_state_title]
            for index, rows in row.iterrows():
                list_ = [rows.state, rows.x, rows.y]
            print(list_)
            staty.goto(list_[1], list_[2])
            staty.write(arg=answer_state_title, align="center", font=('Arial', 8, 'normal'))
            print(check_continue)


def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop()
