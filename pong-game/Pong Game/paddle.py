from turtle import Turtle,Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.x = x
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.setting(self.x)
        self.move_with_key(self.x)
    
    # Fixing paddle's position
    def setting(self,x):
        self.penup()
        self.goto(x,0)

    
    # Paddle moving functionalities
    def move_with_key(self,x):
        def move_up():
            y = self.ycor()
            self.goto(x, y + 20)

        def move_down():
            y = self.ycor()
            self.goto(x, y - 20)

        screen.listen()


        # Right paddle control
        if (x > 0):
            screen.onkey(move_up , 'Up')
            screen.onkey(move_down, 'Down')
        

        # Left paddle control
        else:
            screen.onkey(move_up , 'u')
            screen.onkey(move_down, 'd')




