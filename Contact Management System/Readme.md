

# Contact Management System

This is a Python-based GUI application built using Tkinter for managing contacts. It allows users to add, update, view, and delete contact information, which is stored in a local SQLite database.

## Features

- **Add New Contacts**: Users can add new contacts with fields such as first name, last name, gender, age, address, and contact number.
- **Update Contacts**: Existing contacts can be updated by selecting them from the list.
- **Delete Contacts**: Users can delete a selected contact.
- **View Contacts**: All contacts are displayed in a table with options to sort and select for further actions.

## Technologies Used

- **Python**: The programming language used for the application.
- **Tkinter**: A standard Python library used for creating the GUI.
- **SQLite**: A lightweight, file-based database to store and manage contacts.

## Prerequisites

- Python 3.x
- Tkinter (typically included with Python installations)
- SQLite (included in Python's `sqlite3` library)



3. Ensure you have the required Python libraries installed. If Tkinter is not installed, you can install it using:

   ```bash
   sudo apt-get install python3-tk # For Linux
   ```

   Tkinter is included with standard Python installations on Windows and macOS.

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Upon launching the app, the main window will display a table showing all stored contacts.
2. Use the **+ ADD NEW** button to open a new window to add a new contact.
3. Select any existing contact from the table and double-click to update its details.
4. The **DELETE** button allows you to remove a selected contact.
5. All data is automatically saved in the `contact.db` SQLite database file in the same directory.

## File Structure

- `main.py`: The main Python script containing the Tkinter GUI and SQLite database interaction logic.
- `contact.db`: SQLite database file that stores contact information (automatically created).



