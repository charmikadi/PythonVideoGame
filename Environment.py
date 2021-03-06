# Import modules 
import pygame, random, math, sys

# Intialize pygame
from pygame.locals import *
pygame.init()
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)

# Constants for colours
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (17, 172, 250)
GREEN = (2, 219, 60)
GREY = (192, 196, 204)
TAN = (250,231,218)
PURPLE = (240, 127, 250)
PALEPURPLE = (255, 217, 253)
VIOLET = (47, 35, 176)
LIGHTBLUE = (227, 250, 255)
LIGHTGREEN = (217, 255, 229)
PINEG = (61, 168, 25)
FOREST = (9, 71, 31)
BROWN = (125, 58, 22)
RED = (255, 0, 0)
DARKG = (0, 148, 40)

# Blue colours
COLOUR1 = (50, 109, 168)
COLOUR2 = (50, 131, 168)
COLOUR3 = (50, 146, 168)
COLOUR4 = (50, 162, 168)
COLOUR5 = (80, 217, 210)
COLOUR6 = (111, 232, 226)
COLOUR7 = (165, 232, 242)
COLOUR8 = (184, 249, 255)

# Orange colours
ORANGE = (255, 123, 66)
MEDIUMORANGE = (255, 138, 66)
LIGHTORANGE = (255, 157, 66)
BRIGHTORANGE = (255, 170, 66)
MUSTARD = (255, 183, 66)
PALEYELLOW = (255, 201, 66)
LIGHTYELLOW = (255, 220, 66)
PALE = (255, 232, 117)
LIGHTERORANGE = (255, 243, 189)

# Green colours
DARKGREEN = (54, 128, 58)
MEDIUMGREEN = (59, 148, 64)
LIGHTERGREEN = (66, 173, 72)
BRIGHTGREEN = (71, 201, 78)
NEONGREEN = (70, 219, 78)
PALEGREEN = (74, 237, 82)
LIGHT = (87, 255, 126)
THINGREEN = (135, 255, 163)

# Starting game screen
global click 
click = False

# Intialize a font
font = pygame.font.SysFont("Times New Roman", 45)

# Function for displaying text on menu screen 
def draw_text(text, font, colour, x, y):
    text_object = font.render(text, 30, colour)
    text_box = text_object.get_rect(center=(x, y))
    screen.blit(text_object, text_box)
         
