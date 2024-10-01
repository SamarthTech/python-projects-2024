from turtle import Turtle
movee = 20
import time

class Snake:

     def __init__(self, b):
         self.c = []
         for i in b:
             tim = Turtle()
             tim.color("white")
             tim.shape("square")
             tim.penup()
             tim.goto(i)
             self.c.append(tim)
         self.head = self.c[0]

     def intro(self):
         tim = Turtle()
         tim.color("white")
         tim.shape("square")
         tim.penup()
         tim.goto(x=self.c[len(self.c) - 1].xcor(), y= self.c[len(self.c) - 1].ycor())
         self.c.append(tim)






     def move(self):
         for i in range(len(self.c)-1, 0, -1):
             x_cor = self.c[i - 1].xcor()
             y_cor = self.c[i - 1].ycor()
             self.c[i].goto(x_cor, y_cor)
         self.c[0].fd(movee)

     def up(self):
         if self.c[0].heading()!=270:
             self.c[0].setheading(90)

     def down(self):
         if self.c[0].heading() != 90:
             self.c[0].setheading(270)

     def left(self):
         if self.c[0].heading() != 0:
             self.c[0].setheading(180)

     def right(self):
         if self.c[0].heading() != 180:
             self.c[0].setheading(0)

     # def cut(self):
     #     for i in self.c[1:]:
     #         if self.head.distance(i)<10:
     #             for j in range(len(self.c)-1,self.c.index(i),-1):
     #                 self.c[j].hideturtle()
     #                 self.c.pop(j)


