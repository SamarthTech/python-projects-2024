import tkinter as tk
import random
import time
from PIL import Image, ImageTk

# Function to roll the dice and show animation
def roll_dice_animation():
    global dice_value
    dice_value = random.randint(1, 6)
    dice_image = dice_images[dice_value - 1]
    dice_label.config(image=dice_image)
    dice_label.image = dice_image
    root.after(100, roll_dice_animation_step)

def roll_dice_animation_step():
    global animation_step
    if animation_step < 10:
        dice_value = random.randint(1, 6)
        dice_image = dice_images[dice_value - 1]
        dice_label.config(image=dice_image)
        dice_label.image = dice_image
        animation_step += 1
        root.after(100, roll_dice_animation_step)
    else:
        result_label.config(text=f"You rolled a {dice_value}!")
        animation_step = 0  # Reset the animation step

# Function to start rolling animation when the button is clicked
def roll_dice():
    for _ in range(10): 
        dice_value = random.randint(1, 6)
        dice_image = dice_images[dice_value - 1]
        dice_label.config(image=dice_image)
        dice_label.image = dice_image
        root.update()
        time.sleep(0.1)
    result_label.config(text=f"You rolled a {dice_value}!")

# Initialize the main window
root = tk.Tk()
root.title("Dice Roller")

# Get the screen size and adjust window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width, window_height = 400, 400
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Load dice images
dice_images = [
    ImageTk.PhotoImage(Image.open(f"dice/dice{i}.png").resize((150, 150))) for i in range(1, 7)
]

# Add title label
title_label = tk.Label(root, text="Welcome to Dice Roller", font=("Helvetica", 16), bg="#282828", fg="#FFFFFF", pady=10)
title_label.pack(fill=tk.X)

# Add label to display the dice image
dice_label = tk.Label(root)
dice_label.pack(pady=20)

# Add label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 18), fg="#333333")
result_label.pack(pady=20)

# Add roll button
roll_button = tk.Button(root, text="Roll the Dice", command=roll_dice, font=("Helvetica", 14), bg="#4CAF50", fg="white", width=15, height=2)
roll_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
