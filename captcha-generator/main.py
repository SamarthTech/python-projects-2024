# Importing the necessary packages
import random, string, tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.captchaLabel = Label(root, bg="lightskyblue4", borderwidth=3, relief="groove", width=33, height=6)
    root.captchaLabel.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    generateBTN = Button(root, width=10, text="GENERATE", command=generateCaptcha)
    generateBTN.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Defining a function named generateCaptcha() to generate captcha image of random string
def generateCaptcha():
    # Setting the width and height of the captchaImage Label
    root.captchaLabel.config(width=300, height=100)
    # Creating an object of ImageCaptcha() with height and width parameters
    captcha_image = ImageCaptcha(width=280, height=90)
    # Generating random string of random length using random library to be used as captcha text
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 7)))
    # Generating image of the captcha_text using the generate() method of captcha_image object
    captcha_data = captcha_image.generate(captcha_text)
    # Captch Image can be saved using the write() method of the captcha_image object of ImageCaptcha()
    # captcha_image.write(captcha_text, "IMAGE_NAME.png")
    # Opening the image of captcha_data using open() method of Image class which takes image as argument
    imageView = Image.open(captcha_data)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageView)
    # Configuring the label to display the frame
    root.captchaLabel.config(image=imageDisplay)
    # Keeping a reference
    root.captchaLabel.photo = imageDisplay

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color
root.geometry("325x170")
root.title("Captcha Generator")
root.config(background="black")

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()