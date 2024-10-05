import pygame
from sys import exit
import random
import array as arr

s_x = 300
s_y = 300

a_x = 330
a_y = 300

score = 0
snake_position = [(s_x,s_y)]
t_snake_position = [(s_x,s_y)]

speed = 15
movement = 0
lastkeypress = 0
clocktickspeed = 20

pygame.display.init()
screen = pygame.display.set_mode((1023,600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

apple = pygame.Surface((60, 60), pygame.SRCALPHA)
snake = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.rect(snake,(250,0,0), pygame.Rect(47,47,60,60))
pygame.draw.rect(apple,(0,250,0), pygame.Rect(47, 47, 60, 60))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))    

    if(s_x < -30 or s_x > 970):
        pygame.quit()
    elif(s_y < -30 or s_y > 530):
        pygame.quit()

    if(score > 0):
        for i in range(score , 0 , -1):
            snake_position[i] = snake_position[i-1] 

    #movement
    if (lastkeypress == 1):
        s_y += speed
    elif (lastkeypress == 2):
        s_y -= speed
    elif (lastkeypress == 3):
        s_x += speed
    elif (lastkeypress == 4):
        s_x -= speed

    


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:            
            lastkeypress = 1            
        elif event.key == pygame.K_UP:            
            lastkeypress = 2
        elif event.key == pygame.K_RIGHT:            
            lastkeypress = 3
        elif event.key == pygame.K_LEFT:            
            lastkeypress = 4
    
    

        

    #if statement which updates the coordinates of the apple
    if ( a_x == s_x and a_y == s_y ):
        a_x = random.randrange(60,1006,15)
        a_y = random.randrange(60,511,15)
        score += 1

        if(lastkeypress == 1):
            snake_position.append((s_x,s_y - 15))
        elif(lastkeypress == 2):
            snake_position.append((s_x,s_y + 15))
        elif(lastkeypress == 3):
            snake_position.append((s_x - 15,s_y))
        elif(lastkeypress == 4):
            snake_position.append((s_x + 15,s_y))
    
    screen.blit(apple,(a_x,a_y))

    #snake body 
    if ( score == 0 ):
        screen.blit(snake,(s_x,s_y))
    else:
        screen.blit(snake,(snake_position[0]))
        for i in range(  1 , score + 1 , 1 ):
            screen.blit(snake,(snake_position[i]))

    snake_position[0] = (s_x,s_y)


    print(snake_position,a_x,a_y)

    pygame.display.update() 
    
    if (score > 10):
        clocktickspeed + 5
    #tells the while loop to not run this loop more than 60 times per second
    clock.tick(clocktickspeed)