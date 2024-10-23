# Dice Roller

A simple Python program that simulates rolling dice. The program allows the user to specify how many dice to roll and displays the result of each roll. The user can continue rolling or exit the program at any time.

## Features

- Roll a specified number of six-sided dice.
- Input validation to handle non-integer inputs.
- Option to exit the program by typing "exit".
- Generates random dice rolls using Python's `random` module.

## Getting Started

### Prerequisites

To run this program, you need to have Python installed on your system. Python 3.6 or later is recommended.


## How to Use

1. When the program starts, it will prompt you to enter the number of dice you would like to roll.
2. Enter a positive integer to roll that number of dice. For example, entering `3` will roll three dice.
3. The program will output the results of each roll, separated by commas.
4. You can type "exit" at any prompt to close the program.

### Example

```
How many dice would you like to roll? 3
4, 1, 6

How many dice would you like to roll? 2
5, 2

How many dice would you like to roll? exit
Thanks for playing!
```

## Code Overview

### `roll_dice(amount: int = 2) -> list[int]`
A function that rolls a specified number of dice and returns the results as a list.

- **Parameters:**
  - `amount` (int): The number of dice to roll (default is 2).
- **Returns:**
  - A list of integers representing the dice rolls.

### `main()`
The main loop that runs the program. It continually prompts the user for input and displays the dice roll results, handling errors for non-integer inputs.

### Error Handling
- If the user inputs a non-integer value, the program displays `(Please enter a valid number)` and prompts the user to try again.
- If the number of dice specified is zero or less, a `ValueError` is raised.

---
