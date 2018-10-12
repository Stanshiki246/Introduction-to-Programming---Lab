# import sprite module from
from pygame.sprite import *
# Make a class of space jet
class Jet(Sprite):
    """initialize the jet"""
    # Define the function to initialize class Jet
    def __init__(self, screen):
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = pygame.image.load("sprites/battlejet.png") # self parameter for loading space jet image
        self.image = pygame.transform.scale(self.image, (90, 50)) # self parameter for scaling image
        self.rect = self.image.get_rect() # self parameter for getting image
        self.rect.x = 10 # self parameter for value of rect.x
        self.rect.y = 50 # self parameter for value of rect.y
        self.screen = screen # self parameter for game screen
        self.move_speed = 6 # self parameter for moving speed
        """bullet"""
        self.firerates = 2 # self parameter for limit of bullets
    # Define the function to move left
    def moveleft(self):
        self.rect.x -= self.move_speed # value of rect.x is subtracted by value of moving speed
        pygame.display.flip() # Show the moving left
    # Define the function to move right
    def moveright(self):
        self.rect.x += self.move_speed # value of rect.x is added by value of moving speed
        pygame.display.flip() # Show the moving right
    # Define the function to move up
    def moveup(self):
        self.rect.y -= self.move_speed # value of rect.y is subtracted by value of moving speed
        pygame.display.flip() # Show the moving up
    # Define the function to move down
    def movedown(self):
        self.rect.y += self.move_speed # value of rect.y is added by value of moving speed
        pygame.display.flip() # Show the moving down
# Make a class function of star background
class Star_bg:
    # Define a function to initialize class star_bg
    def __init__(self,background):
        self.background=pygame.image.load(background) # self parameter for loading star background image
        self.background=pygame.transform.scale(self.background,(800,600)) # self parameter for scaling background image
        self.background_size=self.background.get_size() # self parameter for getting the size of background image
        self.background_rect=self.background.get_rect() # self parameter for getting the coordinates of  background image
        self.width,self.height=self.background_size # self parameter for height and width of background image
    # Define a function to draw background image
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y)) # Draw star as background image

# Make a class function of bullets
class Bullet(Sprite):
    # Define a function to initialize class Bullet
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx # self parameter for starting x point
        self.starty = starty # self parameter for starting y point
        self.speedx = 20 # self parameter for speed
        self.image = pygame.image.load("sprites/bullets.png") # self parameter for loading bullet image
        self.image = pygame.transform.scale(self.image,(40,40)) # self parameter for scaling bullet image
        self.rect=self.image.get_rect() # self parameter for getting coordinates of bullet image
        self.rect.left = startx # self parameter for getting x coordinate of bullet image
        self.rect.top = starty # self parameter for getting y coordinates of bullet image
        self.rect.center = (startx,starty) # self parameter for getting center coordinates of bullet image
        self.screen = screen # self parameter for game screen
    # Define a function to move bullet
    def movement(self):
        self.screen.blit(self.image,[self.startx,self.starty]) # Self parameter for drawing bullet
        self.rect.left += self.speedx # value of x coordinate is subtracted by value of speed
# Make a class function of asteroid
class Asteroid(Sprite):
    # Define a function to initialize class Asteroid
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx # self parameter for starting x point
        self.starty = starty # self parameter for starting y point
        self.speedx = speedx # self parameter for speed
        self.image = pygame.image.load("sprites\meteor.png") # self parameter for loading asteroid image
        self.image = pygame.transform.scale(self.image, (width, height)) # self parameter for scaling asteroid image
        self.rect = self.image.get_rect() # self parameter for getting coordinates of asteroid image
        self.rect.left = startx # self parameter for getting x coordinate of asteroid image
        self.rect.top = starty # self parameter for getting y coordinate of asteroid image
        self.screen = screen # self parameter for game screen
    # Define a function to move asteroid
    def movement(self):
        """method to move the Asteoid"""
        self.rect.left -= self.speedx # value of x coordinate is subtracted by value of speed
# Make a class function of button
class Button(Sprite):
    # Define a function to initialize class Button
    def __init__(self,image):
        Sprite. __init__(self)
        self.button = pygame.image.load(image) # self parameter for loading button image
        self.button = pygame.transform.scale(self.button,(300,150)) # self parameter for scaling button image
