# Name: Charmi Kadi
# Date: June. 21, 2021
# Course Code: ICS3U1-01
# Description: Summative environmental themed python game.

# Import modules 
import pygame, random, math

# Constants
SIZE = (800,600)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (17, 172, 250)
GREEN = (2, 219, 60)
GREY = (192, 196, 204)
TAN = (250,231,218)
RED = (255, 0, 0)
PURPLE = (240, 127, 250)
LIGHTBLUE = (227, 250, 255)
YELLOW = (255, 255, 0)


# Opening pygame screen
screen = pygame.display.set_mode(SIZE)

running = True
while running:
    screen.fill((BLUE))    
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
    
    # Drawing a star
    coordinates_star = [(165, 151), (200, 25), (235, 151), (371, 144), (257, 219), (306, 346), (200, 260), (94, 346), (143, 219), (30, 140)]  
    pygame.draw.polygon(screen, YELLOW, coordinates_star)

    # Character's right arm and hand
    pygame.draw.line(screen, TAN, (520, 280), (420, 330), 18)
    pygame.draw.ellipse(screen,TAN, pygame.Rect(510, 265, 20, 30)) # base of hand
    pygame.draw.ellipse(screen,TAN, pygame.Rect(520, 267, 30, 8))
    pygame.draw.ellipse(screen,TAN, pygame.Rect(520, 275, 30, 8))
    pygame.draw.ellipse(screen,TAN, pygame.Rect(520, 283, 30, 8))
    pygame.draw.ellipse(screen,TAN, pygame.Rect(520, 290, 20, 8)) # pinky finger    
    
    # Character's left arm and hand
    pygame.draw.line(screen, TAN, (280, 280), (380, 330), 18)
    pygame.draw.ellipse(screen,TAN, pygame.Rect(265, 260, 20, 30)) # base of hand
    pygame.draw.ellipse(screen,TAN, pygame.Rect(245, 262, 30, 8)) 
    pygame.draw.ellipse(screen,TAN, pygame.Rect(245, 270, 30, 8)) 
    pygame.draw.ellipse(screen,TAN, pygame.Rect(245, 278, 30, 8)) 
    pygame.draw.ellipse(screen,TAN, pygame.Rect(252, 285, 20, 8))  # pinky finger    

    # Character's legs
    pygame.draw.rect(screen, TAN, pygame.Rect(372, 435, 20, 60))
    pygame.draw.rect(screen, TAN, pygame.Rect(412, 435, 20, 60))   
    
    # Character's body
    pygame.draw.ellipse(screen,GREEN, pygame.Rect(352, 250, 100, 160))
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(345, 320, 105, 100))
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(343, 345, 110, 100))
    pygame.draw.ellipse(screen,GREEN, pygame.Rect(352, 299, 91, 70))      
    
    # Buttons
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(370, 380, 10, 25)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(410, 380, 10, 25))    
    
    # Character's face
    pygame.draw.circle(screen, TAN, (400,210), 55)
    
    # Character's mouth
    pygame.draw.arc(screen, RED, (365,178,68,75), 3*math.pi/2, 2*math.pi, 2)
    pygame.draw.arc(screen, RED, (365,178,68,75), math.pi, 3*math.pi/2, 2)    
    
    # Character's nose
    pygame.draw.circle(screen, BLACK, (400, 220), 10)
    
    
    # Character's eyes
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(370, 182, 18, 31)) 
    pygame.draw.ellipse(screen,WHITE, pygame.Rect(410, 182, 18, 31)) 
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(373, 195, 11, 17)) 
    pygame.draw.ellipse(screen,BLACK, pygame.Rect(413, 195, 11, 17))  
        
    # Character's shoes
    pygame.draw.ellipse(screen,PURPLE, pygame.Rect(400, 475, 60, 30))
    pygame.draw.ellipse(screen,PURPLE, pygame.Rect(330, 475, 60, 30))
    
    
    pygame.display.flip()
    pygame.time.wait(500)    
            
pygame.quit()    
