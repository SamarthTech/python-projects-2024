# Static Face Detection Using Haar Cascade Classifier

## Project Overview

This project demonstrates a basic static face detection system using OpenCV and Haar Cascade Classifiers. The program loads an image, converts it to grayscale, and detects faces using a pre-trained Haar Cascade model. Once faces are detected, they are highlighted with a red rectangle drawn around them.

## Features
- Detects faces from a static image.
- Uses OpenCV's `CascadeClassifier` for face detection.
- Visualizes detected faces by drawing rectangles around them.

## Requirements

### 1. Python (version 3.x)
Ensure that Python is installed. You can download it from [Python's official website](https://www.python.org/).

### 2. Dependencies
Install the required Python packages by running:

```bash
pip install opencv-python
```

### 3. Haar Cascade XML File
You will need the Haar Cascade file for face detection. Download the `haarcascade_frontalface_default.xml` from the OpenCV GitHub repository [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Project Structure

```
face-detection/
│
├── students.jpg                # The static image used for face detection
├── haarcascade_frontalface_default.xml # Haar Cascade for face detection
└── image.py         # Python script for face detection
```


## How to Run

1. **Clone the repository** or download the files.
2. **Place an image** in the same directory as `image.py` and name it `students.jpg` (or modify the code to point to a different image).
3. **Download the Haar Cascade** file and ensure it is in the same directory as `image.py`.
4. Run the script:
    ```bash
    python image.py
    ```

The program will display the image with red rectangles around detected faces. Press any key to close the window.

## Customization
- **Tuning the face detection**: You can adjust the parameters in the `detectMultiScale` function to improve detection accuracy:
  - `scaleFactor` (default 1.1): Determines how much the image size is reduced at each image scale.
  - `minNeighbors` (default 1): Defines how many neighbors each rectangle should have to retain it.
  
## Notes
- Ensure the Haar Cascade XML file is correctly placed in your project directory.
- Face detection might not work well on images with poor lighting or at extreme angles.