from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(pos,270)
        self.show()

    def incr_score(self):
        self.score += 1
        self.clear()
        self.show()

    def show(self):
        self.write(arg= f"{self.score}",align= 'center' , font=("Arial" , 15, 'normal'))
    

