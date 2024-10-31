

---

# Currency Converter

## Overview

The Currency Converter is a simple Python application that allows users to convert amounts between different currencies. The application has a user-friendly graphical interface built using the `tkinter` library and fetches real-time exchange rates using the `requests` library.

## Features

- Convert currency amounts between multiple currencies.
- Real-time exchange rate fetching from an online API.
- User-friendly graphical interface.
- Easy to use with clear input and output sections.

## Requirements

To run this application, you'll need:

- Python 3.x installed on your machine.
- The following Python packages:
  - `requests`
  - `tkinter` (usually comes pre-installed with Python)

You can install the required packages using pip:

```bash
pip install requests
```

## How to Run

1. Clone this repository or download the code file.

2. Navigate to the directory where the file is saved.

3. Run the application with the following command:

   ```bash
   python currency_converter.py
   ```

4. The application window will open. Enter the amount you wish to convert, select the currencies you want to convert from and to, and click the "Convert" button to see the converted amount.

## Usage

1. **Amount**: Enter the amount you want to convert in the "Amount" field.
2. **From Currency**: Select the currency you want to convert from using the dropdown menu.
3. **To Currency**: Select the currency you want to convert to using the dropdown menu.
4. **Convert**: Click the "Convert" button to display the converted amount below.

## Example

- If you want to convert 100 USD to EUR, enter `100` in the "Amount" field, select `USD` from the "From Currency" dropdown, select `EUR` from the "To Currency" dropdown, and click "Convert." The converted amount will be displayed.

## API Information

The application fetches exchange rates from the following API:

- **API Endpoint**: [ExchangeRate API](https://api.exchangerate-api.com)