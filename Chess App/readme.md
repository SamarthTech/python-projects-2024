# Chess Engine Web Application

This project is a Flask-based web application that integrates a chess engine to calculate the best possible move based on the given board state. The chess engine uses the Minimax algorithm with Alpha-Beta pruning and iterative deepening to evaluate the best move for a given depth.

## Features

- **Chess Move Calculation**: Given a position in Forsyth–Edwards Notation (FEN) and a depth, the engine calculates the best move using the Minimax algorithm.
- **Iterative Deepening**: The engine progressively deepens the search to find the best possible move within a specified depth.
- **Alpha-Beta Pruning**: Optimized move calculation using Alpha-Beta pruning for efficient tree search.

## Technologies Used

- **Flask**: Used as the web framework to handle routes and serve the application.
- **Python-Chess**: A Python library used to represent the chess board and calculate legal moves.
- **Minimax Algorithm**: Implemented to calculate the best move.
- **Alpha-Beta Pruning**: An enhancement to the Minimax algorithm to prune unnecessary branches and improve search efficiency.

## Setup and Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chess-engine-webapp.git
   cd chess-engine-webapp
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python flask_app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000/` to see the application.

