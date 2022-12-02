import turtle
import pandas
import time

correct_answers = 49
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
check_continue = True
FONT = ("Arial", 15, "normal")
print(states_list)

# timey.hideturtle()

time_check = True
tom = turtle.Turtle()
tom.speed(0)
tom.hideturtle()
tom.pu()
tom.goto(312, 287)


# def countdown(t):
#     tom.goto(312, 287)  # 312 287
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         time.sleep(1)
#         t -= 1
#         return timer


def countdown(time_):
    tom.clear()
    if check_continue:
        if time_ > 0:
            mins, secs = divmod(time_, 60)
            new_time = '{:02d}:{:02d}'.format(mins, secs)
            tom.write(new_time, align='center', font=FONT)
            screen.ontimer(lambda: countdown(time_ - 1), 1000)
        else:
            tom.write("TIME OVER!!!", align='center', font=FONT)


while check_continue:
    difficulty_state = screen.textinput(
        title="Difficulty level",
        prompt=
        "Choose a difficulty level:\n"
        "Easy (5 min)\n"
        "Intermediate (3 min)\n"
        "Hard (2 min)\n"
        "God Mode (1 min, -1 from the score if answered wrong)".lower()
    )
    break

if difficulty_state == "easy":
    countdown(300)
elif difficulty_state == "intermediate":
    countdown(180)
elif difficulty_state == "hard":
    countdown(120)
elif difficulty_state == "god mode":
    countdown(90)

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
                list_1 = [rows.state, rows.x, rows.y]
            print(list_1)
            staty.goto(list_1[1], list_1[2])
            staty.write(arg=answer_state_title,
                        align="center",
                        font=('Arial', 8, 'normal'))
            print(check_continue)
    if answer_state_title not in states_list:
        if difficulty_state == "god mode":
            correct_answers -= 1

if correct_answers >= 50:
    tom.clear()
    tom.write("YOU WON!!", align='center', font=FONT)
    if difficulty_state == "god mode":
        tom.write("YOU CLEARED GOD MODE!!", align='center', font=FONT)
        check_continue = False
    check_continue = False

# def get_mouse_click_cor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop()
screen.mainloop()
