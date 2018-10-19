import pygame
import math
import numpy
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HEIGHT = 750
WIDTH = 750
CENTERY = int(HEIGHT/2)
CENTERX = int(WIDTH/2)
RADIUS = 300
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text, screen, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',12)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x , y)
    screen.blit(TextSurf, TextRect)
    
class ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ball.bmp')
        self.image.set_colorkey(BLACK)
        self.image.convert_alpha()
        self.rect = self.image.get_rect();
        self.rect.x = x
        self.rect.y = y
        self.centerx = x + self.image.get_width()/2
        self.centery = y + self.image.get_height()/2
        self.dir = 270
        self.v = 5
        self.edgeangle = 0
        self.ballangle = 0

 
    def bounce(self, inputAngle):
        
    
        self.dir = (inputAngle + (inputAngle - (self.dir + 180)) + 180) % 360
         #if 1 == 1: #(paddle.x > CENTERX):
         #   if((self.ballangle - inputAngle) > 2):
          #       self.dir = self.dir - math.radians(10)
           # if((self.ballangle - inputAngle) < -2):
            #     self.dir = self.dir + math.radians(10)
        #elif(paddle.x < CENTERX):
         #   if((self.ballangle - inputAngle) < 2):
         #        self.dir = self.dir - math.radians(10)
          #  if((self.ballangle - inputAngle) > -2):
         #        self.dir = self.dir + math.radians(10)
        
        
        self.rect.x = self.rect.x + math.cos(math.radians(self.dir)) *self.v
        self.rect.y = self.rect.y + math.sin(math.radians(self.dir))*self.v
        print(self.dir)
        
    def update(self):
        (x, y) = pygame.mouse.get_pos()
        self.rect.x = self.centerx + math.cos(math.radians(self.dir))*self.v - self.image.get_width()/2
        self.rect.y = self.centery + math.sin(math.radians(self.dir))*self.v - self.image.get_height()/2
        self.centerx = self.rect.x + self.image.get_width()/2
        self.centery = self.rect.y + self.image.get_height()/2
        if math.sqrt((self.rect.x + self.image.get_width()/2  - CENTERX)**2 + ((self.rect.y + self.image.get_height()/2)  - CENTERY)**2) > RADIUS - 5:
            self.centerx = CENTERX
            self.centery = CENTERY
            self.centerx = self.centerx + math.cos(math.radians(self.dir)) *self.v* 3
            self.centery = self.centery + math.sin(math.radians(self.dir))*self.v * 3 
    def checkCollide(self, paddle):
         if(self.centerx - CENTERX == 0):
             if(self.rect.y > CENTERY):
                 ballangle = 180;
             else:
                 ballangle = 0
         else:
             ballangle = numpy.arctan((self.centery - CENTERY)/(self.centerx - CENTERX))
             ballangle = math.degrees(ballangle)
             if(self.rect.x - CENTERX < 0):
                ballangle = ballangle-180
             ballangle = ballangle + 270   
         self.ballangle = ballangle
        
         if math.sqrt((self.centerx  - CENTERX)**2 + (self.centery  - CENTERY)**2) > RADIUS - 10:
             
             if  abs(ballangle - paddle.angle) < 8:
                  self.bounce(paddle.angle)
             if (ballangle < 10 and paddle.angle > 350):
                  self.bounce(abs(paddle.angle - 360))
             if (ballangle > 350 and paddle.angle < 10):
                  self.bounce(abs(paddle.angle - 360))
         if math.sqrt((self.centerx  - CENTERX)**2 + (self.centery  - CENTERY)**2) < RADIUS/20:
             self.bounce(180)
         if(self.rect.x - CENTERX != 0):    
             self.edgeangle = numpy.arctan((self .rect.y - CENTERY)/(self.rect.x - CENTERX))
        
class bar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bar.bmp')
        self.image.set_colorkey(BLACK)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.angle = 90
        self.x = x
        self.y = y
        
    def update(self):
        (x, y) = pygame.mouse.get_pos();
        if(x - CENTERX == 0):
                xBar = CENTERX
                yBar = CENTERY-RADIUS
                angle = 0
        else:
            angle = numpy.arctan((y - CENTERY)/(x - CENTERX))
            xBAR = (RADIUS-5) * math.cos(angle) + CENTERX
            yBAR = (RADIUS-5) * math.sin(angle) + CENTERY
            if(x  < CENTERX):
                xBAR = -xBAR + 2*CENTERX
                yBAR = -yBAR + 2*CENTERY
                
            self.image = pygame.image.load("bar.bmp")
            angle = math.degrees(angle)
            rotateangle = -angle + 90
            self.image = rot_center(self.image, rotateangle)
            self.image.set_colorkey(BLACK)
            self.image.convert_alpha()
            finalpos = (xBAR - (self.image.get_width())/2, yBAR - (self.image.get_height())/2)
    
            self.rect.x = finalpos[0]
            self.rect.y = finalpos[1]
            self.x = x
            self.y = y
            if(x - CENTERX < 0):
                angle = angle-180
            self.angle = angle + 270
            
                
            
    #def checkCollision(self):
        #upperleft = [self.rect.x - self.image.get_width()/2, self.rect.y - self.image.get_height()/2
        #upperright = self.rect.x - 
pygame.init()
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

# The loop will carry on until the user exit the game (e. g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

ball1 = ball(CENTERX, CENTERY)
paddle = bar(CENTERX, CENTERY - RADIUS)
movingsprites = pygame.sprite.Group()
movingsprites.add(ball1)
movingsprites.add(paddle)
balls = pygame.sprite.Group()
balls.add(ball1)
counter = 0;
#--------Main Program Loop --------
while carryOn:
    ball1.update()
    paddle.update() 
    ball1.checkCollide(paddle)
    counter = counter + 1
    #if(counter % 10 == 0):
      #  print(ball1.ballangle)
       # print(paddle.angle)
    
    # --- Main event loop
    for event in pygame.event.get(): #User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
            
            
    
               
    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the sceen to white.
    #screen.fill(WHITE)
    #Then you can draw didfferent shapes and lines or add text to your background
    
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, [CENTERX, CENTERY], RADIUS, 0)
    #pygame.draw.line(screen, RED, [CENTERX, CENTERY],[ball1.centerx, ball1.centery], 2)
    pygame.draw.circle(screen, WHITE, [CENTERX, CENTERY], int(RADIUS/20), 0)
    
    movingsprites.draw(screen)
    message_display(str(ball1.dir) , screen, 100, 50)
    message_display(str(paddle.angle) , screen, 100, 100)
    message_display(str(ball1.ballangle) , screen, 100, 150)
   
    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
    
