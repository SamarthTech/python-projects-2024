# 📕 Contact Book CLI App

A sleek and powerful command-line interface (CLI) application for managing your contacts with style!

## 🌟 Features

- **Add Contacts**: Quickly add new contacts with names and phone numbers
- **View Contacts**: Display all your contacts in a beautifully formatted table
- **Edit Contacts**: Update contact information with ease
- **Remove Contacts**: Delete contacts you no longer need
- **Rich CLI**: Enjoy a colorful and interactive command-line experience

## 🛠 Installation

1. Clone this repository:
   ```
   git clone https://github.com/KoustavDeveloper/contact-book-cli-app.git
   cd contact-book-cli-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the application using the following command:

```
python main.py [COMMAND] [ARGUMENTS]
```

### Available Commands:

- **Add a contact**:
  ```
  python main.py add "John Doe" "1234567890"
  ```

- **Show all contacts**:
  ```
  python main.py show
  ```

- **Edit a contact**:
  ```
  python main.py edit 1 --name "Jane Doe" --contact-number "9876543210"
  ```

- **Remove a contact**:
  ```
  python main.py remove 1
  ```

## 🧰 Tech Stack

- **Python**: The core programming language
- **Typer**: For creating the CLI interface
- **Rich**: For beautiful terminal formatting
- **TinyDB**: A lightweight document-oriented database

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/KoustavDeveloper/contact-book-cli-app/issues).

## 💖 Show your support

Give a ⭐️ if you like this project!

---

Made with 💻 and ❤️ by [Koustav Singh](https://github.com/KoustavDeveloper/)