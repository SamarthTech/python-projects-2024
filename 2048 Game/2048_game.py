import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 450
TILE_SIZE = WIDTH // 4
FONT = pygame.font.Font(None, 40)
WHITE = (255, 255, 255)
BRIGHT_BLUE = (0, 162, 232)
BRIGHT_YELLOW = (255, 221, 51)
BRIGHT_RED = (255, 76, 76)
BRIGHT_GREEN = (76, 255, 76)
BLACK = (0, 0, 0)

# Tile colors
COLORS = {
    0: (200, 200, 200), 2: (238, 228, 218), 4: (236, 224, 200),
    8: BRIGHT_RED, 16: BRIGHT_YELLOW, 32: (246, 124, 95),
    64: (246, 94, 59), 128: BRIGHT_GREEN, 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: BRIGHT_BLUE
}

# Initialize the board
def initialize_board():
    return [[0] * 4 for _ in range(4)]

# Adding new tile after every turn
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.7 else 4

# Game over function to determine if any legal move is possible
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
    return True

# The functions to make the moves
def move_left(board):
    moved = False
    score = 0
    for row in board:
        temp = [cell for cell in row if cell != 0]
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1] and temp[i] != 0:
                temp[i] *= 2
                score += temp[i]
                temp[i + 1] = 0
                moved = True
        temp = [cell for cell in temp if cell != 0]
        while len(temp) < 4:
            temp.append(0)
        if row != temp:
            moved = True
        row[:] = temp
    return moved, score

def move_right(board):
    for row in board:
        row.reverse()
    moved, score = move_left(board)
    for row in board:
        row.reverse()
    return moved, score

def transpose(board):
    return [[board[j][i] for j in range(4)] for i in range(4)]

def move_up(board):
    board[:] = transpose(board)
    moved, score = move_left(board)
    board[:] = transpose(board)
    return moved, score

def move_down(board):
    board[:] = transpose(board)
    moved, score = move_right(board)
    board[:] = transpose(board)
    return moved, score

# To make the structure of the board using Pygame
def draw_board(screen, board, score):
    screen.fill(WHITE)
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    for i in range(4):
        for j in range(4):
            tile_value = board[i][j]
            tile_color = COLORS[tile_value]
            pygame.draw.rect(screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE + 50, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, BLACK, (j * TILE_SIZE, i * TILE_SIZE + 50, TILE_SIZE, TILE_SIZE), 2)
            if tile_value != 0:
                text = FONT.render(str(tile_value), True, BLACK)
                text_rect = text.get_rect(center=((j + 0.5) * TILE_SIZE, (i + 0.5) * TILE_SIZE + 50))
                screen.blit(text, text_rect)

    pygame.display.update()

# Making the game over screen for replay or quit and also showing the score achieved
def display_game_over(screen, score):
    screen.fill((0, 0, 0, 150))
    game_over_text = FONT.render("Game Over!", True, BRIGHT_YELLOW)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(game_over_text, text_rect)

    score_text = FONT.render(f"Your Score: {score}", True, BRIGHT_YELLOW)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    screen.blit(score_text, score_rect)

    replay_text = FONT.render("Press R to Replay or Q to Quit", True, BRIGHT_YELLOW)
    replay_rect = replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
    screen.blit(replay_text, replay_rect)

    pygame.display.update()

    # Wait for player to choose replay or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Replay the game
                    main()  # Start a new game
                elif event.key == pygame.K_q:
                    waiting = False  # Quit the game

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Game")

    board = initialize_board()
    add_new_tile(board)
    add_new_tile(board)
    score = 0

    running = True
    while running:
        draw_board(screen, board, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                moved = False
                if event.key in (pygame.K_UP, pygame.K_w):
                    moved, points = move_up(board)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    moved, points = move_left(board)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    moved, points = move_down(board)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    moved, points = move_right(board)

                if moved:
                    score += points
                    add_new_tile(board)
                    if is_game_over(board):
                        display_game_over(screen, score)
                        running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
