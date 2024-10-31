
# AI TicTacToe

This is a simple implementation of a **TicTacToe** game in Python, where a human player competes against an AI that uses the **Minimax algorithm**. The game is played on a 3x3 grid, and the AI ensures optimal play, making it impossible for the human to win if the AI plays perfectly.

## Features
- **Human vs AI gameplay**: The human player plays against an AI opponent.
- **AI with Minimax algorithm**: The AI player is programmed to play optimally using the Minimax algorithm.
- **Simple and intuitive command-line interface**: Easy-to-follow prompts for human players.
- **Draw detection**: The game recognizes when all spaces are filled and the match ends in a tie.
- **Win detection**: The game announces when either player wins.

## Game Rules
- Players take turns placing their marks (X for the human, O for the AI) on the grid.
- The goal is to place three of your marks in a row, column, or diagonal.
- The first player to align three marks wins the game.
- If the grid is full and no player has aligned three marks, the game ends in a tie.

## How the AI Works
The AI uses the **Minimax algorithm**, a recursive algorithm used for decision-making in turn-based games like TicTacToe. The AI will:
- Try to maximize its own score by selecting the best possible move.
- Minimize the human player's score, ensuring the best defense.
- The AI will never lose if it plays optimally, though it may tie if the human plays perfectly.

## Project Structure

```
ai_tictactoe/
│
├── main.py         # Main Python script containing game logic
└── README.md              # Project documentation
```

## How to Play

1. After running the script, the game will display the 3x3 grid.
2. You will be prompted to enter the row and column number (0 to 2) for your move.
3. The AI will make its move after yours.
4. The game will continue until either player wins or the grid is full (tie).
5. The game will print the result once it is over.

### Example Gameplay
```
  |   |
-----
  |   |
-----
  |   |

Your turn!
Enter row (0-2): 1
Enter column (0-2): 1

  |   |
-----
  | X |
-----
  |   |

AI's turn...

  |   |
-----
  | X |
-----
  | O |

```

## Customization

### Change the Board Size
The current implementation uses a 3x3 grid, which is standard for TicTacToe. If you want to experiment with different board sizes, you can modify the `board` initialization in the code:
```python
board = [[EMPTY for _ in range(3)] for _ in range(3)]
```
You can change the `3` to any other number to try out different grid sizes, though you will need to adjust the win condition logic accordingly.

## How Minimax Works

The Minimax algorithm works by simulating all possible moves from the current position. It evaluates:
- If a move will lead to a win for the AI.
- If a move will lead to a loss (so it avoids it).
- If no immediate win or loss is detected, it tries to secure a draw.

The AI looks several moves ahead to ensure it always makes the best possible decision.

## Future Improvements
- **GUI support**: Implement a graphical interface using a library like Pygame or Tkinter.
- **Difficulty levels**: Add options for different AI difficulty levels by modifying the depth of the Minimax search.
- **Multiplayer mode**: Allow two human players to play against each other.

---
