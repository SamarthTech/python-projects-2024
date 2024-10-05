# Enhanced Snake Game AI

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Game Rules](#game-rules)
6. [AI Algorithms](#ai-algorithms)
7. [Customization](#customization)
8. [License](#license)

## Introduction

This project implements an enhanced version of the classic Snake game with an AI player using Python and Pygame. The AI uses a Breadth-First Search (BFS) algorithm to navigate through obstacles and collect power-ups while finding the shortest path to the food. This project serves as an excellent example of pathfinding algorithms, game development, and AI decision-making in Python.

## Features

- Classic Snake game mechanics with additional elements
- AI-controlled snake using BFS or or A* pathfinding
- Obstacles to avoid
- Power-ups for bonus points
- Score tracking
- Path visualization
- Customizable game parameters

## Requirements

- Python 3.6+
- Pygame
- NumPy

## Installation

1. Clone this repository or download the source code.
2. Install the required libraries:

```bash
pip install pygame numpy
```

3. Run the game:

```bash
python main.py
```

## How to Play

Use the arrow keys to navigate the start menu and press Enter to select a game mode:

- Single Player (BFS): AI snake uses Breadth-First Search algorithm
- Single Player (A*): AI snake uses A* pathfinding algorithm
- Multi-snake Mode: Two AI-controlled snakes compete
- Watch as the AI navigates the snake to eat the food, avoid obstacles, and collect power-ups.
- The game ends when the snake collides with the wall, an obstacle, or itself.
- After the game ends, the final state is displayed for 3 seconds before the program closes.

## Game Rules

- The snake grows longer as it eats food (red squares)
- Avoid hitting the walls, obstacles (blue squares), or the snake's own body
- Collect power-ups (yellow squares) for bonus points
- The game speeds up as you progress through levels

## AI Algorithms

The game implements two pathfinding algorithms for the AI:

1. Breadth-First Search (BFS): Explores all neighbor squares evenly to find the shortest path to the food.
2. A* (A-star): Uses a heuristic to guide the search towards the food more efficiently.

The AI considers obstacles, power-ups, and its own body when planning paths.

## Customization

You can modify various game parameters in the `main.py` file:

- `width` and `height`: Change the game window size
- `snake_block`: Adjust the size of the snake and grid squares
- `initial_speed`: Set the starting game speed
- `obstacle_count`: Change the number of obstacles
- `power_up_duration`: Adjust how long power-ups last


Please fork the repository and create a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

---
