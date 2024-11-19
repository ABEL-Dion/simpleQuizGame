import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.tolist()

def write_state_name(name, x, y):
    markers = turtle.Turtle()
    markers.hideturtle()
    markers.penup()
    markers.goto(x, y)
    markers.write(name, align="center", font=("Arial", 9, "normal"))

marker = turtle.Turtle()
marker.hideturtle()
marker.penup()

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()

is_on = True
correct_guess = []
score = 0

try:
    with open("score.txt", "r") as high_score:
        highscore = int(high_score.read())
except FileNotFoundError:
    highscore = 0

while is_on:
    score_turtle.clear()
    score_turtle.goto(0, 260)
    score_turtle.write(f"Score: {score}  Highscore: {highscore}", align="center", font=("Arial", 14, "normal"))

    # Get user input
    answer = screen.textinput("Welcome to the quiz game", "Enter the guess of your state")

    if answer is None:
        is_on = False
        screen.bye()
        break
    if answer.title() in correct_guess:
        print("you have guessed it already ")
        continue
    for state in states_list:
        if state == answer.title():
            matching_row = states[states['state'] == state]
            correct_guess.append(state)
            score += 1

            if not matching_row.empty:
                xcor = int(matching_row['x'].values[0])
                ycor = int(matching_row['y'].values[0])
                marker.penup()
                marker.goto(xcor, ycor)
                write_state_name(state, xcor, ycor)

    if score > highscore:
        highscore = score
        with open("score.txt", "w") as score_file:
            score_file.write(f"{highscore}")