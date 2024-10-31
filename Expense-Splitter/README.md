# Expense Splitter
## Project Description

This Python project is a simple expense-splitting tool that calculates how much each person should pay when the total amount of an expense is divided among multiple people. It takes user input for the total expense amount, the number of people sharing the expense, and the currency in which the amount is denominated. The program ensures that the number of people is greater than one, and it outputs the share for each individual in the specified currency.

## Features

- User-friendly input prompts for total amount, number of people, and currency.
- Error handling for invalid inputs such as negative values or an insufficient number of people.
- Neatly formatted output, displaying the amount each person should pay.
- Support for any currency via user input (displayed in uppercase).
  
## How to Use

1. **Run the Program:**
   - Run the program in a Python environment (Python 3.6+ recommended).

2. **Provide Inputs:**
   - Enter the total amount to be split.
   - Enter the number of people who will be splitting the amount.
   - Enter the currency symbol or abbreviation for the currency (e.g., `USD`, `EUR`).

3. **View the Output:**
   - The program will display:
     - The total amount.
     - The number of people sharing the cost.
     - The amount each person has to pay, formatted in the chosen currency.

### Example:
```
Enter total amount to be split: 150.00
Enter number of people to be split: 5
Enter currency to split the amount: usd
```
Output:
```
total expenses: USD150.0
number of people: 5
Share per person: USD30.00
```

## Project Files

- **`main.py`**: The main Python script that handles the expense splitting logic.
  
### `main.py` Structure:

1. **`calculate_split`** function:
   - Inputs:
     - `total_amount`: The total expense to be split (float).
     - `number_of_people`: Number of people to divide the expense among (integer).
     - `currency`: The currency symbol (string).
   - Output:
     - Prints the total expense, number of people, and the share per person formatted in the specified currency.
   - Error Handling:
     - Raises a `ValueError` if the number of people is less than or equal to 1.

2. **`main`** function:
   - Gathers inputs from the user.
   - Calls the `calculate_split` function.
   - Handles invalid input by catching `ValueError` exceptions.

## Installation and Setup

### Prerequisites:

- Python 3.6 or later

### Steps:

1. Clone the repository or download the `main.py` file.
2. Open the terminal and navigate to the project directory.
3. Run the Python file using the following command:

   ```
   python main.py
   ```

## Error Handling

- If the user enters a number of people that is less than or equal to 1, the program raises a `ValueError` with the message: *"Number of people must be greater than 1."*
- Invalid inputs like non-numeric values for total amount or number of people will also raise a `ValueError`.


## Future Improvements

- Add support for input validation to prevent negative values.
- Expand the tool to handle scenarios such as:
  - Tip calculation.
  - Splitting based on unequal shares.
  - Saving the results to a file or database for future reference.

---
