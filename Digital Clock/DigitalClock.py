import tkinter as tk
from time import strftime

def get_gradient_color(color1, color2, t):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:], 16)

    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)

    return f'#{r:02x}{g:02x}{b:02x}'

def update_background(step=0):
    t = step / 100
    color = get_gradient_color("#C6FFDD", "#f7797d", t)
    canvas.config(bg=color)
    label.config(bg=color)  

    step = (step + 1) % 100
    canvas.after(50, update_background, step)


def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")


canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)


label = tk.Label(canvas, font=('calibri', 50, 'bold'), fg='white')
label.place(relx=0.5, rely=0.5, anchor='center')

time()
update_background()


root.mainloop()
