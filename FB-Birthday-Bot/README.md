# Facebook Birthday Wisher
## Project Overview

This project automates the process of wishing your Facebook friends a happy birthday. The script, written in Python and utilizing Selenium, logs into a Facebook account, navigates to the birthdays section, and sends a predefined birthday wish to all friends celebrating their birthdays on that day.

## Features

- **Automated Login:** Logs into your Facebook account using credentials provided by the user.
- **Birthday Detection:** Retrieves the list of friends who have birthdays on the current day.
- **Automated Wishes:** Sends a custom birthday message to each friend with a birthday, up to the number specified by Facebook.

## Technologies Used

- **Python**: The core programming language used.
- **Selenium WebDriver**: A powerful tool for controlling a web browser through programs and performing automated tasks.
- **ChromeDriver**: Used as the interface for controlling Chrome browser during automation.

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.x**: You can download it from [here](https://www.python.org/downloads/).
2. **Selenium**: Install it using the command:

    ```bash
    pip install selenium
    ```

3. **Chrome Browser**: Make sure you have the Chrome browser installed on your machine.
4. **ChromeDriver**: Download the ChromeDriver that matches your browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/). Extract the `chromedriver.exe` and update the `cd` path in the script accordingly.

## Important Notes

- **Facebook Login Restrictions**: Facebook may block the automated login if it detects unusual activity from your account. Use this script responsibly.
- **Captcha Handling**: The current version does not handle Facebook CAPTCHA challenges, which may arise during automated logins.
- **Rate Limiting**: The script limits the number of wishes sent to avoid sending belated birthday wishes and reduce the risk of being flagged for suspicious activity.

