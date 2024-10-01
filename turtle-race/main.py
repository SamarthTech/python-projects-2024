from itertools import filterfalse
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

g_over = Turtle()
g_over.color("Black")
g_over.hideturtle()
g_over.penup()

checkster = 0
for z in colors:
    if user_bet != z:
        checkster+=1;

bet_on = False
if checkster==5:
    bet_on=True

if bet_on == False:
    g_over.write("Race not held because of wrong option",align="center", font=("Arial", 18, "normal"))




if bet_on:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                g_over.write("You Won!!!!!", align="center", font=("Arial", 22, "normal"))
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                g_over.write("Loser", align="center", font=("Arial", 22, "normal"))

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
