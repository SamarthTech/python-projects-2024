
## 🧠 AI-Powered Code Review Bot 🤖

Welcome to the AI-Powered Code Review Bot project! This Python-based tool is designed to automatically analyze Python code and provide valuable feedback using the popular pylint library. Whether you’re a seasoned developer or just starting out, this bot helps you improve your code quality by detecting potential issues such as bad practices, inefficiencies, and style violations.

## 🚀 Contributing to Hacktoberfest 2024
This project is part of Hacktoberfest 2024, and I’m excited to contribute! If you're interested in improving this AI-powered code review bot, feel free to fork the repository, submit a pull request (PR), and get involved.
## 🔍 Features

- Automated Code Review: Scans Python scripts and provides feedback on issues like unused imports, bad naming conventions, missing docstrings, and more.
- Efficiency Suggestions: Highlights inefficient algorithms and recommends code optimization.
- Modular and Extensible: The bot can easily be extended to add more rules or integrate with other code analysis tools.
- Hacktoberfest Friendly: Contributors are welcome to improve the bot, add new features, or suggest optimizations


## 🛠️ Tech Stack

- **Python:** The core language.
- **Pylint:** Used for code analysis and review.
- **Subprocess:** For running external commands like pylint from within the script.


## ⚙️ Installation and Setup

Follow these steps to get the bot running locally:

1. Clone the Repository:
```bash
git clone https://github.com/5haiqin/AI-Powered_code_review_Bot.git

```

2. Create and Activate Virtual Environment:
```bash
python -m venv AI-Powered_code_review_Bot/venv
# Windows
AI-Powered_code_review_Bot\venv\Scripts\activate
# Mac/Linux
source AI-Powered_code_review_Bot/venv/bin/activate
```

3. Install Dependencies:
```bash
pip install pylint
```
4. Run this cmd if you get any error related to pip  
```bash
python.exe -m pip install --upgrade pip
# Again install pylint
pip install pylint
```

5. Open the AI-Powered_code_review_Bot Folder:
```bash
cd AI-Powered_code_review_Bot
```

5. Run the Bot:
```bash
python code_review_bot.py
```


## ⚙️ How It Works

1. Provide a Python File: Enter the file path of the Python script you want to review.

2. Analyze the Code: The bot will run pylint and output detailed feedback about the code.

3. Improve Your Code: Use the feedback to fix issues, optimize your code, and ensure it follows best practices.

## 📋 Example Usage


**Sample Python Code (with issues):**
```bash
myFunction():
    print("Hello World")

```
**Run the bot and input the file path of the above script:**
```javascript
Enter the path to the Python file you want to review: test_file.py
```
**Example Output:**
```bash
************* Module test_file
test_file.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test_file.py:1:0: C0116: Missing function docstring (missing-function-docstring)
test_file.py:1:4: C0103: Function name "my_function" doesn't conform to snake_case naming style (invalid-name)

```

## 🤝 How to Contribute

1. **Fork the Repository:** Fork the project from GitHub and create a new branch for your contribution.
2. **Make Changes:** Add new features, improve existing functionality, or enhance the documentation.
3. **Submit a PR:** Once you're happy with your changes, submit a pull request for review

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

# **Let’s make Python code better together! Happy coding! 🎉** 