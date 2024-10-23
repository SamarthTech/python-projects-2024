from tkinter import Tk, Button, Label, Frame
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def convert_to_jpg():
    global image_label, filename_label, saved_label

    if image_path:
        # Open the image using PIL
        image = Image.open(image_path)

        # Convert the image to RGB if it has an RGBA color mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Convert the image to JPG format
        jpg_filename = image_path.replace('.png', '.jpg')
        image.save(jpg_filename, 'JPEG')

        saved_label.config(text=f"Saved as: {jpg_filename}")
        print(f"Image converted and saved as {jpg_filename}.")


def open_image():
    global image_path, image_label, filename_label

    # Open a file dialog to select an image file
    Tk().withdraw()
    image_path = askopenfilename(filetypes=[("PNG Files", ".png")])

    if image_path:
        # Open the image using PIL
        image = Image.open(image_path)

        # Resize the image to a square preview
        size = min(image.size)
        image = image.crop((0, 0, size, size))
        image = image.resize((400, 400))

        # Create a PhotoImage from the PIL image
        photo = ImageTk.PhotoImage(image)

        # Update the image label with the new image
        image_label.configure(image=photo)
        image_label.image = photo

        # Update the filename label
        filename_label.config(text=f"Selected file: {image_path}")

# Create a Tkinter window
window = Tk()
window.title("PNG to JPG Converter")
window.geometry("600x600")
window.resizable(False, False)

# Create a frame for the image label
image_frame = Frame(window, width=250, height=200, relief="solid")
image_frame.place(x=50, y=20)

# Create an image label for preview
image_label = Label(image_frame)
image_label.pack(padx=50, pady=20)

# Create a label for the selected filename
filename_label = Label(window, text="Selected file: None", font=("Arial", 12))
filename_label.place(x=0, y=470)

# Create a button to open the image
open_button = Button(window, text="Open Image", command=open_image, font=("Arial", 14))
open_button.place(x=0, y=500)

# Create a button to convert the image
convert_button = Button(window, text="Convert to JPG", command=convert_to_jpg, font=("Arial", 14))
convert_button.place(x=150, y=500)

# Create a label for the saved file
saved_label = Label(window, font=("Arial", 12))
saved_label.place(x=0, y=550)

previewtext_label = Label(window, text="Preview", font=("Arial", 18))
previewtext_label.place(x=250, y=10)

# Initialize the image path variable
image_path = None

# Start the Tkinter event loop
window.mainloop()
