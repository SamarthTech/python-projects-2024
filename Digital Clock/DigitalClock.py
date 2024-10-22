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
root.mainloop()
