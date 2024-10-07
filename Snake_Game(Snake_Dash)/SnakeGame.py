import pygame, sys, random, os
from pygame.math import Vector2
pygame.init()

# Background Images
GAMEOVER = pygame.image.load("Images/game_over.jpg")
GAMEOVER = pygame.transform.scale(GAMEOVER, (800, 800))
WELCOME = pygame.image.load("Images/welcome.jpg")
WELCOME = pygame.transform.scale(WELCOME, (800, 800))

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.load_graphics()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
        self.game_over_sound = pygame.mixer.Sound('Sound/game_over.wav')
        self.score = 0
    
    def load_graphics(self):
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                if block.y == self.body[index - 1].y and block.y == self.body[index + 1].y:
                    screen.blit(self.body_horizontal, block_rect)
                elif block.x == self.body[index - 1].x and block.x == self.body[index + 1].x:
                    screen.blit(self.body_vertical, block_rect)
                else:
                    prev_block = self.body[index - 1] - block
                    next_block = self.body[index + 1] - block
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
    
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
        self.score += 1
    
    def play_crunch_sound(self):
        self.crunch_sound.play()
    
    def play_game_over_sound(self):
        self.game_over_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.score = 0

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class GRASS:
    def __init__(self):
        self.color1 = (167, 209, 61)
        self.color2 = (175, 215, 70)
    
    def draw_grass(self):
        for row in range(cell_number):
            if row % 2 == 0: 
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, self.color1, grass_rect)
                    else:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, self.color2, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, self.color2, grass_rect)
                    else:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, self.color1, grass_rect)
def draw_elements():
    grass.draw_grass()
    fruit.draw_fruit()
    snake.draw_snake()
    draw_score()

def check_fail():
    if not 0 <= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
        return True
    for block in snake.body[1:]:
        if block == snake.body[0]:
            return True
    return False

def show_game_over():
    screen.blit(GAMEOVER, (0, 0))

def welcome():
    screen.blit(WELCOME, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

def draw_score():
    score_surface = game_font.render(f'{snake.score}', True, (56, 74, 12))
    score_x = int(cell_size * cell_number - 60)
    score_y = int(cell_size * cell_number - 40)
    score_rect = score_surface.get_rect(center=(score_x, score_y))
    apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

    high_score_surface = game_font.render(f'       {high_score}', True, (56, 74, 12))
    high_score_x = int(cell_size * cell_number - 700)
    high_score_y = int(cell_size * cell_number - 40)
    high_score_rect = high_score_surface.get_rect(center=(high_score_x, high_score_y))
    trophie_rect = trophie.get_rect(midleft = (high_score_rect.left, high_score_rect.centery))
    
    screen.blit(score_surface, score_rect)
    screen.blit(high_score_surface, high_score_rect)
    screen.blit(apple, apple_rect)
    screen.blit(trophie, trophie_rect)

def save_high_score(new_high_score):
    with open('high_score.txt', 'w') as file:
        file.write(str(new_high_score))

def load_high_score():
        if (not os.path.exists("high_score.txt")):
            with open("high_score.txt", "w") as f:
                f.write("0")
        with open('high_score.txt', 'r') as file:
            return int(file.read())


# Screen settings
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake Dash")
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
trophie = pygame.image.load('Graphics\Trophie.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
snake = SNAKE()
fruit = FRUIT()
grass = GRASS()
game_state = 'running'
game_over_sound_played = False
high_score = load_high_score()

def gameloop():
    global game_state
    global game_over_sound_played
    global high_score
    game_state = 'running'
    game_over_sound_played = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE and game_state == 'running':
                snake.move_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and game_state == 'over':
                    if snake.score > high_score:
                        high_score = snake.score
                        save_high_score(high_score)
                    snake.reset()
                    fruit.randomize()
                    welcome()
                    game_state = 'running'
                    game_over_sound_played = False
                if event.key == pygame.K_UP and snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                    snake.direction = Vector2(1, 0)
        
        if game_state == 'running':
            if check_fail():
                game_state = 'over'
                snake.play_game_over_sound()
                game_over_sound_played = True
                if snake.score > high_score:
                    high_score = snake.score
                    save_high_score(high_score)
            if snake.body[0] == fruit.pos:
                snake.add_block()
                fruit.randomize()
                snake.play_crunch_sound()
        
        draw_elements()
        
        if game_state == 'over':
            show_game_over()
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

welcome()