def main_menu():
    global click     
    while True:
        screen.fill(LIGHTBLUE)
      
        # Background sky in different shades of blue
        pygame.draw.rect(screen, COLOUR1, pygame.Rect(0, 0, 800, 100))
        pygame.draw.rect(screen, COLOUR2, pygame.Rect(0, 50, 800, 100))
        pygame.draw.rect(screen, COLOUR3, pygame.Rect(0, 100, 800, 100))
        pygame.draw.rect(screen, COLOUR4, pygame.Rect(0, 150, 800, 100))
        pygame.draw.rect(screen, COLOUR5, pygame.Rect(0, 200, 800, 100))
        pygame.draw.rect(screen, COLOUR6, pygame.Rect(0, 250, 800, 100))
        pygame.draw.rect(screen, COLOUR7, pygame.Rect(0, 300, 800, 100))
        pygame.draw.rect(screen, COLOUR8, pygame.Rect(0, 400, 800, 100))             
      
        # Background Grass    
        pygame.draw.rect(screen, DARKG, pygame.Rect(0, 350, 800, 200))
        pygame.draw.rect(screen, GREEN, pygame.Rect(0, 420, 800, 200)) 
        
        # Randomized position of clouds 
        randpos = (random.randint(525,650), 160, 140, 35)
        pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos))
        
        randpos2 = (random.randint(0,140), 25, 120, 45)
        pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos2))
        
        randpos3 = (random.randint(120,190), 120, 100, 30)
        pygame.draw.ellipse(screen, GREY, pygame.Rect(randpos3))
        
        # Background flowers function with parameters
        def drawFlower(screen, x, y):
            pygame.draw.circle(screen, VIOLET, (170+x,90+y), 15)
            pygame.draw.circle(screen, VIOLET, (130+x,90+y), 15)
            pygame.draw.circle(screen, VIOLET, (150+x,70+y), 15)
            pygame.draw.circle(screen, VIOLET, (150+x,110+y),15)
            pygame.draw.circle(screen, YELLOW, (150+x,90+y), 10)
        
        drawFlower(screen, 300, 450)
        drawFlower(screen, 100, 450)
        drawFlower(screen, 500, 450)
        
        
        # Larger trees
        pygame.draw.rect(screen, BROWN, (615, 325, 20, 70))
        pygame.draw.polygon(screen, PINEG, [[670, 335], [625, 265], [580, 335]])
        pygame.draw.polygon(screen, PINEG, [[660, 295], [625, 215], [590, 295]])      
        
        pygame.draw.rect(screen, BROWN, (175, 335, 20, 70))
        pygame.draw.polygon(screen, FOREST, [[230, 345], [185, 275], [140, 345]])
        pygame.draw.polygon(screen, FOREST, [[220, 305], [185, 225], [150, 305]])        
  
          
        # Function for trees 
        def drawTree(screen, x):
            pygame.draw.rect(screen, BROWN, (45+x, 350, 15, 50))
            pygame.draw.polygon(screen, GREEN, [[75+x, 370], [50+x, 320], [25+x, 370]])
            pygame.draw.polygon(screen, GREEN, [[70+x, 340], [50+x, 300], [30+x, 340]]) 
            
        drawTree(screen, -50)       
        drawTree(screen, 30)
        drawTree(screen, 110)
        drawTree(screen, 190)
        drawTree(screen, 270)
        drawTree(screen, 350)
        drawTree(screen, 430)
        drawTree(screen, 510)
        drawTree(screen, 590)
        drawTree(screen, 670)
        drawTree(screen, 750)         
            
      
        # Random Colour Generator for flowers    
        rand_colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        def drawColour(screen, x, y):
            pygame.draw.circle(screen, rand_colour, (110+x,410+y), 15)
            pygame.draw.circle(screen, rand_colour, (90+x,410+y), 15)
            pygame.draw.circle(screen, rand_colour, (100+x,400+y), 15)
            pygame.draw.circle(screen, rand_colour, (100+x,420+y),15)
            pygame.draw.circle(screen, YELLOW, (100+x,410+y), 10)
           
        drawColour(screen, -50, 45)
        drawColour(screen, 50, 45)
        drawColour(screen, 150, 45)
        drawColour(screen, 250, 45)
        drawColour(screen, 350, 45)
        drawColour(screen, 450, 45)
        drawColour(screen, 550, 45)
        drawColour(screen, 650, 45)
        
        # User mouse input
        mx, my = pygame.mouse.get_pos()
        
        # Purple star to indicate user's mouse cursor  
        pygame.draw.line(screen, PURPLE, (mx - 20, my), (mx + 20, my))
        pygame.draw.line(screen, PURPLE, (mx, my - 20), (mx, my + 20))
                
        # Buttons for instructions and playing game
        button_teach = pygame.Rect(30, 100, 345, 50)
        button_play = pygame.Rect(100, 200, 140, 50)
        
        if button_teach.collidepoint((mx, my)):
            if not click:
                instructions()
        if button_play.collidepoint((mx, my)):
            if not click:
                playing_game()
                
        pygame.draw.rect(screen, BLUE, button_teach)
        pygame.draw.rect(screen, BLUE, button_play)    
        
        draw_text('SPEED SORT', font, WHITE, 400, 50)
        draw_text('INSTRUCTIONS', font, BLACK, 200, 125)
        draw_text('PLAY', font, BLACK, 170, 225)        
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        
        pygame.display.flip()
        pygame.time.wait(500) 

def playing_game():
    global click 
    click = False
    while True:
        #click = False
        screen.fill(PALEPURPLE) 
        
        # User mouse input
        mx, my = pygame.mouse.get_pos()
        
        # Button for easy level 
        button_easy = pygame.Rect(30, 100, 345, 50)
        pygame.draw.rect(screen, BLUE, button_easy)
        draw_text('EASY', font, WHITE, 200, 125)
        
        # Button for medium level         
        button_medium = pygame.Rect(170, 300, 345, 50)
        pygame.draw.rect(screen, BLUE, button_medium)  
        draw_text('MEDIUM', font, WHITE, 350, 325)                                
        
        # Button for hard level  
        button_hard = pygame.Rect(310, 500, 345, 50)
        pygame.draw.rect(screen, BLUE, button_hard)  
        draw_text('HARD', font, WHITE, 515, 525)           
        
        if button_easy.collidepoint((mx, my)):
            if not click:
                easy_Level()
        if button_medium.collidepoint((mx, my)):
            if not click:
                medium_Level()    
        if button_hard.collidepoint((mx, my)):
            if not click:
                hard_Level()              
                            
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.flip()
        pygame.time.wait(500)     
 
