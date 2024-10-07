from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.goto(0,-300)
        self.hideturtle()
        self.pensize(1.5)
        self.draw_border()

    def draw_border(self):
        self.goto(0,300)