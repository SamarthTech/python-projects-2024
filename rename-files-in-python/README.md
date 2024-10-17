# File Renamer

A Python GUI application for batch renaming files with a user-friendly interface. This tool allows you to rename multiple files at once using customizable patterns and supports both individual file and folder selection.

## Features

- **Multiple Selection Methods**
  - Select individual files
  - Select entire folders
  - Option to include subfolders
  - File extension filtering

- **Customizable Renaming Options**
  - Custom prefix for new filenames
  - Configurable starting number
  - Adjustable number padding (e.g., 01, 001)
  - Preview changes before applying

- **Safety Features**
  - Preview functionality to review changes
  - File collision detection
  - Error handling
  - Confirmation dialogs for existing files

## Requirements

- Python 3.x
- tkinter (usually comes with Python)

## Screenshot  

![alt text](<Screenshot 2024-10-17 122547.png>)  


## Installation

1. Clone this repository or download the script:
```bash
git clone <repository-url>
```

2. Ensure Python 3.x is installed on your system
3. No additional dependencies needed as tkinter comes with Python

## Usage

1. Run the script:
```bash
python main.py
```

2. Using the application:

   a. **Select Files to Rename:**
   - Click "Select Files" to choose individual files, or
   - Click "Select Folder" to select an entire folder
   - Optionally specify file extensions to filter (e.g., .jpg,.png)
   - Choose whether to include subfolders

   b. **Configure Renaming Options:**
   - Enter a prefix for the new filenames
   - Set the starting number
   - Set the number of padding digits

   c. **Preview and Apply:**
   - Click "Preview Changes" to see how files will be renamed
   - Review the changes in the preview list
   - Click "Apply Rename" to perform the renaming

## Interface Guide

### Main Controls
- **Select Files**: Choose individual files to rename
- **Select Folder**: Choose a folder containing files to rename
- **Clear Selection**: Remove all selected files from the list

### Filter Options
- **Extensions**: Enter file extensions to filter (e.g., .jpg,.png)
- **Include Subfolders**: Check to include files in subfolders

### Renaming Options
- **Prefix**: Text to add before the number
- **Start Number**: First number in the sequence
- **Padding Digits**: Number of digits to use (e.g., 2 digits: 01, 02, 03)

### Preview Area
- Shows original filename and new filename
- Scrollable list for many files
- Updates in real-time when settings change

## Examples

1. Basic File Renaming:
   - Prefix: "vacation_"
   - Start Number: 1
   - Padding Digits: 2
   - Result: vacation_01.jpg, vacation_02.jpg, etc.

2. Folder Processing:
   - Select a folder of images
   - Filter: ".jpg,.png"
   - Include subfolders: checked
   - Renames all matching files in the folder and subfolders

## Error Handling

The application handles various error cases:
- Invalid input values
- File access permissions
- Existing files with same names
- Invalid characters in filenames


## License

This project is released under the [MIT License]. Feel free to use, modify, and distribute it as needed.

---
