import tkinter as tk #to use tkinder module as tk in code
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def time():
    string=strftime('%H:%M:%S %p \n %D')#to display time in Hours:Minutes:Seconds format in onme line and display the date in the next line
    label.config(text=string)
    label.after(1000,time)

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

# Call the time function to start the clock
time()

# Bind the "Shift + D" key to toggle between light and dark modes
root.bind('<Shift-D>', toggle_mode)


root.mainloop()
