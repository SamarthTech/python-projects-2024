import turtle
import pandas

'''
 
'''

screen = turtle.Screen()
image = "WB_outline_map.gif"
screen.addshape(image)
turtle.shape(image)

dist = ["Cooch Behar" , "Alipurduar" , "Jalpaiguri" , "Kalimpomg" , "Darjeeling" , "Uttar Dinajpur" , "Dakshin Dinajpur" , "Malda" , "Murshidabad" , "Birbhum" , "Pashchim Bardhaman" , "Purba Bardhaman" , "Nadia", "North 24 Parganas" , "Hoogly" , "Bankura" , "Purulia" , "Jhargram" , "Pashchim Midnapur" , "Howrah" , "Kolkata" , "South 24 Parganas" , "Purba Medinipur"]

x_coor = [48.0 , 47.0 , 26.0 , 19.0, 10.0, 1.0, 26.0, 8.0 , 8.0, -11.0 , -23.0, 0.0 , 17.0 , 29.0, 13.0, -28.0, -50.0, -32.0, -18.0, 6.0, 16.0, 18.0, -9.0]

y_coor = [87.0 ,101.0, 101.0, 115.0, 107.0, 71.0, 52.0, 42.0, 9.0, -4.0, -12.0 , -23.0,-13.0, -41.0, -40.0, -27.0, -21.0, -62.0,-55.0, -53.0,-53.0,-64.0 , -74.0]

# Findin coordinates of the districts on the map
# def on_mouse (x, y):
#     print(x,y)

# turtle.onscreenclick(on_mouse)
    
dist_dict = {
    "districts" : dist,
    "x" : x_coor,
    "y" : y_coor
}

dist_df = pandas.DataFrame(dist_dict)

dist_df.to_csv("District_Datas.csv")



turtle.mainloop()