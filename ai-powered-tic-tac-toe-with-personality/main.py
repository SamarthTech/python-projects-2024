import tkinter as tk
from tkinter import messagebox
import random

# Constants for the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# AI personalities
PERSONALITIES = {
    "aggressive": "AGGRESSIVE",
    "cautious": "CAUTIOUS",
    "unpredictable": "UNPREDICTABLE"
}

class TicTacToe:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X
        self.game_over = False
        self.update_buttons()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = buttons[i][j]
                btn.config(text=self.board[i][j], state=tk.NORMAL if self.board[i][j] == EMPTY else tk.DISABLED)

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all([cell == player for cell in self.board[i]]):  # Check row
                return True
            if all([self.board[j][i] == player for j in range(3)]):  # Check column
                return True
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2 - i] == player for i in range(3)]):  # Check diagonals
            return True
        return False

    def is_full(self):
        return all(cell != EMPTY for row in self.board for cell in row)

    def make_move(self, row, col, player):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player
            return True
        return False

    def ai_move(self, personality):
        if personality == PERSONALITIES["aggressive"]:
            self.aggressive_ai_move()
        elif personality == PERSONALITIES["cautious"]:
            self.cautious_ai_move()
        elif personality == PERSONALITIES["unpredictable"]:
            self.unpredictable_ai_move()

    def aggressive_ai_move(self):
        # Try to win if possible, else block opponent
        for move in self.get_available_moves():
            self.make_move(move[0], move[1], PLAYER_O)  # Assume AI is PLAYER_O
            if self.is_winner(PLAYER_O):
                return
            self.make_move(move[0], move[1], EMPTY)  # Undo move

        for move in self.get_available_moves():
            self.make_move(move[0], move[1], PLAYER_X)  # Assume Player X is PLAYER_X
            if self.is_winner(PLAYER_X):
                self.make_move(move[0], move[1], PLAYER_O)
                return
            self.make_move(move[0], move[1], EMPTY)  # Undo move

        # If no immediate win or block, choose a random move
        self.random_ai_move()

    def cautious_ai_move(self):
        # Try to block opponent if they are about to win
        for move in self.get_available_moves():
            self.make_move(move[0], move[1], PLAYER_X)  # Assume Player X is PLAYER_X
            if self.is_winner(PLAYER_X):
                self.make_move(move[0], move[1], PLAYER_O)
                return
            self.make_move(move[0], move[1], EMPTY)  # Undo move

        # If no blocks needed, choose a random move
        self.random_ai_move()

    def unpredictable_ai_move(self):
        # Randomly select a move
        self.random_ai_move()

    def random_ai_move(self):
        move = random.choice(self.get_available_moves())
        self.make_move(move[0], move[1], PLAYER_O)

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]

    def minimax(self, board, depth, is_maximizing):
        if self.is_winner(PLAYER_O):
            return 10 - depth
        if self.is_winner(PLAYER_X):
            return depth - 10
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_available_moves():
                board[move[0]][move[1]] = PLAYER_O
                score = self.minimax(board, depth + 1, False)
                board[move[0]][move[1]] = EMPTY
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                board[move[0]][move[1]] = PLAYER_X
                score = self.minimax(board, depth + 1, True)
                board[move[0]][move[1]] = EMPTY
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_O
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play_game(self):
        while True:
            if self.current_player == PLAYER_X:
                break
            else:
                row, col = self.best_move()
                self.make_move(row, col, PLAYER_O)

            if self.is_winner(self.current_player):
                self.update_buttons()
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
                break
            if self.is_full():
                self.update_buttons()
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
                break

            # Switch player
            self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O


def button_click(row, col):
    if game.game_over:
        return

    if game.make_move(row, col, PLAYER_X):
        game.update_buttons()
        if game.is_winner(PLAYER_X):
            messagebox.showinfo("Game Over", "X wins!")
            game.reset_game()
            return
        if game.is_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            game.reset_game()
            return
        game.current_player = PLAYER_O
        game.play_game()


# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe with AI")
game = TicTacToe()

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=EMPTY, font=('Arial', 40), width=5, height=2,
                                   command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
