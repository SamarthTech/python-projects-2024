# RSS News Fetcher
## Overview
The **RSS News Fetcher** is a Python project that fetches and parses news stories from a given RSS feed using HTTP requests. It demonstrates how to handle RSS feeds using Python libraries such as `requests` for fetching data and `xml.etree.ElementTree` for parsing XML content.

This project provides a utility to load an RSS feed from a URL, parse the XML content, and extract key elements like the news title, description, and media URLs. It is designed with a focus on modularity, making it easy to extend or modify for other RSS feeds.

## Table of Contents
1. [Features](#features)
2. [Dependencies](#dependencies)
3. [Usage](#usage)
4. [Code Walkthrough](#code-walkthrough)
5. [Customization](#customization)
6. [Future Improvements](#future-improvements)

---

## Features
- **Fetch RSS Feed**: Load RSS feeds from a specified URL using HTTP requests with custom headers.
- **XML Parsing**: Parse the fetched XML to extract structured news information.
- **Support for Media Content**: Handle RSS feeds with embedded media content, such as images.
- **Modular Design**: Each part of the functionality (fetching, parsing, and displaying data) is handled by separate functions for easier maintenance.

---

## Dependencies
To run this project, you'll need the following Python libraries:
- `requests`: Used to send HTTP requests to fetch the RSS feed.
- `xml.etree.ElementTree`: A built-in Python library to parse XML data.

You can install the necessary libraries via pip:
```bash
pip install requests
```

> `xml.etree.ElementTree` comes with Python, so no separate installation is required.

---

## Usage
1. Open a terminal and navigate to the project directory.
   
2. Run the `topStories` function to fetch and display top news stories:
   ```bash
   python main.py
   ```

3. The script will print the following details:
   - Raw RSS feed content (first 500 characters) to ensure valid response.
   - Parsed news items from the feed, showing the title, description, link, publication date, and media (if available).

---

## Code Walkthrough

### 1. `loadRSS()`
This function is responsible for:
- Sending a GET request to the RSS feed URL with custom headers (User-Agent) to avoid potential access restrictions.
- Returning the response content, which contains the RSS feed in XML format.

Example:
```python
resp = requests.get(RSS_FEED_URL, headers=headers)
```

### 2. `parseXML(rss)`
This function:
- Parses the XML content using Python’s `xml.etree.ElementTree`.
- Iterates over each `<item>` in the RSS feed to extract the title, description, link, media, etc.
- Appends each news item into a list and returns it.

It specifically checks for media content in the RSS feed using the `{http://search.yahoo.com/mrss/}content` namespace.

Example:
```python
for child in item:
    if child.tag == '{http://search.yahoo.com/mrss/}content':
        news['media'] = child.attrib['url']
```

### 3. `topStories()`
This function is the main entry point of the script. It:
- Loads the RSS feed using `loadRSS()`.
- Parses the XML data using `parseXML()`.
- Displays the first 5 top stories in the console for debugging.

---

## Customization

### 1. Change RSS Feed URL
To fetch news from a different source, update the `RSS_FEED_URL` variable in the script:
```python
RSS_FEED_URL = "https://example.com/rss-feed-url"
```

### 2. Modify News Item Structure
If your RSS feed contains different tags or data points, adjust the logic inside `parseXML()` to extract the appropriate fields. For example, if the feed includes author details, you can extract them as follows:
```python
news['author'] = item.find('author').text
```

---

## Future Improvements

1. **Error Handling**: Add more robust error handling to manage network failures, timeouts, and invalid RSS feeds.
2. **Data Storage**: Store the fetched news items in a file or database for offline access or historical tracking.
3. **Web Scraping**: If the RSS feed doesn’t provide enough detail, integrate a web scraping mechanism to fetch full articles.
4. **User Interface**: Build a simple GUI or web interface to display the news stories in a more user-friendly way.
5. **RSS Feed Customization**: Allow users to input their preferred RSS feed URL at runtime.

---
