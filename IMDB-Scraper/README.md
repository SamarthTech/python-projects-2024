# IMDB Scraper

## Overview
This project is a Python-based web scraper that extracts movie details from the **IMDb** website using `requests` and `BeautifulSoup`. The user can enter a movie title as a command-line argument, and the scraper will search for that movie, extract key information, and display it.

## Features
- Search for movies by title on IMDb.
- Extract and display movie details such as:
  - Title
  - Year of release
  - IMDb rating
  - Genre
  - Plot summary
  - Release date
  - Country
  - Language
  - Budget
  - Gross revenue (worldwide, USA, opening weekend)
  
The script fetches details for the top 5 search results matching the movie title.

## Prerequisites
To use this project, you need to have Python 3 installed along with the following dependencies:

- `requests`: Used to send HTTP requests to IMDb and retrieve HTML content.
- `BeautifulSoup`: Part of the `bs4` library, used to parse and extract data from the IMDb HTML.
- `argparse`: A Python library used to handle command-line arguments.

Install the required libraries using the following command:
```bash
pip install requests beautifulsoup4 lxml
```

## Usage

### Command-line Arguments
- `--t`: The title of the movie (required). This is the only required argument for the script.

### Example:
```bash
python main.py --t "Inception"
```
This will search IMDb for movies with the title "Inception" and return details about the top 5 matches.

### Output
For each movie match, the script will display the following details (if available):
- **Title**: The name of the movie.
- **Year**: Year of release.
- **IMDb Rating**: Rating based on IMDb user reviews.
- **Genre**: Genre(s) of the movie.
- **Plot**: A brief summary of the movie plot.
- **Release Date**: The official release date of the movie.
- **Country**: Country where the movie was produced.
- **Language**: Language(s) spoken in the movie.
- **Budget**: Estimated production budget.
- **Cumulative Worldwide Gross**: Total gross revenue worldwide.
- **Gross USA**: Total revenue in the USA.
- **Opening Weekend USA**: Revenue generated in the USA during the opening weekend.


## Code Structure

### 1. **argparse setup**
- The `argparse` library is used to handle command-line input. The argument `--t` is mandatory and represents the movie title to search for.

### 2. **Base URLs**
- **`base_id`**: This is the URL format for accessing IMDb movie details when the IMDb ID is known.
- **`base`**: This is the URL format for searching IMDb by a movie title.

### 3. **Main Functions**
#### `get_info(soup)`
- Extracts information from a movie's IMDb page using the parsed HTML (`soup`). This includes the movie's title, year, rating, genre, plot, release date, budget, and gross revenues.

#### `find_movie(query)`
- Builds the IMDb search URL using the base search URL and the query (movie title).
- Fetches the search results from IMDb, parses the top 5 results, and retrieves the IMDb ID for each movie.
- For each movie, fetches the corresponding movie details page and passes the content to `get_info` for detailed scraping.

### 4. **Error Handling**
- Basic error handling is implemented to ensure that if no movie details are found, the user receives a message informing them of the lack of results.
- The `get_info` function checks for missing data and skips elements if not found.

## Notes
- The scraper is designed to work with the current structure of IMDb’s website. However, IMDb’s page structure may change over time, potentially breaking the scraper. To fix any issues, the HTML tags and attributes in the `get_info` function may need updating.
