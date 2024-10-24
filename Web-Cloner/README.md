# Web Cloner

Web Cloner is a Python-based tool for downloading and cloning websites. It retrieves the content of a specified website and saves it locally, preserving the website's structure. This can be useful for offline browsing, archiving, or content analysis.

## Features

- Downloads web pages from a given URL.
- Saves content locally with the website's structure maintained.
- Uses `requests` for HTTP requests and `BeautifulSoup` for parsing HTML content.
- Filters and saves only valid URLs within the same domain to avoid unnecessary external requests.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using:
```bash
pip install requests beautifulsoup4
```


## Code Overview

The script consists of the following main components:

- **Initialization**: Sets up the main parameters like the base URL and domain name.
- **URL Handling**: Functions to handle URL validation and joining.
- **Content Downloading**: Fetches and saves the content of the specified pages.

## Example

To clone a website, run:
```bash
python webcloner.py https://example.com
```
The content will be saved in a directory named after the website's domain.

## Limitations

- The tool does not handle complex JavaScript-based content.
- Only downloads static content like HTML, images, and stylesheets.
- May not work with websites that block automated requests.

---
