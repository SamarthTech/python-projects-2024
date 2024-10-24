import calendar
yy = int (input("Enter year:"))
mm = int (input("Enter month:"))
from tkinter import *
def show_calendar(yy, mm):
    cal = calendar.month(yy, mm)
    cal_window = Tk()
    cal_window.title(f'Calendar - {mm}/{yy}')
    cal_label = Label(cal_window, text=cal, font='Consolas 8 bold')
    cal_label.pack()
    cal_window.mainloop()
    
print(calendar.month(yy,mm))
show_calendar(yy, mm)

