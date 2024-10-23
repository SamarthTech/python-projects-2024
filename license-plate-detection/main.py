import numpy as np
import cv2
import imutils
import pytesseract
import os

# Specify the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to display an image and wait for a key press
def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read the image
image_path = os.path.join('Car Images', '7.jpg')
image = cv2.imread(image_path)

# Resize the image
image = imutils.resize(image, width=500)
display_image("Original Image", image)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image("1 - Grayscale Conversion", gray)

# Apply a bilateral filter for noise removal
gray = cv2.bilateralFilter(gray, 11, 17, 17)
display_image("2 - Bilateral Filter", gray)

# Detect edges using Canny
edged = cv2.Canny(gray, 170, 200)
display_image("3 - Canny Edges", edged)

# Find contours based on edges
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours on a copy of the original image
img1 = image.copy()
cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
display_image("4 - All Contours", img1)

# Sort contours based on area, keeping only the largest 30
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCnt = None  # Placeholder for the number plate contour

# Draw top 30 contours on a copy of the original image
img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)
display_image("5 - Top 30 Contours", img2)

# Loop through the contours to find the one that approximates the shape of a license plate
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    if len(approx) == 4:  # Contour with 4 corners detected
        NumberPlateCnt = approx

        # Extract the bounding rectangle for the detected contour
        x, y, w, h = cv2.boundingRect(c)
        new_img = gray[y:y + h, x:x + w]

        # Save the cropped image of the potential number plate
        cropped_img_path = os.path.join('Cropped Images-Text', '7.png')
        cv2.imwrite(cropped_img_path, new_img)
        break

# Draw the selected contour (the detected number plate) on the original image
if NumberPlateCnt is not None:
    cv2.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3)
    display_image("Final Image With Number Plate Detected", image)

# Display the cropped image
display_image("Cropped Image", cv2.imread(cropped_img_path))

# Use Tesseract to extract text from the cropped image
text = pytesseract.image_to_string(cropped_img_path, lang='eng')
print("Detected Number Plate Text:", text)
