# import all modules from pygame
from pygame import *
# import system module
import sys
# import pygame module
import pygame
# Define a function to show menu screen
def menu_screen(Button,run_game):
    # show the title of game screen
    display.set_caption("Asteroid Fighter")
    # variable for game screen
    screen = pygame.display.set_mode((800, 600))
    # variables for start and quit buttons
    start_button = Button("sprites/New Piskel.png")
    quit_button = Button("sprites/quit button.png")
    # variables for loading and scaling background image
    bg_image=pygame.image.load("bg/asteroid_wall.jpg")
    bg_image=pygame.transform.scale(bg_image, (800, 600))

    pygame.init() # Initialize pygame module
    # as long as statement is True, it will run.
    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) # Variable for coordinating start button
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) # Variable for coordinating quit button
        screen.blit(bg_image,(0,0)) # Show background image
        screen.blit(start_button.button,(250,200)) # Show start button
        screen.blit(quit_button.button,(250,300)) # Show quit button
        ev = event.wait() # Variable for waiting event
        # if event type is equal to clicking mouse key, it will do an action
        if ev.type == MOUSEBUTTONDOWN:
            # if start button is clicked, it will run game
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            # if quit button is clicked, it will quit game
            elif rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()
        # if event type is equal to close window, it will quit game
        if ev.type == QUIT:
            sys.exit()
        display.update() # Update the display
# Define a function to show pause menu screen
def pause_menu(Button,run_game):
    # show the title of game screen
    display.set_caption("Asteroid Fighter")
    # variable for game screen
    screen = pygame.display.set_mode((800, 600))
    # variables for quit and continue buttons
    quit_button = Button("sprites/quit button.png")
    continue_button = Button("sprites/pause button.png")
    # variables for loading and scaling background image
    bg_image = pygame.image.load("bg/asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init() # Initialize pygame module

    paused = True # pause becomes True statement
    # as long as paused is True, it will run until paused becomes False statement.
    while paused:
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) # Variable for coordinating quit button
        rect_continue = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) # Variable for coordinating continue button
        screen.blit(bg_image, (0, 0)) # Show background image
        screen.blit(quit_button.button, (250, 200)) # Show quit button
        screen.blit(continue_button.button, (250, 300)) # Show continue button
        ev = event.wait() # Variable for waiting event
        # if event type is equal to clicking mouse key, it will do an action
        if ev.type == MOUSEBUTTONDOWN:
            # if quit button is clicked, it will return to menu screen
            if rect_quit.collidepoint(mouse.get_pos()):
                menu_screen(Button,run_game)
            # if continue button is clicked, it will return to game
            elif rect_continue.collidepoint(mouse.get_pos()):
                paused = False # paused becomes False statement
        # if event type is equal to close window, it will quit game
        if ev.type == QUIT:
            sys.exit()
        display.update() # Update the display
# Define a function to show lose menu screen
def lose_menu(Button,run_game,score):
    # show the title of game scree
    display.set_caption("Asteroid Fighter")
    # variable for game screen
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("times new roman",100) # Variable for font
    text = font.render("Game Over",True,(255,255,255)) # Variable for rendering "Game Over" text with font and color.
    score_text=font.render("score:"+str(score),True,(255,255,255)) # Variable for rendering score board text with font and color.
    # variables for start and quit buttons
    start_button = Button("sprites/New Piskel.png")
    quit_button = Button("sprites/quit button.png")
    # variables for loading and scaling background image
    bg_image = pygame.image.load("bg/asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init() # Initialize pygame module
    # as long as statement is True, it will run.
    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) # Variable for coordinating start button
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) # Variable for coordinating quit button
        screen.blit(bg_image, (0, 0)) # Show background image
        screen.blit(text,(200,10)) # Show "Game Over" text
        screen.blit(start_button.button, (250, 200)) # Show start button
        screen.blit(quit_button.button, (250, 300)) # Show quit button
        screen.blit(score_text,(200,400)) # Show score board text
        ev = event.wait() # Variable for waiting event
        # if event type is equal to clicking mouse key, it will do an action
        if ev.type == MOUSEBUTTONDOWN:
            # if start button is clicked, it will run game
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            # if quit button is clicked, it will quit game
            elif rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()
        # if event type is equal to close window, it will quit game
        if ev.type == QUIT:
            sys.exit()
        display.update() # Update the display