# Function for easy level with one type of waste
def easy_Level():
        global arrow_position
        # Basic Player image
        playerImg = pygame.image.load('Kadiplayer.png')
        playerX = 370
        playerX_variable = 0
        playerY = 460
        
        # Incoming plastic water bottles at player
        num_of_bottles = 4
        bottleImg = []
        bottleX = []
        bottleX_variable = []
        bottleY = []
        bottleY_variable = []
        
        # The moving bottles' position
        for i in range(num_of_bottles):
            bottleImg.append(pygame.image.load('Kadibottle.png'))
            bottleX.append(random.randint(0, 736))
            bottleY.append(random.randint(50, 150))
            bottleX_variable.append(4)
            bottleY_variable.append(10)
            
        # Shooting out arrow at the plastic water bottles by user 
        arrowImg = pygame.image.load('Kadiarrow.png')
        arrowX = 0
        arrowY = 460
        arrowX_variable = 0
        arrowY_variable = 10
        arrow_position = "Start"
        
        # Player score 
        score_value = 0
        font = pygame.font.SysFont('Times New Roman', 75)
        finished_game_font = pygame.font.SysFont('Times New Roman', 40)
        
        # The displayed font coordindates 
        fontX = 15
        fontY = 15
        
        # Defining the functions for images of water bottles, arrow and displaying player's score
        def display_score(x,y):
            value = font.render("Your Score: "+ str(score_value), True, BLACK)
            screen.blit(value, (x, y))
        
        def player(x, y):
            screen.blit(playerImg, (x, y))
        
        def bottle(x, y, i):
            screen.blit(bottleImg[i], (x, y))
        
        def shoot_arrow(x, y):
            global arrow_position
            arrow_position = "Shoot"
            screen.blit(arrowImg, (x + 15, y + 8))
            
        def game_over_message():
            game_over_message = finished_game_font.render("SPEED SORT GAME OVER. GOOD TRY!", True, BLACK)
            screen.blit(game_over_message, (50, 300))
            
        # Determining collision between water bottles and arrow using distance formula
        def collision(bottleX, bottleY, arrowX, arrowY):
            length = ((bottleX - arrowX)**2 + (bottleY - arrowY)**2)**0.5
            if length < 30:
                return True
            else:
                return False        
        
        # Game loop
        running = True
        while running:
            screen.fill(LIGHTERORANGE)          
        
            # Background sky in different shades of orange
            pygame.draw.rect(screen, ORANGE, pygame.Rect(0, 0, 800, 100))
            pygame.draw.rect(screen, MEDIUMORANGE, pygame.Rect(0, 50, 800, 100))
            pygame.draw.rect(screen, LIGHTORANGE, pygame.Rect(0, 100, 800, 100))
            pygame.draw.rect(screen, BRIGHTORANGE, pygame.Rect(0, 150, 800, 100))
            pygame.draw.rect(screen, MUSTARD, pygame.Rect(0, 200, 800, 100))
            pygame.draw.rect(screen, PALEYELLOW, pygame.Rect(0, 250, 800, 100))
            pygame.draw.rect(screen, LIGHTYELLOW, pygame.Rect(0, 300, 800, 100))
            pygame.draw.rect(screen, PALE, pygame.Rect(0, 400, 800, 100))  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
                # Keyboard input from player
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_variable = -4
                    if event.key == pygame.K_RIGHT:
                        playerX_variable = 4  
                    if event.key == pygame.K_SPACE:
                        if arrow_position == "Start":
                            arrowX = playerX
                            shoot_arrow(arrowX, arrowY)
            
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_variable = 0
            
            playerX += playerX_variable
            if playerX <= 0:
                playerX = 0
           
            elif playerX >= 730:
                playerX = 730
                    
            # Motion of the plastic water bottles 
            for i in range(num_of_bottles):   
                if bottleY[i] > 440:
                    for j in range(num_of_bottles):
                        bottleY[j] = 2000
                    game_over_message()
                    break
                    
                bottleX[i] += bottleX_variable[i]
                if bottleX[i] <= 0:
                    bottleX_variable[i] = 4
                    bottleY[i] += bottleY_variable[i]
                           
                elif bottleX[i] >= 750:
                    bottleX_variable[i] = -4
                    bottleY[i] += bottleY_variable[i]    
                            
                # Collision between arrow and incoming plastic water bottles
                collision_site = collision(bottleX[i], bottleY[i], arrowX, arrowY)        
                
                if collision_site:
                    arrowY = 480
                    arrow_position = "Start"
                    score_value += 1
                    bottleX[i] = random.randint(0, 736)
                    bottleY[i] = random.randint(50, 150)
        
                bottle(bottleX[i], bottleY[i], i)
                
            # Movement of the shooting arrow
            if arrowY <= 0:
                arrowY = 460
                arrow_position = "Start"
            
            if arrow_position == "Shoot":
                arrowY -= arrowY_variable
                shoot_arrow (arrowX, arrowY)   
        
            player(playerX, playerY)
            display_score(fontX, fontY)
            pygame.display.update()   
            
            click = False
 
 
 # Function for medium level with 2 types of waste
