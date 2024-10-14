import pygame
from os import path
from random import randint, uniform

#initial setup
pygame.init()
clock = pygame.time.Clock()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
displaySurf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Space Shooter")

#imports
playerSurf = pygame.image.load(path.join("..", "images", "player.png")).convert_alpha()
laserSurf = pygame.image.load(path.join("..", "images", "laser.png")).convert_alpha()
meteorSurf = pygame.image.load(path.join("..", "images", "meteor.png")).convert_alpha()
starSurf = pygame.image.load(path.join("..", "images", "star.png")).convert_alpha()
font = pygame.font.Font(path.join("..", "images", "Oxanium-Bold.ttf"), 40)
animatedExplosions = [pygame.image.load(path.join("..", "images", "explosion", str(i)+".png")).convert_alpha() for i in range(21)]
laserSound = pygame.mixer.Sound(path.join("..", "audio", "laser.wav"))
laserSound.set_volume(0.5)
explosionSound = pygame.mixer.Sound(path.join("..", "audio", "explosion.wav"))
gameSound = pygame.mixer.Sound(path.join("..", "audio", "game_music.wav"))
gameSound.set_volume(0.1)
gameSound.play(loops = -1)

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.cooldown_duration = 500
        self.can_shoot = True
        self.shoot_time = 0
        self.mask = pygame.mask.from_surface(self.image)

    def laser_time(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):    
        #player movement here
        keys = pygame.key.get_pressed()
        self.direction.x = (int(keys[pygame.K_RIGHT]) or int(keys[pygame.K_d])) - (int(keys[pygame.K_LEFT]) or int(keys[pygame.K_a]))
        self.direction.y = (int(keys[pygame.K_DOWN]) or int(keys[pygame.K_s])) - (int(keys[pygame.K_UP]) or int(keys[pygame.K_w]))
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * (self.speed * dt)
        shoot_key = pygame.key.get_just_pressed()
        if (shoot_key[pygame.K_SPACE]) and self.can_shoot:
            Laser(laserSurf, self.rect.midtop, (all_sprites, laser_sprites))
            laserSound.play()
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        self.laser_time()

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (pos))

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if (self.rect.bottom < 0):
            self.kill()
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.original_image = surf
        self.image = self.original_image
        self.rect = self.image.get_frect(center = pos)
        self.meteor_speed = randint(400, 500)
        self.meteor_direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.rotation_speed = 0

    def update(self, dt):
        self.rect.center += self.meteor_direction * self.meteor_speed * dt
        self.rotation_speed += (randint(50, 150) * dt)
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation_speed, 1)
        self.rect = self.image.get_frect(center = self.rect.center)
        if (self.rect.top > WINDOW_HEIGHT):
            self.kill()
        
class Star(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

class AnimatedExposions(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

#collision logic
def collisions():
    global isRunning
    player_collision = pygame.sprite.spritecollide(player, meteor_sprites, False)
    if player_collision:
        isRunning = False

    for laser in laser_sprites:
        collided_lasers = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_lasers:
            laser.kill()
            explosionSound.play()
            AnimatedExposions(animatedExplosions, laser.rect.midtop, all_sprites)

def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (240, 240, 240))
    text_rect = text_surf.get_frect(left = 20, top = 20)
    displaySurf.blit(text_surf, text_rect)
    pygame.draw.rect(displaySurf, "purple", text_rect.inflate(20, 10).move(0, -8), 5, 10)

#sprite_creation
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
player = Player(playerSurf, all_sprites)
for i in range(20):
    Star(starSurf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)), all_sprites)
    
#custom_event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

isRunning = True
while isRunning:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == meteor_event:
            Meteor(meteorSurf, (randint(0, WINDOW_WIDTH), randint(-200, -100)) , (all_sprites, meteor_sprites))

    all_sprites.update(dt)
    collisions()
    displaySurf.fill("#3a2e3f")
    all_sprites.draw(displaySurf)
    display_score()
    
    pygame.display.flip()

pygame.quit()