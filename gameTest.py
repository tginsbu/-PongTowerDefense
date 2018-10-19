import pygame
import math
import numpy
import random
pygame.init()
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HEIGHT = 750
WIDTH = 750
CENTERY = int(HEIGHT/2)
CENTERX = int(WIDTH/2)
RADIUS = 300
#Open a new window
size = (HEIGHT, WIDTH)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("middle")
bar = pygame.image.load('bar.bmp')
bar.set_colorkey(BLACK)
ball = pygame.image.load('ball.bmp');



#bar = pygame.transform.rotozoom(bar, 10, 1)
# The loop will carry on until the user exit the game (e. g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

rectangle = pygame.rect.Rect(CENTERX , CENTERY - RADIUS, 10, 10)
ballxv = 1
ballyv = 1
ballx = CENTERX
bally = CENTERY
#--------Main Program Loop --------
while carryOn:
    
    
        
        
    
    
    # --- Main event loop
    for event in pygame.event.get(): #User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
        
        if event.type == pygame.MOUSEMOTION:
            
            
            (x, y) = pygame.mouse.get_pos();
            if(x - CENTERX == 0):
                xBar = CENTERX
                yBar = CENTERY-RADIUS
            else:
                slope = (y - CENTERY)/(x - CENTERX)
                angle = numpy.arctan((y - CENTERY)/(x - CENTERX))
                xBAR = (RADIUS-5) * math.cos(angle) + CENTERX
                yBAR = (RADIUS-5) * math.sin(angle) + CENTERY
            
                if(x  < CENTERX):
            
                    xBAR = -xBAR + 2*CENTERX
                    yBAR = -yBAR + 2*CENTERY
                bar = pygame.image.load("bar.bmp")
                


                bar = rot_center(bar, -(angle*360)/(2*math.pi)+90)
            
    print(math.sqrt((ballx - xBAR)**2 + (bally - xBAR)**2))
    if math.sqrt((ballx - xBAR)**2 + (bally - xBAR)**2) < 20:
                normx = (xBAR - CENTERX)/(math.sqrt((xBAR - CENTERX)**2 + (yBAR - CENTERY)**2))
                normy = (yBAR - CENTERY)/(math.sqrt((xBAR - CENTERX)**2 + (yBAR - CENTERY)**2))
                newvelx = -2 * (ballxv*normx + ballyv * normy) * normx + ballxv + random.randint(0, 1)
                newvely = -2 * (ballxv*normx + ballyv * normy) * normy + ballyv + random.randint(0, 1)
                if math.sqrt((ballx + ballxv - CENTERX)**2 + (bally + ballyv - CENTERY)**2) > RADIUS:
                    newvelx = -2 * (ballxv*normx + ballyv * normy) * normx + ballxv
                    newvely = -2 * (ballxv*normx + ballyv * normy) * normy + ballyv
                ballxv = newvelx
                ballyv = newvely    
    ballx = ballx + ballxv
    bally = bally + ballyv           
            
            
            
    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the sceen to white.
    #screen.fill(WHITE)
    #Then you can draw didfferent shapes and lines or add text to your background
    
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, [CENTERX, CENTERY], RADIUS, 0)
    
    #bar = pygame.transform.rotozoom(bar, 10, 1)
    
    
    finalpos = (xBAR - (bar.get_width())/2, yBAR - (bar.get_height())/2)
    bar.set_colorkey(BLACK)
    bar.convert_alpha()
    ball.set_colorkey(BLACK)
    ball.convert_alpha()
    screen.blit(bar, finalpos)
    screen.blit(ball, (ballx-25, bally-25))
    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
    
