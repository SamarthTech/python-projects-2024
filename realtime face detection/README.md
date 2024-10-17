

# Face Detection using OpenCV

This project demonstrates a basic face detection system using OpenCV and Haar Cascades. It captures live video from the webcam, detects faces in real-time, and highlights them with a rectangle.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Installation

1. **Install OpenCV**  
   To install OpenCV, run the following command in your terminal:
   ```bash
   pip install opencv-python
   ```

2. **Download the Haar Cascade XML file**  
   The face detection model is based on Haar Cascades. You can download the required XML file for frontal face detection from the following [link](https://github.com/opencv/opencv/tree/master/data/haarcascades):

   Place the file (`haarcascade_frontalface_default.xml`) in the `model` folder of your project.

## How It Works

1. The script uses OpenCV to access the webcam and capture video frames.
2. Each frame is converted to grayscale for easier face detection.
3. The `CascadeClassifier` is used to detect faces, and rectangles are drawn around detected faces in the frame.
4. The program continuously displays the video feed with detected faces until the user presses the 'q' key to quit.

## Code Explanation

### Import Libraries
```python
import cv2
```
We import the OpenCV library for video capture and face detection.

### Load Haar Cascade
```python
harcascade = "model/haarcascade_frontalface_default.xml"
```
Load the pre-trained model for frontal face detection.

### Capture Video Feed
```python
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height
```
Open the default webcam and set the frame width and height.

### Detect Faces
```python
facecascade = cv2.CascadeClassifier(harcascade)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = facecascade.detectMultiScale(img_gray, 1.1, 4)
```
Convert each frame to grayscale, and detect faces using the `CascadeClassifier`.

### Display Video with Detected Faces
```python
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow("Face", img)
```
Draw rectangles around detected faces and display the video with the marked faces.

### Exit Condition
```python
if cv2.waitKey(1) & 0xff == ord('q'):
    break
```
Terminate the video capture when the 'q' key is pressed.

## Usage

1. Run the script:
   ```bash
   python face_detection.py
   ```
2. The webcam feed will open, and detected faces will be highlighted in real-time.
3. Press the 'q' key to stop the program.

## Troubleshooting

- **Webcam not working**: Ensure your webcam is connected and try restarting your system if the video feed doesn't appear.
- **No faces detected**: Ensure good lighting conditions and that your face is within the camera's frame.
