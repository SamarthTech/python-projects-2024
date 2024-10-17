
# Bank Management System

## Overview

The Bank Management System is a console-based application that allows users to manage bank accounts. Users can create new accounts, deposit and withdraw money, check account balances, modify account details, and delete accounts. The application uses the `pickle` module to serialize account data, allowing for persistent storage.

## Features

- Create a new account with unique account numbers.
- Deposit and withdraw funds.
- Display account balances.
- List all account holders.
- Modify existing account details.
- Delete an account.
- Persistent storage of account data using Python's `pickle`.

## Technologies Used

- **Python**: The programming language used to implement the application.
- **pickle**: For serializing and deserializing account data to maintain persistent storage.

## Installation

1. **Install the required packages**:

   Create a virtual environment (recommended) and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:

   Execute the script in your terminal:

   ```bash
   python main.py
   ```

2. **Follow the prompts**:

   After starting the application, follow the on-screen prompts to perform various operations.

## Project Structure

```
├── main.py     # Main application file
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```