def medium_Level():
    global arrow_position 
    global arrow2_position 
    
    # Basic Player image
    playerImg = pygame.image.load('Kadiplayer.png')
    playerX = 370
    playerX_variable = 0
    playerY = 460
    
    # Incoming plastic water bottles at player
    num_of_bottles = 4
    bottleImg = []
    bottleX = []
    bottleX_variable = []
    bottleY = []
    bottleY_variable = []
    
    # Incoming compost at player
    num_of_compost = 4
    compostImg = []
    compostX = []
    compostX_variable = []
    compostY = []
    compostY_variable = []
    
    # The moving bottles' position
    for i in range(num_of_bottles):
        bottleImg.append(pygame.image.load('Kadibottle.png'))
        bottleX.append(random.randint(0, 736))
        bottleY.append(random.randint(50, 150))
        bottleX_variable.append(4)
        bottleY_variable.append(10)
        
    # The moving compost's position
    for i in range(num_of_compost):
        compostImg.append(pygame.image.load('Kadicompost.png'))
        compostX.append(random.randint(0, 736))
        compostY.append(random.randint(50, 150))
        compostX_variable.append(4)
        compostY_variable.append(10)
    
    # Shooting out recyle arrow at the plastic water bottles by user 
    arrowImg = pygame.image.load('Kadiarrow.png')
    arrowX = 0
    arrowY = 460
    arrowX_variable = 0
    arrowY_variable = 10
    arrow_position = "Start"
    
    # Shooting out compost arrow at the apples by user 
    arrow2Img = pygame.image.load('Kadiarrow2.png')
    arrow2X = 0
    arrow2Y = 460
    arrow2X_variable = 0
    arrow2Y_variable = 10
    arrow2_position = "Start"
    
    # Player score 
    score_value = 0
    font = pygame.font.SysFont('Times New Roman', 75)
    finished_game_font = pygame.font.SysFont('Times New Roman', 40)    
    
    # The displayed font coordindates 
    fontX = 15
    fontY = 15
    
    # Defining the functions for images of water bottles, arrow and displaying player's score
    def display_score(x,y):
        value = font.render("Your Score: "+ str(score_value), True, WHITE)
        screen.blit(value, (x, y))
    
    def player(x, y):
        screen.blit(playerImg, (x, y))
    
    def bottle(x, y, i):
        screen.blit(bottleImg[i], (x, y))
    
    def compost(x, y, i):
        screen.blit(compostImg[i], (x, y))
    
    def shoot_arrow(x, y):
        global arrow_position
        arrow_position = "Shoot"
        screen.blit(arrowImg, (x + 15, y + 8))
    
    def shoot_arrow_two(x, y):
        global arrow2_position
        arrow2_position = "Shoot"
        screen.blit(arrow2Img, (x + 15, y + 8))
        
    def game_over_message():
        game_over_message = finished_game_font.render("SPEED SORT GAME OVER. GOOD TRY!", True, BLACK)
        screen.blit(game_over_message, (50, 300))    
        
    # Determining collision between water bottles and arrow using distance formula
    def collision(bottleX, bottleY, arrowX, arrowY):
        length = ((bottleX - arrowX)**2 + (bottleY - arrowY)**2)**0.5
        if length < 25:
            return True
        else:
            return False
    
    # Determining collision between compost  and arrow using distance formula
    def collisionTwo(compostX, compostY, arrow2X, arrow2Y):
        distance = ((compostX - arrow2X)**2 + (compostY - arrow2Y)**2)**0.5
        if distance < 25:
            return True
        else:
            return False
    
    # The main game loop 
    running = True
    while running:
        screen.fill((LIGHTBLUE))
        
        # Background sky in different shades of blue
        pygame.draw.rect(screen, COLOUR1, pygame.Rect(0, 0, 800, 100))
        pygame.draw.rect(screen, COLOUR2, pygame.Rect(0, 50, 800, 100))
        pygame.draw.rect(screen, COLOUR3, pygame.Rect(0, 100, 800, 100))
        pygame.draw.rect(screen, COLOUR4, pygame.Rect(0, 150, 800, 100))
        pygame.draw.rect(screen, COLOUR5, pygame.Rect(0, 200, 800, 100))
        pygame.draw.rect(screen, COLOUR6, pygame.Rect(0, 250, 800, 100))
        pygame.draw.rect(screen, COLOUR7, pygame.Rect(0, 300, 800, 100))
        pygame.draw.rect(screen, COLOUR8, pygame.Rect(0, 400, 800, 100))       
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            # Keyboard input from player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_variable = -4
                if event.key == pygame.K_RIGHT:
                    playerX_variable = 4  
                if event.key == pygame.K_SPACE:
                    if arrow_position == "Start":
                        arrowX = playerX
                        shoot_arrow(arrowX, arrowY)
                if event.key == pygame.K_EQUALS:
                    if arrow2_position == "Start":
                        arrow2X = playerX
                        shoot_arrow_two(arrow2X, arrow2Y)                
                
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_variable = 0
        
        playerX += playerX_variable
        if playerX <= 0:
            playerX = 0
       
        elif playerX >= 730:
            playerX = 730
                
        # Motion of the plastic water bottles 
        for i in range(num_of_bottles):   
            if bottleY[i] > 440:
                for j in range(num_of_bottles):
                    bottleY[j] = 2000
                game_over_message()
                break
                
            bottleX[i] += bottleX_variable[i]
            if bottleX[i] <= 0:
                bottleX_variable[i] = 4
                bottleY[i] += bottleY_variable[i]
                       
            elif bottleX[i] >= 730:
                bottleX_variable[i] = -4
                bottleY[i] += bottleY_variable[i]
        
        # Motion of the compost
        for i in range(num_of_compost):   
            if compostY[i] > 440:
                for j in range(num_of_compost):
                    compostY[j] = 2000
                game_over_message()
                break
            
            compostX[i] += compostX_variable[i]
            if compostX[i] <= 0:
                compostX_variable[i] = 4
                compostY[i] += compostY_variable[i]
                       
            elif compostX[i] >= 730:
                compostX_variable[i] = -4
                compostY[i] += compostY_variable[i]        
                        
            # Collision between arrow and incoming plastic water bottles
            collision_site = collision(bottleX[i], bottleY[i], arrowX, arrowY)        
            
            if collision_site:
                arrowY = 480
                arrow_position = "Start"
                score_value += 1
                bottleX[i] = random.randint(0, 736)
                bottleY[i] = random.randint(50, 150)
    
            bottle(bottleX[i], bottleY[i], i)
            
            # Collision between arrow and compost
            collision_site_two = collisionTwo(compostX[i], compostY[i], arrow2X, arrow2Y)        
            
            if collision_site_two:
                arrow2Y = 480
                arrow2_position = "Start"
                score_value += 1
                compostX[i] = random.randint(0, 736)
                compostY[i] = random.randint(50, 150)
    
            compost(compostX[i], compostY[i], i)        
            
        # Movement of the shooting arrow
        if arrowY <= 0:
            arrowY = 460
            arrow_position = "Start"
        
        if arrow_position == "Shoot":
            arrowY -= arrowY_variable
            shoot_arrow (arrowX, arrowY)   
        
        # Movement of the shooting compost arrow 2
        if arrow2Y <= 0:
            arrow2Y = 460
            arrow2_position = "Start"
        
        if arrow2_position == "Shoot":
            arrow2Y -= arrow2Y_variable
            shoot_arrow_two (arrow2X, arrow2Y)   
     
    
        player(playerX, playerY)
        display_score(fontX, fontY)
        pygame.display.flip()       
    
