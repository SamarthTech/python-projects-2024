import turtle
import pandas as pd
import time


screen = turtle.Screen()

image = "WB_outline_map.gif"
screen.addshape(image)
turtle.shape(image)


dists_infos = pd.read_csv("District_Datas.csv")
dists_list = dists_infos["districts"].to_list()


correct = 0
done = False
while len(dists_list) > 0:
    answer = screen.textinput(f"{correct}/23 is correct" , "Guess the name of a state").title()

    if answer == "Exit" :
        break


    if answer in dists_list:
        print(answer)
        s = dists_infos[dists_infos["districts"] == answer]
        x = s.x.item()
        y = s.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x , y)
        t.write(arg=f"{answer}" , font=("Arial" , 8 , "normal"))
        dists_list.remove(answer)
        correct += 1
        time.sleep(0.5)

    
left_names = {
    "States" : dists_list
}

df = pd.DataFrame(dists_list)

df.to_csv("$districts_names_to_learn$.csv")




        





screen.exitonclick()