import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %d %B %Y')
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, time_update)

root = tk.Tk()
root.title('Digital Clock')

root.configure(bg='black')

clock_label = tk.Label(root, font=('calibri', 50, 'bold'), bg='black', fg='green')
clock_label.pack(pady=20)

date_label = tk.Label(root, font=('calibri', 20), bg='black', fg='green')
date_label.pack()

time_update()
=======
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

# Function to toggle between dark mode and light mode
def toggle_mode(event=None):
    global is_dark_mode
    if is_dark_mode:
        # Switch to light mode
        label.config(background='white', foreground='black')
        root.config(bg='white')
        is_dark_mode = False
    else:
        # Switch back to dark mode
        label.config(background='black', foreground='red')
        root.config(bg='black')
        is_dark_mode = True

# Label to display the clock
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='red')

# Pack the label
label.pack(anchor='center')

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

label = tk.Label(canvas, font=('calibri', 50, 'bold'), fg='white')
label.place(relx=0.5, rely=0.5, anchor='center')

# Bind the "Shift + D" key to toggle between light and dark modes
root.bind('<Shift-D>', toggle_mode)

# Call the time function to start the clock
time()
update_background()
root.mainloop()