# Function for hard level 
def hard_Level():
    global arrow_position 
    global arrow2_position 
    global arrow3_position
    
    # Basic Player image
    playerImg = pygame.image.load('Kadiplayer.png')
    playerX = 370
    playerX_variable = 0
    playerY = 460
    
    # Incoming plastic water bottles at player
    num_of_bottles = 3
    bottleImg = []
    bottleX = []
    bottleX_variable = []
    bottleY = []
    bottleY_variable = []
    
    # Incoming compost at player
    num_of_compost = 3
    compostImg = []
    compostX = []
    compostX_variable = []
    compostY = []
    compostY_variable = []
    
    # Incoming e-waste at player
    num_of_computer = 3
    computerImg = []
    computerX = []
    computerX_variable = []
    computerY = []
    computerY_variable = []
    
    # The moving bottles' position
    for i in range(num_of_bottles):
        bottleImg.append(pygame.image.load('Kadibottle.png'))
        bottleX.append(random.randint(0, 736))
        bottleY.append(random.randint(50, 150))
        bottleX_variable.append(4)
        bottleY_variable.append(10)
        
    # The moving compost's position
    for i in range(num_of_compost):
        compostImg.append(pygame.image.load('Kadicompost.png'))
        compostX.append(random.randint(0, 736))
        compostY.append(random.randint(50, 150))
        compostX_variable.append(4)
        compostY_variable.append(10)
    
    # The moving e-waste's position
    for i in range(num_of_computer):
        computerImg.append(pygame.image.load('Kadicomputer.png'))
        computerX.append(random.randint(0, 736))
        computerY.append(random.randint(50, 150))
        computerX_variable.append(4)
        computerY_variable.append(10)
    
    # Shooting out recyle arrow at the plastic water bottles by user 
    arrowImg = pygame.image.load('Kadiarrow.png')
    arrowX = 0
    arrowY = 460
    arrowX_variable = 0
    arrowY_variable = 10
    arrow_position = "Start"
    
    # Shooting out compost arrow at the apples by user 
    arrow2Img = pygame.image.load('Kadiarrow2.png')
    arrow2X = 0
    arrow2Y = 460
    arrow2X_variable = 0
    arrow2Y_variable = 10
    arrow2_position = "Start"
    
    # Shooting out e-waste arrow at the computers by user 
    arrow3Img = pygame.image.load('Kadiarrow3.png')
    arrow3X = 0
    arrow3Y = 460
    arrow3X_variable = 0
    arrow3Y_variable = 10
    arrow3_position = "Start"
    
    # Player score 
    score_value = 0
    font = pygame.font.SysFont('Times New Roman', 75)
    finished_game_font = pygame.font.SysFont('Times New Roman', 40)    
    
    # The displayed font coordindates 
    fontX = 15
    fontY = 15
    
    # Defining the functions for images of water bottles, arrow and displaying player's score
    def display_score(x,y):
        value = font.render("Your Score: "+ str(score_value), True, PURPLE)
        screen.blit(value, (x, y))
    
    def player(x, y):
        screen.blit(playerImg, (x, y))
    
    def bottle(x, y, i):
        screen.blit(bottleImg[i], (x, y))
    
    def compost(x, y, i):
        screen.blit(compostImg[i], (x, y))
        
    def computer(x, y, i):
        screen.blit(computerImg[i], (x, y))    
    
    def shoot_arrow(x, y):
        global arrow_position
        arrow_position = "Shoot"
        screen.blit(arrowImg, (x + 15, y + 8))
    
    def shoot_arrow_two(x, y):
        global arrow2_position
        arrow2_position = "Shoot"
        screen.blit(arrow2Img, (x + 15, y + 8))
    
    def shoot_arrow_three(x, y):
        global arrow3_position
        arrow3_position = "Shoot"
        screen.blit(arrow3Img, (x + 15, y + 8))
        
    def game_over_message():
        game_over_message = finished_game_font.render("SPEED SORT GAME OVER. GOOD TRY!", True, BLACK)
        screen.blit(game_over_message, (50, 300))        
        
    # Determining collision between water bottles and arrow using distance formula
    def collision(bottleX, bottleY, arrowX, arrowY):
        length = ((bottleX - arrowX)**2 + (bottleY - arrowY)**2)**0.5
        if length < 25:
            return True
        else:
            return False
    
    # Determining collision between compost  and arrow using distance formula
    def collisionTwo(compostX, compostY, arrow2X, arrow2Y):
        distance = ((compostX - arrow2X)**2 + (compostY - arrow2Y)**2)**0.5
        if distance < 25:
            return True
        else:
            return False
    
    # Determining collision between computers and arrow 3 using distance formula
    def collisionThree(computerX, computerY, arrow3X, arrow3Y):
        span = ((computerX - arrow3X)**2 + (computerY - arrow3Y)**2)**0.5
        if span < 25:
            return True
        else:
            return False
        
    # The main game loop 
    running = True
    while running:
        screen.fill((LIGHTGREEN))
        
        # Background in different shades of green
        pygame.draw.rect(screen, DARKGREEN, pygame.Rect(0, 0, 800, 100))
        pygame.draw.rect(screen, MEDIUMGREEN, pygame.Rect(0, 50, 800, 100))
        pygame.draw.rect(screen, LIGHTERGREEN, pygame.Rect(0, 100, 800, 100))
        pygame.draw.rect(screen, BRIGHTGREEN, pygame.Rect(0, 150, 800, 100))
        pygame.draw.rect(screen, NEONGREEN, pygame.Rect(0, 200, 800, 100))
        pygame.draw.rect(screen, PALEGREEN, pygame.Rect(0, 250, 800, 100))
        pygame.draw.rect(screen, LIGHT, pygame.Rect(0, 300, 800, 100))
        pygame.draw.rect(screen, THINGREEN, pygame.Rect(0, 400, 800, 100))       
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            # Keyboard input from player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_variable = -4
                if event.key == pygame.K_RIGHT:
                    playerX_variable = 4  
                if event.key == pygame.K_SPACE:
                    if arrow_position == "Start":
                        arrowX = playerX
                        shoot_arrow(arrowX, arrowY)
                if event.key == pygame.K_EQUALS:
                    if arrow2_position == "Start":
                        arrow2X = playerX
                        shoot_arrow_two(arrow2X, arrow2Y)   
                if event.key == pygame.K_COMMA:
                    if arrow3_position == "Start":
                        arrow3X = playerX
                        shoot_arrow_three(arrow3X, arrow3Y)                         
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_variable = 0
        
        playerX += playerX_variable
        if playerX <= 0:
            playerX = 0
       
        elif playerX >= 730:
            playerX = 730
                
        # Motion of the plastic water bottles 
        for i in range(num_of_bottles):   
            if bottleY[i] > 440:
                for j in range(num_of_bottles):
                    bottleY[j] = 2000
                break
            bottleX[i] += bottleX_variable[i]
            if bottleX[i] <= 0:
                bottleX_variable[i] = 4
                bottleY[i] += bottleY_variable[i]
                       
            elif bottleX[i] >= 730:
                bottleX_variable[i] = -4
                bottleY[i] += bottleY_variable[i]
        
        # Motion of the compost
        for i in range(num_of_compost):   
            if compostY[i] > 440:
                for j in range(num_of_compost):
                    compostY[j] = 2000
                game_over_message()
                break
            compostX[i] += compostX_variable[i]
            if compostX[i] <= 0:
                compostX_variable[i] = 4
                compostY[i] += compostY_variable[i]
                       
            elif compostX[i] >= 730:
                compostX_variable[i] = -4
                compostY[i] += compostY_variable[i]    
                
        # Motion of the computers
        for i in range(num_of_computer):   
            if computerY[i] > 440:
                for j in range(num_of_computer):
                    computerY[j] = 2000
                game_over_message()
                break
            computerX[i] += computerX_variable[i]
            if computerX[i] <= 0:
                computerX_variable[i] = 4
                computerY[i] += computerY_variable[i]
                       
            elif computerX[i] >= 730:
                computerX_variable[i] = -4
                computerY[i] += computerY_variable[i]       
                      
                        
            # Collision between arrow and incoming plastic water bottles
            collision_site = collision(bottleX[i], bottleY[i], arrowX, arrowY)        
            
            if collision_site:
                arrowY = 480
                arrow_position = "Start"
                score_value += 1
                bottleX[i] = random.randint(0, 736)
                bottleY[i] = random.randint(50, 150)
    
            bottle(bottleX[i], bottleY[i], i)
            
            # Collision between arrow and compost
            collision_site_two = collisionTwo(compostX[i], compostY[i], arrow2X, arrow2Y)        
            
            if collision_site_two:
                arrow2Y = 480
                arrow2_position = "Start"
                score_value += 1
                compostX[i] = random.randint(0, 736)
                compostY[i] = random.randint(50, 150)
    
            compost(compostX[i], compostY[i], i)      
            
            # Collision between e-waste arrow 3 and the computers
            collision_site_three = collisionThree(computerX[i], computerY[i], arrow3X, arrow3Y)        
            
            if collision_site_three:
                arrow3Y = 480
                arrow3_position = "Start"
                score_value += 1
                computerX[i] = random.randint(0, 736)
                computerY[i] = random.randint(50, 150)
    
            computer(computerX[i], computerY[i], i)         
            
        # Movement of the shooting arrow
        if arrowY <= 0:
            arrowY = 460
            arrow_position = "Start"
        
        if arrow_position == "Shoot":
            arrowY -= arrowY_variable
            shoot_arrow (arrowX, arrowY)   
        
        # Movement of the shooting compost arrow 2
        if arrow2Y <= 0:
            arrow2Y = 460
            arrow2_position = "Start"
        
        if arrow2_position == "Shoot":
            arrow2Y -= arrow2Y_variable
            shoot_arrow_two (arrow2X, arrow2Y)   
            
        # Movement of the shooting e-waste arrow 3
        if arrow3Y <= 0:
            arrow3Y = 460
            arrow3_position = "Start"
        
        if arrow3_position == "Shoot":
            arrow3Y -= arrow3Y_variable
            shoot_arrow_three (arrow3X, arrow3Y)           
    
    
        player(playerX, playerY)
        display_score(fontX, fontY)
        pygame.display.flip()        
        
