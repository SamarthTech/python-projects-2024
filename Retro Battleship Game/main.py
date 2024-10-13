import pygame
from sys import exit

#initialise the program
pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#font setup
font = pygame.font.SysFont(None, 100)

def display_message(text):
    screen.fill(BLACK)  # Fill screen with white background
    lines = text.split('\n')  # Split the text into lines
    y_offset = 100  # Initial vertical position to start displaying text
    for line in lines:
        message = font.render(line, True, YELLOW)  # Render each line with yellow color
        text_rect = message.get_rect(center=(window_width // 2, y_offset))  # Position each line
        screen.blit(message, text_rect)  # Draw the text onto the screen
        y_offset += 100  # Move down for the next line
    pygame.display.update()


window_width = 800
window_height = 600
clock = pygame.time.Clock()
pygame.display.set_caption('Retro Battleship Game')
screen = pygame.display.set_mode((window_width,window_height))

#load our images
player_spaceship = pygame.image.load("spaceship.png")
opponent_spaceship = pygame.image.load("opponentpaceship.png")
player_bullet = pygame.image.load("player_bullet2.png")
opponent_bullet = pygame.image.load("hahaha.png")

#making rectangles
player_spaceship_rect = player_spaceship.get_rect()
opponent_spaceship_rect = opponent_spaceship.get_rect()
player_bullet_rect = player_bullet.get_rect()
opponent_bullet_rect = opponent_bullet.get_rect()

#making changes to the opponent bullet
# opponent_bullet_rect.width = 30
# opponent_bullet_rect.height = 15

#bulletspeed
bullet_speed = 15
opponent_bullet_speed = 20
blegh = 0
meow = 7
start = True

#position
player_position_x = 0
player_position_y = 300
opponent_position_x = 800
opponent_position_y = 300

player_spaceship_rect.midleft = (player_position_x,player_position_y)
player_bullet_rect.midleft = (player_position_x + 50, player_position_y)

opponent_spaceship_rect.midright = (opponent_position_x,opponent_position_y)

#array for player_bullet pos
player_bullet_array = []
player_bullet_rect_array = []
opponent_bullet_rect_array = []

#for opponent movement
opponent_movement = 0

#total hits
player_hits = 3
opponent_hits = 20

#total hits required
t_player_hits = 20
t_opponent_hits = 4

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if start:
        display_message("Hit the Opponent \n Spaceship \n 20 times and win \n  or get hit 3 times \n  and die!!")
        pygame.time.wait(3000)
        start = False
    

    if player_hits == 0:
        display_message("YOU LOSE")
        pygame.time.wait(3000)
        exit()
    if opponent_hits == 0:
        display_message("YOU WON")
        pygame.time.wait(3000)
        exit()

    if blegh == 10:
        blegh = 0

   
        
    #Don't change anything here
    print(blegh)
    #it took me 4 friggin hours to code this piece of $hitty loop
    if ( len(player_bullet_array) != 0): #gets rid of rect in array
        t2_array = []#Don't change anything here
        t2_array = player_bullet_array[0]#Don't change anything here
        if ( t2_array[0] > 800 ):#Don't change anything here
            player_bullet_array.pop(0)#Don't change anything here
        
        for i in range ( 0 , len(player_bullet_array) , 1): #adds up the array with bullet speed
            t_array = []#Don't change anything here
            t_array = player_bullet_array[i]#Don't change anything here
            t_array[0] = t_array[0] + bullet_speed#Don't change anything here
            player_bullet_array[i] = t_array#Don't change anything here
#Don't change anything here
    if (len(player_bullet_rect_array) != 0):#Don't change anything here 
        t1_array = []#Don't change anything here
        t1_array = player_bullet_rect_array[0].x#Don't change anything here
        if ( t1_array > 800):#Don't change anything here
            player_bullet_rect_array.pop(0)#Don't change anything here
        #Don't change anything here
        for i in range ( 0 , len(player_bullet_rect_array) , 1):#Don't change anything here
            t_array = []#Don't change anything here
            t_array = player_bullet_rect_array[i].x#Don't change anything here
            t_array = t_array + bullet_speed#Don't change anything here
            player_bullet_rect_array[i].x = t_array#Don't change anything here

    #collision system for player bullet and opponent spaceship
    for i in range ( 0 , len(player_bullet_rect_array) , 1):
        if player_bullet_rect_array[i].colliderect(opponent_spaceship_rect):
            opponent_hits = opponent_hits - 1
            player_bullet_rect_array.pop(i)
            player_bullet_array.pop(i)
            break
    
    #collsion system for player spaceship and opponent bullet
    for i in range ( 0 , len(opponent_bullet_rect_array) , 1):
        if opponent_bullet_rect_array[i].colliderect(player_spaceship_rect):
            player_hits = player_hits - 1
            opponent_bullet_rect_array.pop(i)
            break

    #player spaceship movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:            
            player_position_y = player_position_y + 10
            player_spaceship_rect.midleft = (player_position_x,player_position_y)
        elif event.key == pygame.K_UP:
            player_position_y = player_position_y - 10         
            player_spaceship_rect.midleft = (player_position_x,player_position_y)
    
    #bullet movement
    if ( blegh % 6 == 0 ):
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_RIGHT:
                t_array = []
                t2_array = [0,0,25,8]
                for i in range ( 0 , 2 , 1):
                    # 2 for appending both x and y coordinates and then appending the whole t_array as a whole 
                    # which contains the coordinates
                    player_bullet_rect.midleft = (player_position_x + 50, player_position_y) #nochange
                    t_array.append(player_bullet_rect.midleft[i])   #nochange
                player_bullet_array.append(t_array) #nochange

                #appending bullet rect to bullet rect array
                t2_array[0] = player_position_x + 50
                t2_array[1] = player_position_y
                player_bullet_rect_array.append(pygame.Rect(t2_array[0],t2_array[1],25,8))
                

    blegh = blegh + 1       

    #opponent spaceship movement
    if (opponent_movement == 0):
        opponent_position_y = opponent_position_y + 15
        opponent_spaceship_rect.midright = (opponent_position_x,opponent_position_y)
    elif (opponent_movement == 1):
        opponent_position_y = opponent_position_y - 15
        opponent_spaceship_rect.midright = (opponent_position_x,opponent_position_y)
    if ( opponent_spaceship_rect.bottom == 604):
        opponent_movement = 1
    if ( opponent_spaceship_rect.top == 11 ):
        opponent_movement = 0

    #opponent bullet movement
    if (blegh % 5 == 0):  # Every 6 frames, the opponent fires
    # Fire from the middle or edge of the opponent spaceship
        tx = opponent_spaceship_rect.midleft[0]
        ty = opponent_spaceship_rect.midleft[1]
        opponent_bullet_rect_array.append(pygame.Rect(tx, ty, opponent_bullet_rect.width, opponent_bullet_rect.height))

  
    #this deals with adding bullet speed to opponent bullet
    for i in range (len(opponent_bullet_rect_array)):
        t_array = opponent_bullet_rect_array[i].x
        t_array = t_array - opponent_bullet_speed
        opponent_bullet_rect_array[i].x = t_array
    
    

    #if opponent bullet out of screen, pops it
    for i in range(len(opponent_bullet_rect_array) - 1, -1, -1):  # Iterate backwards to safely remove bullets
        opponent_bullet_rect_array[i].x -= opponent_bullet_speed
        if opponent_bullet_rect_array[i].x < 0:
            opponent_bullet_rect_array.pop(i)  # Remove bullets that have gone off-screen

    screen.fill((0,0,0))
    screen.blit(player_spaceship, player_spaceship_rect)
    screen.blit(opponent_spaceship, opponent_spaceship_rect)

    for i in range(len(opponent_bullet_rect_array)):
        screen.blit(opponent_bullet, (opponent_bullet_rect_array[i].x , opponent_bullet_rect_array[i].y , 
                                    opponent_bullet_rect_array[i].width , opponent_bullet_rect_array[i].height))


    if ( len(player_bullet_array) != 0 ):
        for i in range ( 0 , len(player_bullet_array) , 1):
            screen.blit(player_bullet, player_bullet_array[i])
   

    
    
    pygame.display.update() 

    clock.tick(20)
    
  
