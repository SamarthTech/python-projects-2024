# Quantum State Puzzle

A challenging puzzle game where players must manipulate quantum states to match a target configuration. The game features a grid-based interface where toggling one state affects neighboring states, creating an engaging puzzle-solving experience.

## Features

- Multiple difficulty levels (Easy, Medium, Hard)
- Grid sizes from 3x3 to 5x5
- Interactive state toggling mechanism
- Undo functionality
- Hint system
- Progress timer
- Target state visualization

## How to Play

1. **Setup**: Run the game using Python 3:
   ```bash
   python main.py
   ```

2. **Select Difficulty**:
   - Easy (3x3 grid)
   - Medium (4x4 grid)
   - Hard (5x5 grid)

3. **Game Rules**:
   - The game displays two grids: the target state and your current state
   - Each cell can be in one of two states: 0 (off) or 1 (on)
   - Toggling a cell affects both the selected cell and its adjacent cells (up, down, left, right)
   - Your goal is to match your current state with the target state

4. **Controls**:
   - Enter coordinates as "x y" (e.g., "1 2") to toggle a cell
   - Enter "u" to undo your last move
   - Enter "h" to receive a hint

5. **Winning**:
   - The game ends when your current state matches the target state
   - Your completion time will be displayed

## Game Interface Example

```
Target State:
1 0 1
0 1 0
1 0 1

Current State:
0 1 0
1 0 1
0 1 0

Enter 'x y' to toggle, 'u' to undo, or 'h' for a hint (e.g., '1 2', 'u', 'h'):
```

## Requirements

- Python 3.x
- Standard Python libraries:
  - random
  - time

## Installation

1. Clone the repository or download the source code
2. Navigate to the project directory
3. Run the game:
   ```bash
   python main.py
   ```

## Technical Details

### Classes and Methods

- `QuantumStatePuzzle`: Main game class
  - `generate_grid()`: Creates random initial state
  - `generate_target_state()`: Creates random target state
  - `toggle_state(x, y)`: Toggles states of selected and adjacent cells
  - `check_win()`: Verifies if current state matches target
  - `undo()`: Reverts to previous state
  - `show_hint()`: Provides strategic guidance
  - `play()`: Main game loop

### State Management

- States are represented as 2D arrays of binary values (0/1)
- Move history is maintained for undo functionality
- Grid boundaries are enforced during state transitions

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Committing your changes
4. Opening a pull request

## Future Improvements

- Save/load game functionality
- High score system
- Additional puzzle patterns
- Graphical user interface
- Sound effects
- Achievement system
- Multiple game modes

## License

This project is open source and available under the MIT License.

## Author

[Koustav Singh](https://github.com/KoustavDeveloper/)

---

*Note: This quantum state puzzle is a simulation and does not represent actual quantum mechanics. It is designed for entertainment and puzzle-solving purposes only.*