import pygame
import sys
from game import Game
from ai import AI

pygame.init()

WIDTH, HEIGHT = 300, 600  # Adjusted to match the game grid size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Tetris")

clock = pygame.time.Clock()
game = Game(WIDTH, HEIGHT)
ai = AI(game)

# Uncomment the following line if you want to run the genetic algorithm
# ai.genetic_algorithm(generations=100, population_size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    try:
        ai.make_move()
        game.update()

        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()

    clock.tick(5)  # Slowed down to 5 FPS for better visibility