# 🎮 Python Minesweeper Game

A classic Minesweeper implementation built with Python and Tkinter. Challenge yourself with this timeless puzzle game where every click could be your last!

## 🚀 Features

- Clean and intuitive graphical interface
- Real-time game timer
- Mine and flag counter
- Right-click flagging system
- Auto-clear for empty regions
- Victory and defeat detection
- Play again option

## 🎯 How to Play

1. Left-click to reveal a tile
2. Right-click to place/remove a flag
3. Numbers indicate how many mines are adjacent to that tile
4. Clear all non-mine tiles to win
5. Flag all mines correctly for a perfect score
6. Be careful - one wrong click on a mine ends the game!

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- Required image files (see below)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/KoustavDeveloper/python-minesweeper-game.git
cd python-minesweeper-game
```

2. Ensure you have the following image files in an `images` directory:
- tile_plain.gif
- tile_clicked.gif
- tile_mine.gif
- tile_flag.gif
- tile_wrong.gif
- tile_1.gif through tile_8.gif (number tiles)

3. Run the game:
```bash
python main.py
```

## 🎮 Game Controls

- **Left Click**: Reveal tile
- **Right Click**: Place/remove flag
- **MacOS Note**: Use middle click instead of right click for flagging

## ⚙️ Configuration

You can modify these constants in `main.py` to customize the game:

```python
SIZE_X = 10  # Number of rows
SIZE_Y = 10  # Number of columns
```

The mine density is currently set to 10% (0.1) and can be adjusted in the `setup()` method.

## 🎥 Preview

```
+------------------+
|    00:00:00     |
|  [ ][ ][ ][ ]   |
|  [ ][1][1][ ]   |
|  [ ][1][🚩][ ]  |
|  [ ][1][1][ ]   |
| Mines: 5 Flags: 1|
+------------------+
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements you'd like to add, such as:

- Difficulty levels
- Custom grid sizes
- High score system
- Sound effects
- Better mine distribution
- Custom themes

## 📝 License

This project is available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as you please.

## 🙏 Acknowledgments

- Inspired by the classic Microsoft Minesweeper
- Built with Python's Tkinter library
- Uses a queue-based flood fill algorithm for revealing empty tiles

## 🐛 Known Issues

- The first click is not guaranteed to be safe
- No option to customize difficulty settings through UI
- Timer continues until game is closed

Enjoy the game! Remember: patience and strategy are key to becoming a Minesweeper master! 🎮✨