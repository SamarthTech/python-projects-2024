# ZoomZoom: Automated Zoom Meeting Joiner
## Overview

**ZoomZoom** is a Python-based tool designed to automate the process of joining Zoom meetings. It allows users to save their meeting URLs and passwords for future use, then automatically fills in the Zoom meeting credentials using `Selenium` and `PyAutoGUI` to simulate browser actions and desktop inputs. This is particularly useful for frequent Zoom users who want to streamline the process of joining meetings without manual input each time.

## Features

- **Automatic Meeting Joining**: Automatically enters Zoom meeting details and joins meetings without manual intervention.
- **Saved Meetings**: Save frequently-used meeting URLs and passwords for easy access in future sessions.
- **Platform Compatibility**: Works on Linux, Mac, and Windows platforms. The process for joining Zoom differs slightly across operating systems, and the script accounts for these differences.
- **Automated Browser Actions**: Uses `Selenium` to open the Zoom website and `PyAutoGUI` to interact with your desktop.
- **Command Line Interface**: Simple and interactive terminal interface for selecting or adding meeting details.

## Requirements

### Python Libraries

Before running the script, ensure you have the following libraries installed:

- `json` (built-in)
- `pyautogui`
- `re` (built-in)
- `pyfiglet`
- `getpass` (built-in)
- `platform` (built-in)
- `selenium`
- `clint`
- `time` (built-in)
- `os` (built-in)

You can install the required libraries with pip:

```bash
pip install pyautogui pyfiglet selenium clint
```

### WebDriver

You must also download the appropriate WebDriver for your browser. The WebDriver should be placed in the `webdriver/` directory within your project folder.

- **Chrome**: [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
- **Firefox**: [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

### Zoom

Ensure you have the Zoom application installed on your desktop as this tool will open and interact with it.

## Usage

### 1. Start the Application

To run the application, simply execute the Python script:

```bash
python zoom_zoom.py
```

### 2. Interactive Meeting Management

- Upon starting the application, you will be greeted by a welcome screen and a list of your saved meetings.
- You can either select a saved meeting by typing its corresponding number or enter a new Zoom meeting URL.
  
### 3. Joining a Meeting

The script will use the Zoom URL or meeting ID provided, fill in the required fields, and handle window actions like clicking "Join without video."

### 4. Saving a Meeting

If you choose to enter a new Zoom meeting URL, you will be prompted to save the meeting for future use. You can assign a name to this meeting, and the details will be stored in a `meetings.json` file for easy access in future sessions.

### 5. Entering a Password

- If the meeting requires a password, the script will prompt you for it.
- The password will be entered into Zoom automatically when the application opens.

### 6. Exiting the Application

To exit the application at any time, use `CTRL + C`.

## Configuration

### JSON File (`data/meetings.json`)

This file stores your saved meetings in the following format:

```json
{
  "meetings": {
    "Team Standup": {
      "id": "1234567890",
      "psw": "password123"
    }
  }
}
```

This allows for quick retrieval of meeting information during subsequent runs.

### Adjusting Window Size

The script automatically detects your screen size to properly interact with Zoom's UI. If necessary, you can adjust this by modifying the window size arguments passed to `chrome_options` in the script.

## Important Notes

- **Disabling Tiling Window Managers**: If you are using a tiling window manager on Linux or Mac, disable it before running the script, as it may interfere with window detection and interaction.
  
- **WebDriver Compatibility**: Make sure you download the appropriate WebDriver that corresponds to the version of the browser you have installed.

## Known Issues and Limitations

- The script is designed to work with Chrome, but it can be adapted for Firefox or other browsers by changing the WebDriver.
- The use of `pyautogui` requires exact screen resolution settings for mouse clicks. This means the script may need adjustments if Zoom’s UI elements are resized.
- The tool doesn't handle advanced Zoom settings such as pre-joining audio or video permissions. 

## Future Enhancements

Some planned improvements for the script include:

- Adding support for automatic video/audio configuration during joining.
- Introducing multi-browser support.
- Enhancing error handling to account for meeting failures or incorrect URLs.

---
