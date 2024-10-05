import pygame
import random
import numpy as np
from collections import deque
import heapq

# Initialize Pygame
pygame.init()

# Set up the game window
width = 1000
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Snake Game AI")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Game parameters
snake_block = 20
initial_speed = 15
obstacle_count = 10
power_up_duration = 50  # frames

# Initialize clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 30)

# Sound effects
# pygame.mixer.init()
# eat_sound = pygame.mixer.Sound("eat.wav")
# power_up_sound = pygame.mixer.Sound("power_up.wav")
# game_over_sound = pygame.mixer.Sound("game_over.wav")

def our_snake(snake_block, snake_list, color=GREEN):
    for x in snake_list:
        pygame.draw.rect(window, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [10, 10 + y_displace])

def bfs(start, goal, grid):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        
        if (y, x) == goal:
            return path
        
        for y2, x2 in ((y+1,x), (y-1,x), (y,x+1), (y,x-1)):
            if (0 <= y2 < grid.shape[0] and 0 <= x2 < grid.shape[1] and 
                grid[int(y2)][int(x2)] != 1 and (y2, x2) not in visited):
                queue.append(path + [(y2, x2)])
                visited.add((y2, x2))
    
    return None

def astar(start, goal, grid):
    def heuristic(a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])
    
    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    open_set = []
    heapq.heappush(open_set, (fscore[start], start))
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        close_set.add(current)
        
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1] and grid[neighbor[0]][neighbor[1]] != 1:
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_set]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = gscore[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (fscore[neighbor], neighbor))
    
    return None

def ai_make_decision(x1, y1, foodx, foody, snake_list, obstacles, power_up, algorithm='bfs'):
    grid = np.zeros((height // snake_block, width // snake_block))
    
    for segment in snake_list:
        grid[int(segment[1] // snake_block)][int(segment[0] // snake_block)] = 1
    
    for obs in obstacles:
        grid[int(obs[1] // snake_block)][int(obs[0] // snake_block)] = 1
    
    start = (y1 // snake_block, x1 // snake_block)
    goal = (foody // snake_block, foodx // snake_block)
    
    if algorithm == 'bfs':
        path = bfs(start, goal, grid)
    elif algorithm == 'astar':
        path = astar(start, goal, grid)
    
    if power_up:
        power_up_goal = (power_up[1] // snake_block, power_up[0] // snake_block)
        if algorithm == 'bfs':
            path_to_power_up = bfs(start, power_up_goal, grid)
        elif algorithm == 'astar':
            path_to_power_up = astar(start, power_up_goal, grid)
        
        if path_to_power_up and (not path or len(path_to_power_up) < len(path)):
            path = path_to_power_up
    
    if path:
        next_move = path[1]
        dx = (next_move[1] * snake_block) - x1
        dy = (next_move[0] * snake_block) - y1
        return dx, dy, path
    else:
        possible_moves = [
            (snake_block, 0), (-snake_block, 0), (0, snake_block), (0, -snake_block)
        ]
        for move in possible_moves:
            new_x = x1 + move[0]
            new_y = y1 + move[1]
            if (0 <= new_x < width and 0 <= new_y < height and 
                [new_x, new_y] not in snake_list and [new_x, new_y] not in obstacles):
                return move[0], move[1], None
        
        return 0, 0, None

def gameLoop(mode='single', algorithm='bfs'):
    game_over = False
    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    score = 0
    power_up_active = 0
    level = 1
    snake_speed = initial_speed

    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    obstacles = [[round(random.randrange(0, width - snake_block) / snake_block) * snake_block,
                  round(random.randrange(0, height - snake_block) / snake_block) * snake_block]
                 for _ in range(obstacle_count)]

    power_up = None
    power_up_timer = 0

    # Multi-snake mode
    if mode == 'multi':
        x2 = width // 4
        y2 = height // 4
        snake_list2 = []
        length_of_snake2 = 1
        score2 = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        x1_change, y1_change, path = ai_make_decision(x1, y1, foodx, foody, snake_list, obstacles, power_up, algorithm)

        if mode == 'multi':
            x2_change, y2_change, _ = ai_make_decision(x2, y2, foodx, foody, snake_list2, obstacles, power_up, 'bfs')

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
            break

        x1 += x1_change
        y1 += y1_change
        
        if mode == 'multi':
            x2 += x2_change
            y2 += y2_change

        window.fill(BLACK)
        
        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(window, BLUE, [obs[0], obs[1], snake_block, snake_block])
        
        # Draw food
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        
        # Draw power-up
        if power_up:
            pygame.draw.rect(window, YELLOW, [power_up[0], power_up[1], snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_list)
        
        if mode == 'multi':
            snake_head2 = [x2, y2]
            snake_list2.append(snake_head2)
            if len(snake_list2) > length_of_snake2:
                del snake_list2[0]
            our_snake(snake_block, snake_list2, PURPLE)
        
        # Draw path
        if path:
            for node in path[1:]:
                pygame.draw.rect(window, (100, 100, 100), 
                                 [node[1]*snake_block, node[0]*snake_block, snake_block, snake_block], 1)

        if power_up_active > 0:
            message(f"Score: {score} - POWER UP!", YELLOW)
            power_up_active -= 1
        else:
            message(f"Score: {score}", WHITE)
        
        message(f"Level: {level}", WHITE, 30)
        
        if mode == 'multi':
            message(f"Score 2: {score2}", PURPLE, 60)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            # eat_sound.play()
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            score += 1
            
            # Level up and increase speed
            if score % 5 == 0:
                level += 1
                snake_speed += 2
            
            # Spawn power-up
            if random.random() < 0.3 and not power_up:  # 30% chance to spawn power-up
                power_up = [round(random.randrange(0, width - snake_block) / snake_block) * snake_block,
                            round(random.randrange(0, height - snake_block) / snake_block) * snake_block]

        if mode == 'multi' and x2 == foodx and y2 == foody:
            # eat_sound.play()
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake2 += 1
            score2 += 1

        if power_up and x1 == power_up[0] and y1 == power_up[1]:
            # power_up_sound.play()
            power_up = None
            power_up_active = power_up_duration
            score += 5

        clock.tick(snake_speed)

    # Game over
    # game_over_sound.play()
    message("Game Over!", RED)
    message(f"Final Score: {score}", WHITE, 30)
    if mode == 'multi':
        message(f"Final Score 2: {score2}", PURPLE, 60)
    pygame.display.update()
    
    # Wait for a few seconds before quitting
    pygame.time.wait(3000)
    
    pygame.quit()
    quit()

# Start menu
def start_menu():
    menu = True
    selected = 0
    options = ['Single Player (BFS)', 'Single Player (A*)', 'Multi-snake Mode']

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        gameLoop(mode='single', algorithm='bfs')
                    elif selected == 1:
                        gameLoop(mode='single', algorithm='astar')
                    elif selected == 2:
                        gameLoop(mode='multi', algorithm='bfs')

        window.fill(BLACK)
        title = font.render('Advanced Snake Game AI', True, WHITE)
        window.blit(title, (width//2 - title.get_width()//2, 50))

        for i, option in enumerate(options):
            color = RED if i == selected else WHITE
            text = font.render(option, True, color)
            window.blit(text, (width//2 - text.get_width()//2, 200 + i*50))

        pygame.display.update()
        clock.tick(15)

# Start the game
start_menu()