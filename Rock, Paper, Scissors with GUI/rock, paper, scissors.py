import pygame
import random

pygame.init()

# Set window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Define colors for UI
BACKGROUND_COLOR = (10, 15, 25)
WHITE = (255, 255, 255)
LIGHT_BLUE = (0, 158, 231)
YELLOW = (252, 200, 0)
RED = (237, 41, 57)

# Load images for Rock, Paper, Scissors
rock_img = pygame.image.load('images/rock.png')
paper_img = pygame.image.load('images/paper.png')
scissors_img = pygame.image.load('images/scissors.png')
logo = pygame.image.load('images/logo.png')

# Resize images for circular buttons
rock_img = pygame.transform.scale(rock_img, (120, 120))
paper_img = pygame.transform.scale(paper_img, (120, 120))
scissors_img = pygame.transform.scale(scissors_img, (120, 120))
logo = pygame.transform.scale(logo, (350, 214))

# Font for text
font = pygame.font.Font('Font/Haettenschweiler-Regular.ttf', 40)

# Game variables
choices = ['rock', 'paper', 'scissors']
player_choice = None
computer_choice = None
result = None
player_score = 0
computer_score = 0

# Function to draw circular buttons
def draw_circle_button(image, color, pos_x, pos_y, radius):
    pygame.draw.circle(screen, color, (pos_x, pos_y), radius)
    screen.blit(image, (pos_x - image.get_width() // 2, pos_y - image.get_height() // 2))

# Functions to display text on the screen
def render_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Function to check if a button is clicked
def is_button_clicked(pos_x, pos_y, mouse_x, mouse_y, radius):
    return (mouse_x - pos_x) ** 2 + (mouse_y - pos_y) ** 2 <= radius ** 2

# Function to determine the winner
def determine_winner(player, computer):
    global player_score, computer_score
    if player == computer:
        return "DRAW"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        player_score += 1
        return "You Win!"
    else:
        computer_score += 1
        return "Computer Wins!"

# Function to display choices with the result in the middle
def display_choices_and_result(player_choice, computer_choice, result):
    images = {'rock': rock_img, 'paper': paper_img, 'scissors': scissors_img}
    player_img = images[player_choice]
    screen.blit(player_img, (SCREEN_WIDTH // 2 - 250,SCREEN_HEIGHT // 2 - 75))
    computer_img = images[computer_choice]
    screen.blit(computer_img, (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 - 75))
    text_obj = font.render(result, True, WHITE)
    text_rect = text_obj.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text_obj, text_rect)

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Render Title (Rock Paper Scissors)
    screen.blit(logo,(0,0))

    # Render Player and Computer Scores
    render_text(f'Player: {player_score}', font, WHITE, SCREEN_WIDTH - 165, 80)
    render_text(f'Computer: {computer_score}', font, WHITE, SCREEN_WIDTH - 210, 30)
    
    # Render choices and result (rearranged section)
    if player_choice and computer_choice:
        display_choices_and_result(player_choice, computer_choice, result)

    # Draw circular buttons for choices (swapped position)
    draw_circle_button(rock_img, RED, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 200, 80)
    draw_circle_button(paper_img, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, 80)
    draw_circle_button(scissors_img, LIGHT_BLUE, SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 + 200, 80)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Check if a choice button is clicked
            if is_button_clicked(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 200, mouse_x, mouse_y, 80):
                player_choice = 'rock'
            elif is_button_clicked(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, mouse_x, mouse_y, 80):
                player_choice = 'paper'
            elif is_button_clicked(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 + 200, mouse_x, mouse_y, 80):
                player_choice = 'scissors'
            
            # Once a choice is made, the computer randomly chooses
            if player_choice:
                computer_choice = random.choice(choices)
                result = determine_winner(player_choice, computer_choice)

    pygame.display.flip()

pygame.quit()
