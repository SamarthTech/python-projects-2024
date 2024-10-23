import math

# Constants for the players
HUMAN = "X"
AI = "O"
EMPTY = " "

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to check for a win condition
def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

# Function to check if the game is over
def is_game_over(board):
    return check_winner(board, HUMAN) or check_winner(board, AI) or is_board_full(board)

# Function to get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

# Minimax algorithm for the AI player
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row, col in get_available_moves(board):
            board[row][col] = AI
            score = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row, col in get_available_moves(board):
            board[row][col] = HUMAN
            score = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Function to get the AI's best move
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for row, col in get_available_moves(board):
        board[row][col] = AI
        score = minimax(board, 0, False)
        board[row][col] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

# Function to play TicTacToe
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = HUMAN

    while not is_game_over(board):
        print_board(board)
        if current_player == HUMAN:
            print("Your turn!")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == EMPTY:
                board[row][col] = HUMAN
                current_player = AI
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn...")
            row, col = get_best_move(board)
            board[row][col] = AI
            current_player = HUMAN

    print_board(board)
    if check_winner(board, HUMAN):
        print("Congratulations! You win!")
    elif check_winner(board, AI):
        print("AI wins! Better luck next time.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
