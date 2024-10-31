

# Tic-Tac-Toe Game

Welcome to the **Tic-Tac-Toe** game! This Python-based game allows you to play a classic game of Tic-Tac-Toe against the computer.

## Table of Contents

- [Introduction](#introduction)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [How to Run](#how-to-run)
- [Features](#features)


## Introduction

This is a simple implementation of the Tic-Tac-Toe game in Python. The player can play against the computer in a 3x3 grid. The player uses 'X' and the computer uses 'O'. The game ends when either player wins or the game is a draw.

## How to Play

1. The game is played on a 3x3 grid.
2. You (the player) will use 'X', and the computer will use 'O'.
3. Players take turns placing their marks (X or O) in empty cells.
4. The player must input a number from 1 to 9 to choose a spot on the grid.
5. The computer chooses a random spot from the available cells.
6. The first player to align three of their marks vertically, horizontally, or diagonally wins the game.
7. If all cells are filled without any player winning, the game ends in a draw.

## Game Rules

- The player always plays as 'X', and the computer as 'O'.
- The grid positions are represented by numbers from 1 to 9:
  
  ```
   1 | 2 | 3
  -----------
   4 | 5 | 6
  -----------
   7 | 8 | 9
  ```

- To place your mark, input the number corresponding to the grid position.
- The game checks for a winner after every move.
- If there’s a winner, the game displays the winner and ends.
- If the grid is full without a winner, it ends in a draw.


## How to Run

To run the game, use the following command:

```bash
python main.py
```

## Features

- **Player vs. Computer**: Play against the computer.
- **Random Moves**: The computer chooses its moves randomly.
- **Win Detection**: Automatically detects a win or draw condition.
- **Simple CLI**: Easy to use, text-based interface.



