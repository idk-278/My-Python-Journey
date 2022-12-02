import turtle
import pandas
import time

correct_answers = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
check_continue = True
screen.tracer(0)
print(states_list)

# timey.hideturtle()

time_check = True


def countdown(t):
    timey = turtle.Turtle()
    timey.pu()
    timey.goto(0, 0)  # 312 287
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        print(timer)
        timey.write(arg=timer, align="right", font=('Arial', 8, 'normal'))


while check_continue:
    difficulty_state = screen.textinput(
        title="Difficulty level",
        prompt=
        "Choose a difficulty level:\n"
        "Easy (5 min)\n"
        "Intermediate (3 min)\n"
        "Hard (2 min)\n"
        "God Mode (1 min, -1 from the score if answered wrong)"
    )
    difficulty_state_lower = difficulty_state.lower
    break

countdown(120)

print(check_continue)

while check_continue:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state_title = answer_state.title()
    for state in states_list:
        if answer_state_title == state:
            correct_answers += 1
            staty = turtle.Turtle()
            staty.hideturtle()
            staty.pu()
            row = data[data.state == answer_state_title]
            for index, rows in row.iterrows():
                list_ = [rows.state, rows.x, rows.y]
            print(list_)
            staty.goto(list_[1], list_[2])
            staty.write(arg=answer_state_title,
                        align="center",
                        font=('Arial', 8, 'normal'))
            print(check_continue)
            # elif answer_state_title != state:
            #    if difficulty_state == "god mode":
            #        correct_answers -= 1

# def get_mouse_click_cor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop()
