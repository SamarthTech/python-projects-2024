# Book Recommendation System

This project is a basic book recommendation system that recommends similar books based on a given book title. It uses TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to find and rank the most similar books.

## Features

- **Data Analysis**: Plot histograms for the distribution of average ratings and bar charts for the most popular authors.
- **Recommendation System**: Provides book recommendations based on cosine similarity between books' content (title and author combined).
- **Interactive Visualization**: Leverages Plotly for interactive data visualization (currently commented out for simplicity).

## Installation

### Prerequisites

You need to have Python installed on your machine. You can download and install Python from the official [Python website](https://www.python.org/).

### Step-by-Step Setup

1. Clone the repository or download the script files.
   
2. Install the required Python packages. You can do this by running the following command in the terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the dataset `books_data.csv` in the same directory as the script. The CSV should have the following columns: 
   - `title` (Book title)
   - `authors` (Book author)
   - `average_rating` (Numerical rating of the book)

## Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. Enter the name of the book when prompted:

   ```bash
   Enter the title of the book: The Late Mattia Pascal
   ```

3. The script will output a list of recommended books based on the provided title.

### Visualizations

There are two interactive visualizations you can enable by uncommenting the respective sections in the code:
- **Histogram of Average Ratings**: Shows the distribution of book ratings.
- **Bar Chart of Top Authors**: Displays the top 10 authors with the most books in the dataset.


### Notes:
1. **Dataset**: Ensure your `books_data.csv` file is in the same directory as the script, and it contains columns like `title`, `authors`, and `average_rating`.
2. **Custom Modifications**: If you want to add your visualizations back, simply uncomment the relevant Plotly code lines.
