import random
import time

class QuantumStatePuzzle:
    def __init__(self, size=3):
        self.size = size
        self.grid = self.generate_grid()
        self.target_state = self.generate_target_state()
        self.history = []  # To keep track of previous states for undo functionality

    def generate_grid(self):
        """Generate a grid with random states (0 for off, 1 for on)."""
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def generate_target_state(self):
        """Generate a target state for the grid (0 for off, 1 for on)."""
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def print_grid(self, grid):
        """Print the grid in a readable format."""
        for row in grid:
            print(" ".join(str(x) for x in row))
        print()

    def toggle_state(self, x, y):
        """Toggle the state of the selected object and its neighbors."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]  # Up, down, left, right, and self
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.grid[nx][ny] = 1 - self.grid[nx][ny]  # Toggle between 0 and 1

    def check_win(self):
        """Check if the current grid matches the target state."""
        return self.grid == self.target_state

    def undo(self):
        """Undo the last toggle."""
        if self.history:
            self.grid = self.history.pop()  # Restore last state
        else:
            print("No moves to undo!")

    def play(self):
        """Main game loop."""
        print("Welcome to the Quantum State Puzzle!")
        print("You need to align the grid with the target state.")
        
        # Level selection
        level = input("Select a level (1: Easy, 2: Medium, 3: Hard): ")
        if level == '1':
            self.size = 3
        elif level == '2':
            self.size = 4
        elif level == '3':
            self.size = 5
        else:
            print("Invalid selection! Defaulting to Easy.")
            self.size = 3

        self.grid = self.generate_grid()
        self.target_state = self.generate_target_state()

        print("Target State:")
        self.print_grid(self.target_state)

        start_time = time.time()  # Start the timer

        while True:
            print("Current State:")
            self.print_grid(self.grid)

            elapsed_time = time.time() - start_time
            print(f"Elapsed Time: {elapsed_time:.2f} seconds")

            action = input("Enter 'x y' to toggle, 'u' to undo, or 'h' for a hint (e.g., '1 2', 'u', 'h'): ").strip().lower()
            if action == 'u':
                self.undo()
                continue
            elif action == 'h':
                self.show_hint()
                continue

            try:
                x, y = map(int, action.split())
                if not (0 <= x < self.size and 0 <= y < self.size):
                    print("Invalid coordinates! Try again.")
                    continue

                # Save the current grid to history before toggling
                self.history.append([row[:] for row in self.grid])
                self.toggle_state(x, y)

                if self.check_win():
                    print("Congratulations! You've aligned all objects!")
                    print(f"Total Time: {elapsed_time:.2f} seconds")
                    break
            except ValueError:
                print("Invalid input! Please enter two integers.")

    def show_hint(self):
        """Provide a hint by suggesting one toggle that gets closer to the target."""
        for x in range(self.size):
            for y in range(self.size):
                # Save the original state
                original_state = self.grid[x][y]
                self.toggle_state(x, y)  # Toggle
                if self.check_win():
                    print(f"Hint: Toggle the position ({x}, {y}) to win!")
                self.toggle_state(x, y)  # Toggle back
                # Restore the original state
                self.grid[x][y] = original_state

if __name__ == "__main__":
    game = QuantumStatePuzzle()
    game.play()
