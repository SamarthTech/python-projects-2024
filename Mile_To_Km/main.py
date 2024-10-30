from tkinter import *

FONT = ("Arial" , 10, "normal")


def miles_to_km(n):
    try:
        num = int(n)
        return num * 1.609
    except UnboundLocalError and ValueError:
        return "Not A Number"
    
    

def show_value():
    n = input.get()
    ans = miles_to_km(n)
    answer.config(text=ans)



window = Tk()
window.minsize(width=600, height=300)
window.title("Miles To Km Converter")
window.config(padx=50, pady=50)

label1 = Label(text="is equal to", font= FONT)
label1.grid(column=0, row=1)
label1.config(padx= 100, pady =50)


input = Entry(width=30)
input.grid(column=1, row=0)

label2 = Label(text="Miles" , font= FONT)
label2.grid(column=2, row=0)

answer = Label(text="0",font=FONT)
answer.grid(column=1, row=1)
answer.config(pady= 50)

label3 = Label(text="Km" , font=FONT)
label3.grid(column=2, row=1)
label3.config(pady= 50)

btn= Button(text="Calculate" , width=30, command=show_value)
btn.grid(column=1, row=2)


window.mainloop()