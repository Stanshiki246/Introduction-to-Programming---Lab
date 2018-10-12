import pygame
# Import meteor_shooter_menu module
import meteor_shooter_menu
# Import random module
import random
# Import meteor_shooter_game_function module with variable gf
import meteor_shooter_game_function as gf

# Define a function to run game
def run_game():
    """this is game play interface"""
    screen = pygame.display.set_mode((800, 600)) #Variable for game screen
    pygame.display.set_caption("Asteroid Fighter") #Show title of game

    scores = 0 #Variable for score with starting point at 0
    theClock = pygame.time.Clock() #Variable for pygame time clock
    bg_image = gf.Star_bg("bg\star.gif") #Variable for star.gif background.
    #Variables for coordinating the moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init() #Initialize pygame module

    #creating a jet
    jet1 = gf.Jet(screen)  # Variable for space jet.
    Jet_sprites = gf.Group(jet1) # Variable for space jet sprite
    #create asteroid object group
    asteroid_group = gf.Group() # Variable for group of asteroids
    #create bullets object Group
    bullets = gf.Group() # Variable for bullets

    Fps = 40 # Variable for Frame per second (Fps)
    asteroid_timer = pygame.time.get_ticks() # Variable for asteroid's timer
    # as long as statement is True, it will run.
    while True:
        theClock.tick(Fps) #Counting frames every 1 second passes.
        Fps += 0.01 #game speed goes faster after every frame
        """background moving"""
        x -= 5 # value of x is decreased by 5.
        x1 -= 5 # value of x1 is decreased by 5.
        bg_image.draw(screen,x,y) # Show the background image based on variable x and y.
        bg_image.draw(screen,x1, y1) # Show the background image based on variable x1 and y1.
        if x < -bg_image.width: # if value of x is lower than minus value of background image's width, it will return to 0.
            x = 0
        if x1 < 0: # if value of x1 is lower than 0, it will return to value of background image's width.
            x1 = bg_image.width
        # create score board
        font=pygame.font.SysFont("Times New Romans",36) # Variable for font
        score_board=font.render("score:"+str(scores),True,(255,255,255)) # Variable for rendering score board text with font and color.
        # update referred to the word's method
        screen.blit(score_board,(10,550)) # Draw score board in game screen
        Jet_sprites.draw(screen) # Draw space jet
        bullets.draw(screen) # Draw bullets
        asteroid_group.draw(screen) # Draw group of asteroids
        pygame.display.update() # update display of game
        pygame.event.get() # get event
        """moving the jet according to key pressed"""
        key = pygame.key.get_pressed() # Variable for pressing key
        if key[pygame.K_LEFT] and jet1.rect.x > 0: # if left directional key is pressed, space jet will move to left until it reaches the border
            jet1.moveleft()
        elif key[pygame.K_RIGHT] and jet1.rect.x <= 700: # if right directional key is pressed, space jet will move to left until it reaches the border
            jet1.moveright()
        elif key[pygame.K_DOWN] and jet1.rect.y <= 500: # if down directional key is pressed, space jet will move to left until it reaches the border
            jet1.movedown()
        elif key[pygame.K_UP] and jet1.rect.y > 0: # if up directional key is pressed, space jet will move to left until it reaches the border
            jet1.moveup()
        # if space key is pressed, space jet will shoot bullet until bullets reach the limit.
        if key[pygame.K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = gf.Bullet(screen, jet1.rect.x+50, jet1.rect.y+42) # Variable for bullet in a certain position based on space jet
            bullets.add(bullet) # Add bullets
            pygame.mixer.music.load("bgsound/LaserBlast.wav") # Load the sound of bullet
            pygame.mixer.music.play() # Play the sound of bullet.
        if key[pygame.K_ESCAPE]: # if escape key is pressed, game will be ended.
            meteor_shooter_menu.menu_screen(gf.Button,run_game)
        if key[pygame.K_p]:  # if P key is pressed, game will be paused
            meteor_shooter_menu.pause_menu(gf.Button,run_game)

        """generate asteroid randomly"""
        # if game time which is subtracted by asteroid's timer value is greater than or equal to 200, it will show asteroid randomly.
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            # Variable for showing asteroid randomly
            asteroid = gf.Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            asteroid_group.add(asteroid) # Add group of asteroids
            asteroid_timer = pygame.time.get_ticks() # Variable for asteroid's timer

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement() # Move asteroid
            if asteroid.rect.right <= 0: # if value of asteroid.rect.right is lower than or equal to 0, it will remove asteroid after screen
                asteroid_group.remove(asteroid)
            # Checking whether there is colliding between jet space and asteroid or not
            if gf.groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):
                meteor_shooter_menu.lose_menu(gf.Button,run_game,scores) # Show lose menu after colliding

        """update bullet movement on screen"""
        for bullet in bullets:
            # Move bullet
            bullet.movement()
            # if value of bullet.rect.left is greater than 800, it will remove bullet after screen
            if bullet.rect.left > 800:
                bullets.remove(bullet)
            # Checking whether there is colliding between bullet and asteroid or not
            if gf.groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100 # value of scores will increase after colliding
# Initialize menu_screen function from meteor_shooter_menu
meteor_shooter_menu.menu_screen(gf.Button,run_game)

