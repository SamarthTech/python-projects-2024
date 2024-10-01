from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#2 game modes still under development

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("Snake-Game")
sc.tracer(0)

b= [(0,0), (-20,0), (-40,0)]
snake = Snake(b)
food = Food()
sb = Scoreboard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

on = True
while on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        sb.inc()
        snake.intro()

    x = snake.head.xcor()
    y = snake.head.ycor()
    if x==-300 or x==300 or y==-300 or y==300:
        sb.game_over()
        on = False

    # snake.cut()

    for i in snake.c[1:]:
        if snake.head.distance(i)<10:
            on = False
            sb.game_over()
            break















sc.exitonclick()