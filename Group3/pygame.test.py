import pygame

pygame.init()

screen = pygame.display.set_mode((800,579))
pygame.display.set_caption("4pics 1word")

 
start_img = pygame.image.load('assets/sans.PNG').convert_alpha()
exit_img = pygame.image.load('assets/exit.PNG').convert_alpha()
next_img = pygame.image.load('assets/next.PNG').convert_alpha()


background = pygame.image.load('assets/background.png')
background2 = pygame.image.load('assets/cheetah.png')


#button class
class Button():
    def __init__(self,x,y,image,):
        self.image =  image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        action = False
        #mouse position
        pos = pygame.mouse.get_pos()
        
        #check if button is clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]== 1 and self.clicked == False:
                self.clicked = True
                action = True
                
                
            if pygame.mouse.get_pressed()[0]== 0:
                self.clicked = False
        
        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action
    
 
start_button = Button(10,400,start_img,)
exit_button = Button(500,400,exit_img,)


open = True
while open:
    screen.fill((26,26,26))
    screen.blit(background,(0,0))
    if start_button.draw():
        
        screen = pygame.display.set_mode((800,579))
        pygame.display.set_caption("Level 1")
        next_img = pygame.image.load('assets/next.PNG').convert_alpha()
        background = pygame.image.load('assets/background2.png')
        start_button = Button(10,0,next_img,)
        exit_button = Button(500,0,exit_img,)

        #print('START')
    if exit_button.draw():
        open = False
        #print('EXIT')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    pygame.display.update()
pygame.quit()
quit()
