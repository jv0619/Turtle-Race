from turtle import Turtle as T, Screen as S
from random import choice, randrange as ran

screen = S()
screen.setup(700, 500)
screen.colormode(255)
pen = T()
pen.speed("fastest")
pen.ht()
n = 5
y = -1*(600 - (50*n))//2


def make_setup(start_pos: tuple, length: int, breath: int, n: int, y):
    pen.up()
    pen.goto(start_pos)
    pen.down()
    pen.color("#F0EEED", "#2E3840")
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.fd(breath)
        else:
            pen.fd(length)
        pen.lt(90)
    pen.end_fill()
    for _ in range(n//2):
        y += 50
        pen.sety(y)
        pen.fd(breath)
        y += 50
        pen.sety(y)
        pen.bk(breath)


def set_title():
    pen.up()
    pen.goto(-260, 150)
    pen.down()
    pen.color((64, 89, 51))
    screen.bgcolor("#9DC08B")
    pen.write("T U R T L E 'S G A M E", font=("Arial", 36, "bold"))


def write_finish():
    title = ["\U0001F3C1", "F", "I", "N", "I", "S", 'H', "\U0001F3C1"]
    ypos = 0
    xpos = 280
    pen.up()
    pen.setpos(xpos, ypos)
    for i in title:
        if i == "\U0001F3C1":
            pen.color("white")
            pen.write(i, align = "center", font=("Arial", 20, 'normal'))
        pen.color("#40513B")
        pen.write(i, align="center", font=("Arial", 16, "bold"))
        pen.up()
        ypos -= 20
        pen.setpos(xpos, ypos)




def ready_turtles():
    pos = y+25
    for i in range(n):
        turtles.append(T())
        turtles[i].color(colors[i])
        turtles[i].shape("turtle")
        turtles[i].up()
        turtles[i].goto(-260, pos)
        pos += 50


def set_speed():
    speeds = ["slowest", "slow", "normal", "fast", "fastest"]
    for i in range(n):
        turtles[i].speed(choice(speeds))


def move():
    goal = 250
    for i in range(n):
        turtles[ran(0, 5)].fd(5)
        positions = [tur.pos()[0] for tur in turtles]
        max_ind = positions.index(max(positions))
        if positions[max_ind] >= goal:
            return colors[max_ind]
    return 0


def re_ready():
    pos = y+25
    for i in range(n):
        turtles[i].speed("fastest")
        turtles[i].goto(-260, pos)
        pos += 50


def play_game():
    isFinish = False
    while not isFinish:
        set_speed()
        winner = move()
        if winner in colors:
            isFinish = True

    return winner


set_title()
write_finish()
make_setup((-250, y), n*50, 500, 5, y)
# turtles = []
# colors = ["red", "blue", "yellow", "green", "white"]
# ready_turtles()
# is_want_to_play = True
# user_want = ""
#
#
# while is_want_to_play:
#     if user_want not in colors:
#         user_choice = screen.textinput("Make a Bet", prompt="Which turtle going to be win: ")
#     winner = play_game()
#     text = "Oho... You Lost... \U0001F643"
#     if winner == user_choice:
#         text = "You Win... \U0001F929 \U0001F973"
#     user_want = screen.textinput(text, prompt="Do you want to play again ? : ")
#     if user_want == "yes":
#         re_ready()
#     elif user_want == "no":
#         is_want_to_play = False
#     elif user_want in colors:
#         re_ready()
#     else:
#         is_want_to_play = False

screen.exitonclick()