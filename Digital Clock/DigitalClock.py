import tkinter as tk #to use tkinder module as tk in code
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def time():
    string=strftime('%H:%M:%S %p \n %D')#to display time in Hours:Minutes:Seconds format in onme line and display the date in the next line
    label.config(text=string)
    label.after(1000,time)

#setting font-sizeand style
label=tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='red')#set background color of clock as black and display time and date in red


label.pack(anchor='center')

time()

root.mainloop()