def instructions():
    running = True
    while running:
        screen.fill(LIGHTGREEN)
        
        # Functions to display clusters of grass     
        def drawGrass(screen, x, y):
            pygame.draw.line(screen, PINEG, (425+x, 410+y), (430+x, 370+y), 2) 
            pygame.draw.line(screen, PINEG, (420+x, 410+y), (420+x, 370+y), 2) 
            pygame.draw.line(screen, PINEG, (415+x, 410+y), (410+x, 370+y), 2) 
        
        def drawLargeCluster(screen, x, y):
            drawGrass(screen, -395+x, 185+y)
            drawGrass(screen, -365+x, 195+y)
            drawGrass(screen, -335+x, 185+y)
            
        drawLargeCluster(screen, 0, 0)
        drawLargeCluster(screen, 190, 0)
        drawLargeCluster(screen, 380, 0)
        drawLargeCluster(screen, 570, 0)
        
        def drawOtherLargeCluster(screen, x, y):
            drawGrass(screen, -305+x, 195+y)
            drawGrass(screen, -270+x, 185+y)
            drawGrass(screen, -240+x, 195+y)
            
        drawOtherLargeCluster(screen, 0, 0)
        drawOtherLargeCluster(screen, 190, 0)
        drawOtherLargeCluster(screen, 380, 0)
        drawOtherLargeCluster(screen, 570, 0)
        
        def drawSmallCluster(screen, x, y):
                drawGrass(screen, 185+x, 95+y)
                drawGrass(screen, 210+x, 85+y)
                drawGrass(screen, 235+x, 95+y)
                
        drawSmallCluster(screen, -375, -20)
        drawSmallCluster(screen, 0, 20)         
        
        font = pygame.font.SysFont("Times New Roman", 20)
        draw_text('Every day around 8 million pieces of plastic enter into oceans.', font, BROWN, 400, 50)
        draw_text('A single recycled plastic bottle creates 20% less air pollution and 50% less water pollution.', font, BROWN, 400, 80)
        
        font = pygame.font.SysFont("Calibri", 40)     
        draw_text('GAME RULES', font, PURPLE, 400, 130)
        
        font = pygame.font.SysFont("Calibri", 18)
        draw_text('1. To score points you must shoot items using the arrow with correct garbage disposal category.', font, BLACK, 400, 180)        
        draw_text('2. To move the character use the left and right keys on the keyboard.', font, BLACK, 400, 210)
        draw_text('3. To shoot recyclable waste, press the space bar.', font, BLUE, 400, 240)
        draw_text('4. To shoot compostable items, press the equal sign key.', font, GREEN, 400, 270)
        draw_text('5. To shoot e-waste material, press the comma key.', font, RED, 400, 300)
        
   
        font = pygame.font.SysFont("Calibri", 40)     
        draw_text('GAME OBJECTIVES', font, PURPLE, 400, 350)
        
        font = pygame.font.SysFont("Calibri", 16)
        draw_text('Increase your score before all items reach the character at the bottom due to gravity and the game is over.', font, BLACK, 400, 380)
        draw_text('Successfully improve your score in all 3 of the levels.', font, BLACK, 400, 420)
        
  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False      
                    
        pygame.display.flip()
        pygame.time.wait(500)        

                             
main_menu()
pygame.quit()
