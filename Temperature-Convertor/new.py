import tkinter as tk
from tkinter import messagebox

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"Result: {fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"Result: {celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create and place widgets
input_label = tk.Label(window, text="Enter Temperature:")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

c_to_f_button = tk.Button(window, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
c_to_f_button.pack()

f_to_c_button = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
f_to_c_button.pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
