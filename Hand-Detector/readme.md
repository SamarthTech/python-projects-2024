# Hand Tracking with MediaPipe

A real-time hand tracking application using OpenCV and MediaPipe that captures video from your webcam and detects hand landmarks.

## Features

- Real-time hand detection and tracking
- Visual display of hand landmarks and connections
- Mirror-flipped display for intuitive interaction
- Low-latency processing with configurable detection confidence

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

```bash
pip install opencv-python
pip install mediapipe
```

## System Requirements

- Python 3.7 or higher
- Webcam/camera device
- Sufficient CPU for real-time processing


## Usage

1. Run the main script:
```bash
python main.py
```

2. The application will open your webcam feed and start tracking hands.
3. Press 'q' to quit the application.

## Configuration

The application uses the following default settings which can be modified in `main.py`:

- `model_complexity=0`: Lower complexity for better performance
- `min_detection_confidence=0.5`: Minimum confidence value for hand detection
- `min_tracking_confidence=0.5`: Minimum confidence value for hand tracking

## How It Works

1. Captures video feed from the default camera (index 0)
2. Converts each frame from BGR to RGB color space for MediaPipe processing
3. Processes the frame to detect hands and their landmarks
4. Draws landmarks and connections on detected hands
5. Displays the processed frame with a horizontal flip for mirror-like interaction

## Controls

- **Q**: Quit the application
- The video feed is automatically flipped horizontally for a more intuitive experience

## Troubleshooting

Common issues and solutions:

1. **Camera not found**: 
   - Ensure your webcam is properly connected
   - Try changing the camera index in `cv2.VideoCapture(0)`

2. **Performance issues**:
   - Lower the `model_complexity` parameter
   - Ensure your system meets the minimum requirements

---
