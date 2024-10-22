# Habit Tracker

This Habit Tracker project is a Python-based tool designed to help users break habits and monitor their progress over time. The tool tracks how much time and money have been saved by quitting a habit and provides an estimate of how many days are left to reach a specific goal. The program calculates these metrics based on user-defined details about the habit.

## Features

- **Track Habit Progress**: Measures the amount of time since a habit was broken and calculates the days remaining to reach a goal.
- **Calculate Savings**:
  - Estimates the money saved based on the cost per day associated with the habit.
  - Determines the amount of time saved by avoiding the habit.
- **Tabulated Data Output**: Displays habit details in a structured table format.

## Project Structure

The project consists of the following files:

1. **`habit_tool.py`**:
   - Contains the main function, `break_habit`, which calculates metrics related to breaking a habit.
   - The function takes the following parameters:
     - `habit_name`: Name of the habit being tracked.
     - `start_date`: The date when the habit was broken.
     - `cost_per_day`: The daily cost associated with maintaining the habit.
     - `minutes_wasted`: The estimated minutes wasted on the habit each day.
   - The function returns a dictionary with details such as the habit name, time elapsed since breaking the habit, days remaining to reach the goal, minutes saved, and money saved.

2. **`main.py`**:
   - Uses the `break_habit` function to track multiple habits and displays the results in a tabulated format.
   - Habits tracked in this example include "Coffee," "Social Media," and "Soft Drinks."
   - Uses the `pandas` library to create a DataFrame for structured data representation.
   - Uses the `tabulate` library for formatted table output.

## Usage

1. **Modify Habits**:
   - Update the `main.py` file to add or remove habits as needed. Each habit should be defined with the `break_habit` function, specifying the habit name, start date, cost per day, and minutes wasted.

2. **Run the Program**:
   ```bash
   python main.py
   ```

3. **Output**:
   - The program will output a table displaying the habit details, including:
     - Habit name
     - Time since the habit was broken (in hours or days)
     - Days remaining to reach the goal
     - Minutes saved by avoiding the habit
     - Money saved by not maintaining the habit

## Example

Here is an example of how to use the program:

```python
# In main.py
habits = [
    break_habit('Coffee', datetime(2024, 10, 22, 18, 20), cost_per_day=2, minutes_wasted=15),
    break_habit('Social Media', datetime(2024, 10, 22, 18, 20), cost_per_day=3, minutes_wasted=15),
    break_habit('Soft Drinks', datetime(2024, 10, 22, 18, 20), cost_per_day=4, minutes_wasted=15),
]
```

Running `main.py` would produce a table similar to the following:

```
+----+-----------+---------------+----------------+----------------+----------------+-------------+
|    | habit     | time_since    | days_remaining | minutes_saved  | minutes_wasted | money_saved |
+----+-----------+---------------+----------------+----------------+----------------+-------------+
|  0 | Coffee    | 3 days        | 57             | 45             | 15             | $6.00       |
|  1 | Social Media | 3 days     | 57             | 45             | 15             | $9.00       |
|  2 | Soft Drinks | 3 days      | 57             | 45             | 15             | $12.00      |
+----+-----------+---------------+----------------+----------------+----------------+-------------+
```

## Customization

- **Goal Settings**: The `goal` value in `habit_tool.py` can be modified to change the target number of days for breaking the habit.
- **Hourly Wage**: Adjust the `hourly_wage` variable to reflect the user's income, which affects the calculation of money saved based on time.

---
