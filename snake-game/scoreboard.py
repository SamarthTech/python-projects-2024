from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.upd()

    def upd(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def inc(self):
        self.score+=1
        self.clear()
        self.upd()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))


