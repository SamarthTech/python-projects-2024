import turtle

my_screen= turtle.Screen()
my_turtle = turtle.Turtle()


# Creating Functions
def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_counterclockwise():
    my_turtle.left(10)

def turn_clockwise():
    my_turtle.right(10)

def color_change_red():
    my_turtle.color('red')

def color_change_green():
    my_turtle.color('green')

def color_change_blue():
    my_turtle.color('blue')

def unset_color():
    my_turtle.color('black')

def bolder():
    my_turtle.width(5)

def lighter():
    my_turtle.width(1)

def clear_screen():
    my_screen.resetscreen()
    

# Adding Functionalities
my_screen.listen()
my_screen.onkey(move_forward ,'space')
my_screen.onkey(move_backward ,'Tab')
my_screen.onkey(turn_counterclockwise ,'p')
my_screen.onkey(turn_clockwise ,'n')
my_screen.onkey(color_change_red , 'r')
my_screen.onkey(color_change_green , 'g')
my_screen.onkey(color_change_blue , 'b')
my_screen.onkey(unset_color , 'u')
my_screen.onkey(bolder, '+')
my_screen.onkey(lighter, '-')
my_screen.onkey(clear_screen ,'c')

my_screen.exitonclick()