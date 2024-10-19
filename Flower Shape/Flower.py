from turtle import*
import colorsys

speed(0)#set speed of drawing

bgcolor("black")#set background color

h=0

for i in range(16):
    for j in range(15):
        cl=colorsys.hsv_to_rgb(h,1,1)
        color(cl)

        h+=0.01

        right(90)
        circle(150-j*6,90)
        left(90)
        circle(150-j*6,90)

        right(180)
    circle(40,24)

done()

    

