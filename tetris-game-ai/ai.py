import random
from game import Game

class AI:
    def __init__(self, game):
        self.game = game
        self.weights = {
            'height': -0.510066,
            'lines': 0.760666,
            'holes': -0.35663,
            'bumpiness': -0.184483
        }

    def make_move(self):
        if self.game.current_piece is None:
            return  # No move to make if there's no current piece

        best_move = self.find_best_move()
        self.execute_move(best_move)

    def find_best_move(self):
        if self.game.current_piece is None:
            return None  # No move to find if there's no current piece

        best_score = float('-inf')
        best_move = None

        for rotation in range(4):
            for x in range(self.game.grid_width):
                test_piece = {
                    'shape': self.game.current_piece['shape'],
                    'x': x,
                    'y': self.game.current_piece['y'],
                    'color': self.game.current_piece['color']
                }

                for _ in range(rotation):
                    test_piece['shape'] = list(zip(*test_piece['shape'][::-1]))

                if self.game.can_move(test_piece):
                    while self.game.can_move(test_piece, dy=1):
                        test_piece['y'] += 1

                    score = self.evaluate_move(test_piece)
                    if score > best_score:
                        best_score = score
                        best_move = (rotation, x)

        return best_move

    def evaluate_move(self, piece):
        # Create a copy of the game grid to simulate the move
        test_grid = [row[:] for row in self.game.grid]
        
        # Place the piece on the test grid
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    test_grid[piece['y'] + y][piece['x'] + x] = piece['color']

        # Calculate features
        height = self.calculate_height(test_grid)
        lines = self.calculate_lines(test_grid)
        holes = self.calculate_holes(test_grid)
        bumpiness = self.calculate_bumpiness(test_grid)

        # Calculate score using weights
        score = (
            self.weights['height'] * height +
            self.weights['lines'] * lines +
            self.weights['holes'] * holes +
            self.weights['bumpiness'] * bumpiness
        )

        return score

    def calculate_height(self, grid):
        return max(self.game.grid_height - row.index(1) if 1 in row else 0 for row in zip(*grid))

    def calculate_lines(self, grid):
        return sum(all(cell for cell in row) for row in grid)

    def calculate_holes(self, grid):
        holes = 0
        for col in zip(*grid):
            block_found = False
            for cell in col:
                if cell:
                    block_found = True
                elif block_found:
                    holes += 1
        return holes

    def calculate_bumpiness(self, grid):
        heights = [0] * self.game.grid_width
        for x in range(self.game.grid_width):
            for y in range(self.game.grid_height):
                if grid[y][x]:
                    heights[x] = self.game.grid_height - y
                    break
        return sum(abs(heights[i] - heights[i+1]) for i in range(len(heights)-1))

    def execute_move(self, move):
        if move is None:
            return

        rotation, x = move

        for _ in range(rotation):
            self.game.rotate_piece()

        while self.game.current_piece['x'] < x:
            self.game.move_right()
        while self.game.current_piece['x'] > x:
            self.game.move_left()

        self.game.drop()

# Ensure the AI class is properly exported
__all__ = ['AI']