import pygame
from sys import exit
from random import randint

def display_score():
    current_time =int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (410,50))
    screen.blit(score_surface,score_rectangle)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= 5
            
            screen.blit(snail_character,obstacle_rectangle)
            
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

pygame.init()
screen = pygame.display.set_mode((820,480)) #-weight and height of the pygame window
title = pygame.display.set_caption("Z-RUNNER") #-changes the title 
icon = pygame.image.load('RunnerPics/Graphics/icon.PNG') #-changes the icon of the pygame window
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font('RunnerPics/Fonts/Pixeltype.ttf',50)
font2 = pygame.font.Font('RunnerPics/Fonts/arcadeclassic/ARCADECLASSIC.TTF',50)
Game_start = False
start_time = 0
score = 0


sky_surface = pygame.image.load('RunnerPics/Graphics/Backgrounds.pics/sky.PNG').convert()
ground_surface = pygame.image.load('RunnerPics/Graphics/Backgrounds.pics/ground.PNG').convert()

#text_surface = font.render('OUR GAME',False,(64,64,64))
#text_rectangle = text_surface.get_rect(center = (410,50))

snail_character = pygame.image.load('RunnerPics\Graphics\Characters\Characters\snail\snail1.png').convert_alpha()
snail_rectangle = snail_character.get_rect(midbottom = (600,391))

obstacle_rectangle_list = []

player_character = pygame.image.load('RunnerPics\Graphics\Characters\Characters\Player\player_walk_1.png').convert_alpha()
player_rectangle = player_character.get_rect(midbottom = (50,391))
player_gravity = 0

#intro screen
player_character2 = pygame.image.load('RunnerPics\Graphics\Characters\Characters\Player\player_stand.png').convert_alpha()
player_character2 = pygame.transform.rotozoom(player_character2,0,2)
player2_rectangle = player_character2.get_rect(center = (410,210))

game_name = font.render('RUNNER 2D BY GROUP 3',False,'White')
game_name_rectangle = game_name.get_rect(center = (410,80))

game_message = font2.render('PRESS SPACE TO RUN',False,'Black')
game_message_rectangle = game_message.get_rect(center = (410,400))

#TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)


while  True:
    for event in pygame.event.get(): #-checking for players input
        if event.type == pygame.QUIT: #-if input is quit , then quit the game window
           pygame.quit()
           exit() #-ends the while loop
        if Game_start:   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 391:
                    player_gravity = -21
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 391:
                    player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Game_start = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacle_timer and Game_start:
             obstacle_rectangle_list.append(snail_character.get_rect(midbottom = (randint(900,1100),391)))
            

    if Game_start:            
        screen.blit(sky_surface,(0,-200))
        screen.blit(ground_surface,(-1,391))
        #pygame.draw.rect(screen,'#c0e8ec',text_rectangle)
       # pygame.draw.rect(screen,'#c0e8ec',text_rectangle,10)
        #screen.blit(text_surface,text_rectangle)
        score = display_score()
        
        
        #ENEMY
        #snail_rectangle.right -= 4
        #if snail_rectangle.right <= 0:
            #snail_rectangle.left = 800
        #screen.blit(snail_character,snail_rectangle)
        
        
        #PLAYER
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 391:
            player_rectangle.bottom = 391
        screen.blit(player_character,player_rectangle)
        
        # obstacle movement
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)
        
    
        
        #check if player collides with the enemy
        if snail_rectangle.colliderect(player_rectangle):
            Game_start = False
    else:
        screen.fill((0,0,139))
        screen.blit(player_character2,player2_rectangle)
        
        score_message = font.render(f'YOUR SCORE:{score}',False,'Black')
        score_message_rectangle = score_message.get_rect(center = (410,400))
        screen.blit(game_name,game_name_rectangle)
        
        if score == 0:
            screen.blit(game_message,game_message_rectangle)
        else:
            screen.blit(score_message,score_message_rectangle)
        
    pygame.display.update() #-updates everything
    clock.tick(60) #-setting game speed to 60fps


