from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.penup()
        self.move_y = 10
        self.move_x = 10
        self.in_speed = 0.1
        self.speed_up()

    def speed_up(self):
        self.speed(self.in_speed)
        

    def move(self):
        x= self.xcor() + self.move_x 
        y= self.ycor()  + self.move_y
        self.goto(x , y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.in_speed *= 4.5

    def reset_to(self):
        self.goto(0,0)
        self.in_speed = 0.1
        self.bounce_x()