# Tic-Tac-Toe with AI

A Python implementation of the classic Tic-Tac-Toe game featuring an AI opponent with multiple personalities. The game provides a graphical user interface built with Tkinter and implements the Minimax algorithm for intelligent AI moves.

## Features

- Graphical user interface with clickable buttons
- AI opponent with multiple personalities:
  - Aggressive: Prioritizes winning moves and blocking opponent wins
  - Cautious: Focuses on blocking opponent wins before making offensive moves
  - Unpredictable: Makes random moves
- Minimax algorithm implementation for optimal AI decisions
- Clear game status updates and win/tie notifications
- Easy-to-use reset functionality

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository or download the `main.py` file
2. Ensure Python 3.x is installed on your system
3. No additional package installation is required as the game uses standard Python libraries

## How to Run

```bash
python main.py
```

## How to Play

1. The game starts with an empty 3x3 grid
2. You play as X and the AI plays as O
3. Click on any empty cell to make your move
4. The AI will automatically make its move after yours
5. The game ends when:
   - One player gets three in a row (horizontally, vertically, or diagonally)
   - The board is full (tie game)
6. A message box will announce the winner or tie
7. The game automatically resets after each round

## Code Structure

- `TicTacToe` class: Main game logic implementation
- Game state management:
  - Board representation
  - Move validation
  - Win condition checking
  - AI move generation
- AI strategies:
  - Minimax algorithm implementation
  - Multiple personality behaviors
  - Random move generation
- GUI implementation:
  - Tkinter button grid
  - Event handling
  - Display updates

## AI Implementation Details

The AI opponent uses different strategies based on its personality:

1. **Aggressive**
   - Attempts to win immediately if possible
   - Blocks opponent's winning moves
   - Falls back to random moves if no immediate threats/opportunities

2. **Cautious**
   - Prioritizes blocking opponent's winning moves
   - Makes random moves when no immediate threats exist

3. **Unpredictable**
   - Makes completely random moves
   - Useful for practice and unpredictable gameplay

The AI also implements the Minimax algorithm for optimal move selection in certain scenarios.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements:
- Additional AI personalities
- UI enhancements
- Performance optimizations
- Bug fixes

## License

This project is open-source and available for personal and educational use.