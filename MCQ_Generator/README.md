# MCQ Generator App

This project implements a web application that generates multiple-choice questions (MCQs) from uploaded text-based documents. Users can upload PDF, DOCX, or TXT files, and the app will extract the text, then generate a specified number of MCQs using Google's Generative AI model. The generated MCQs can be downloaded as a text file or a PDF.

## Features

- **File Upload**: Supports PDF, DOCX, and TXT file formats for text extraction.
- **MCQ Generation**: Generates multiple-choice questions (MCQs) based on the uploaded content.
- **Downloadable Results**: Generated MCQs can be downloaded as a text file or PDF.
- **REST API**: Allows users to upload files and generate MCQs via a web interface.
  
## Technologies Used

- **Flask**: Web framework used to build the application.
- **Google Generative AI**: AI model used for generating MCQs.
- **PDFPlumber**: For extracting text from PDFs.
- **python-docx**: For extracting text from DOCX files.
- **FPDF**: For generating PDF files.
  
## Installation

### Prerequisites

- Python 3.7+
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Google API key:
   ```bash
   export GOOGLE_API_KEY="your_google_api_key"
   ```

### Run the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000` to access the app.

## Usage

1. Upload a PDF, DOCX, or TXT file.
2. Specify the number of MCQs to generate.
3. The app will extract the text, generate the MCQs, and display them.
4. Download the MCQs as either a text file or PDF.

## API Endpoints

- `/` : Main page for uploading files and specifying the number of MCQs.
- `/generate` : Handles the file upload, text extraction, and MCQ generation.
- `/download/<filename>` : Allows downloading the generated MCQs.

## Example

1. Upload a file (e.g., `document.pdf`).
2. Specify the number of MCQs (e.g., `5`).
3. View and download the generated MCQs in both text and PDF formats.

## Folder Structure

- `uploads/`: Stores the uploaded files.
- `results/`: Stores the generated MCQs in both text and PDF formats.

## Future Improvements

- **Advanced MCQ Generation**: Implement additional features like difficulty levels for MCQs.
- **Enhanced UI**: Build a more interactive and user-friendly web interface.
- **Text Preprocessing**: Implement more advanced text preprocessing techniques for better MCQ generation.
