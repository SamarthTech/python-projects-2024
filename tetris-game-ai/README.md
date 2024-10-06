# AI Tetris

This project implements an AI-powered Tetris game using Python and Pygame. The AI agent uses a weighted scoring system to make decisions about piece placement.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [To Be Done](#to-be-done)

## Features

- Classic Tetris gameplay
- AI agent that plays the game automatically
- Visualization of the AI's decision-making process

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ritaban06/tetris-game-ai.git
   cd tetris-game-ai
   ```

2. Install the required dependencies:
   ```
   pip install pygame
   ```

## Usage

Run the main script to start the AI Tetris game:

```
python main.py
```

Watch as the AI agent plays Tetris automatically!

## Project Structure

- `main.py`: The entry point of the application. It sets up the game window and runs the main game loop.
- `game.py`: Contains the `Game` class, which implements the Tetris game logic and rendering.
- `ai.py`: Implements the `AI` class, which makes decisions about piece placement.

## How It Works

The AI agent uses a weighted scoring system to evaluate potential moves. It considers factors such as:

- Height of the piece placement
- Number of lines cleared
- Number of holes created
- Bumpiness of the resulting surface

For each possible move (rotation and horizontal position), the AI simulates the outcome and calculates a score. It then chooses the move with the highest score.

## To Be Done

- [ ] Implement a scoring system for the player
- [ ] Add a user interface for starting/stopping the AI
- [ ] Implement different difficulty levels for the AI
- [ ] Add sound effects and background music
- [ ] Create a menu system for game options
- [ ] Optimize the AI's performance for faster decision-making
- [ ] Add support for different Tetris piece sets
- [ ] Implement a genetic algorithm to evolve better AI weights
