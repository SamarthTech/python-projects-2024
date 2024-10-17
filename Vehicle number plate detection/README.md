
# Vehicle Number Plate Detection using Machine Learning

This project implements a Vehicle Number Plate Detection system using Machine Learning techniques. The system detects vehicle number plates from images or video streams and extracts the text from the plates using Optical Character Recognition (OCR).

## Features
- **Plate Detection:** Detects and extracts vehicle number plates from images.
- **OCR:** Uses `EasyOCR` to recognize and extract text from detected plates.
- **Flask API:** A simple RESTful API built with Flask to allow easy integration and deployment.
- **Image/Video Input:** Can process images or video streams for real-time detection.

## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.6+
- pip (Python package installer)

### Install Dependencies
Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

Here is the list of the main dependencies:
- **easyOCR==1.1.7:** Optical Character Recognition for detecting text.
- **opencv-python==4.4.0.40:** Library for real-time computer vision.
- **Flask==1.1.2:** Web framework for building the API.
- **torch==1.4.0** and **torchvision==0.5.0:** For neural network-based processing (used by `easyOCR`).

### Additional Libraries
Other libraries like `matplotlib`, `numpy`, `scikit-image`, and `pandas` are included for image processing and data manipulation.

### TensorFlow
This project is based on TensorFlow 1.14.0, which is also listed in the requirements for any additional ML operations.

## Usage

### Running the Flask Server

1. **Start the Flask API:**

    Once all dependencies are installed, run the Flask server using:
    ```bash
    python app.py
    ```

    The API will be available at `http://127.0.0.1:5000`.

    ```
2. **Response:**
    The server will return a JSON object with the detected plate number and the bounding box coordinates.

## Project Structure

```
├── app.py                  # Flask API for number plate detection
├── requirements.txt         # List of dependencies
├── static/                  # Folder for storing static assets (CSS, JS, images)
└── README.md                # Project documentation
```

## Customization

- **Model:** The current OCR is based on `easyOCR`, which can be modified or replaced with a different model.
- **Improving Accuracy:** Adjust image preprocessing in `detect_plate.py` for better plate detection performance (e.g., thresholding, edge detection using OpenCV).
  

