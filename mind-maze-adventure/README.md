# 🌀 Mind Maze Adventure

A dynamic terminal-based maze game where the walls have a mind of their own! Race against time to reach the goal while navigating through a constantly shifting labyrinth.

## 🎮 Game Features

- **Dynamic Maze Environment**: The walls periodically shift and change, creating an ever-evolving challenge
- **Time-Based Challenge**: Complete the maze within 60 seconds
- **Hint System**: Use up to 3 hints to reveal potential paths to the goal
- **Score System**: Earn points based on your remaining time
- **Terminal Graphics**: Clean, simple ASCII-based interface

## 🎯 How to Play

### Controls
- **↑ ↓ ← →** Arrow keys to move your character
- **H** Use a hint (maximum 3 hints per game)

### Game Elements
- **@** Your character
- **#** Walls
- **X** Goal
- **Space** Open path

### Objective
Navigate through the maze to reach the 'X' goal before time runs out. Watch out for shifting walls that can change your path every 5 seconds!

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Curses library (included in standard library for Unix/Linux/macOS)
  - Windows users need to install windows-curses: `pip install windows-curses`

### Installation
1. Clone the repository:
```bash
git clone https://github.com/KoustavDeveloper/mind-maze-adventure.git
cd mind-maze-adventure
```

2. Run the game:
```bash
python main.py
```

## 🏆 Scoring

Your score is calculated based on the remaining time when you reach the goal:
- Maximum possible score: 600 points (reaching goal instantly)
- Score formula: `remaining_time * 10`
- The faster you reach the goal, the higher your score!

## 💡 Tips & Strategies

1. **Plan Ahead**: The maze changes every 5 seconds, so try to anticipate potential wall shifts
2. **Save Your Hints**: Use hints strategically when you're stuck or running low on time
3. **Stay Flexible**: Keep multiple path options open as walls may shift and block your planned route
4. **Speed vs. Safety**: Balance the need for quick completion with careful navigation

## 🎨 Game Design

The game features a 20x10 maze with:
- Randomly generated initial layout
- 30% wall density
- 5-second interval for maze updates
- 10% chance for each wall to shift during updates

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. Some ideas for contributions:
- Add difficulty levels
- Implement high score tracking
- Create custom maze layouts
- Add power-ups or special items
- Enhance visualization effects

## 📝 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 🎬 Credits

Created with ❤️ for maze enthusiasts and puzzle lovers everywhere. Enjoy the challenge of the Mind Maze Adventure!