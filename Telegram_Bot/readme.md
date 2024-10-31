# Telegram Bot

This is a simple Telegram bot built using Python and the `python-telegram-bot` library. The bot responds to certain commands and messages to provide links to popular websites like YouTube, LinkedIn, Gmail, and GeeksforGeeks.

## Features

- `/start`: Greets the user and provides a welcome message.
- `/help`: Lists all available commands.
- `/youtube`: Sends the YouTube URL.
- `/linkedin`: Sends the LinkedIn URL.
- `/gmail`: Sends a placeholder message for the Gmail URL (customize it with your own link).
- `/geeks`: Sends the GeeksforGeeks URL.
- Handles unknown commands and text input by replying with a message.

## Requirements

- Python 3.7+
- `python-telegram-bot` library (v20 or higher)

## Installation

1. Clone the repository or download the script.
2. Install dependencies:
    ```bash
    pip install python-telegram-bot
    ```
3. Replace `"your_own_API_Token"` in the code with the token you obtained from the [BotFather](https://t.me/BotFather) on Telegram.
4. Run the bot:
    ```bash
    main.py
    ```

## Usage

Once the bot is running, you can interact with it by sending commands in the Telegram chat. Here are the available commands:

- `/start` - Starts the bot and welcomes the user.
- `/help` - Lists available commands.
- `/youtube` - Provides the YouTube URL.
- `/linkedin` - Provides the LinkedIn URL.
- `/gmail` - Provides a Gmail placeholder message.
- `/geeks` - Provides the GeeksforGeeks URL.

### Error Handling

The bot will handle unknown commands and messages that don't match any registered handler by sending a message back to the user, notifying them that the input was not recognized.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
