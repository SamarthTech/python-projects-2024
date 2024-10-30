import turtle
import pandas

sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_states = []

while len(guessed_states)<50:


    s_input = turtle.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()
    print(s_input)

    if s_input=="Exit":
        missing_states = []
        for i in all_states:
            if i not in guessed_states:
                missing_states.append(i)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing states.csv")
        break

    #get mouseclick coordinates
    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)

    # turtle.mainloop() #-Alternative to exitonclick to keep the screen running #place at last like exitonclick

    if s_input in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == s_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(s_input)#state_data.state.item()
        guessed_states.append(s_input)

sc.exitonclick()