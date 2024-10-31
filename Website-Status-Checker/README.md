# Website Status Checker
## Overview

This Python project allows users to check the status of a website by entering its URL. The program validates the URL, sends a request to the server, and returns the HTTP status code of the website. It helps determine whether a website is reachable and what status code it responds with, such as `200 OK` for a successful connection or error codes like `404 Not Found`.

## Features

- **Input URL**: Accepts website URLs from users and validates their format (HTTP/HTTPS).
- **Automatic URL Formatting**: If the user omits the `http://` or `https://` prefix, the program automatically adds `https://` to the URL.
- **HTTP Status Codes**: Retrieves and displays the website’s HTTP status code.
- **Error Handling**: Handles errors when URLs are invalid or the website is unreachable.
- **Retry Option**: Gives the user an option to retry with a different URL after an error.

## Requirements

- Python 3.x
- `urllib` (This is part of Python’s standard library, so no external installations are necessary).

## Installation

No additional installation is needed as `urllib` is part of the Python Standard Library. Just make sure you have Python 3.x installed on your system.

To check your Python version:

```bash
python --version
```

## How to Use

1. Clone the repository or download the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script by typing:

    ```bash
    python main.py
    ```

4. The script will prompt you to enter a website URL. You can type in a URL with or without the `http://` or `https://` prefix.
   
   - Example:
     ```
     Enter the Website URL:  www.example.com
     ```

5. If the URL is valid and the website is reachable, the script will return the HTTP status code of the website:

   ```
   The website https://www.example.com has returned a 200 code
   ```

6. If there’s an error, such as an invalid URL or a server issue, the program will display an error message and give you the option to retry:

   ```
   URL Error: [Errno 11001] getaddrinfo failed
   Make sure you are entering a valid URL
   Do you want to try again (y/n): y
   ```

## Code Explanation

### Function `check_website_status()`

1. **URL Input and Validation**:
   - The program prompts the user to enter a website URL. It checks whether the URL starts with `http://` or `https://`. If not, it automatically appends `https://` to the input.

2. **Request Headers**:
   - It uses the `urllib.request` module to make a GET request to the website. A custom User-Agent header is added to mimic a real browser request.

3. **Handling Responses**:
   - The response code is fetched using `page.getcode()`, and the corresponding HTTP status code is displayed.

4. **Error Handling**:
   - If any exceptions occur (e.g., invalid URL, network issues), the error is caught and printed, and the user is prompted to retry or exit the script.

### Sample Run

```bash
Enter the Website URL:  example.com
The website https://example.com has returned a 200 code
```

If there is an error:

```bash
URL Error: [Errno 11001] getaddrinfo failed
Make sure you are entering a valid URL
Do you want to try again (y/n): y
```

---
