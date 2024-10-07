from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
from table_boundary import Border 
import time


# Making the feild ready
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)
right_paddle = Paddle(280)
left_paddle = Paddle(-280)
right_score = ScoreBoard(50)
left_score = ScoreBoard(-50)
ball = Ball()
border = Border()



# Start play
game = True
while game:
    time.sleep(0.1)
    my_screen.update()
    
    ball.move()

    # When ball collides with the top or down wall

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # When ball collides with paddles

    if ball.distance(right_paddle) < 50 and ball.xcor() > 260 or ball.distance(left_paddle) < 50 and ball.xcor() < -260:
        ball.bounce_x()
    
    
    # When the ball exceeds the right boundary left paddle will get point 
    elif ball.xcor() >= 290:
        ball.reset_to()
        left_score.incr_score()

    # When the ball exceeds the left boundary right paddle will get point 
    elif ball.xcor() <= -290:
        ball.reset_to()
        right_score.incr_score()
    
    

my_screen.exitonclick()