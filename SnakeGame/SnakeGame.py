import pygame
import time
import random
 
pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# set screen size
width = 1200
height = 800
 
# create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
 
# set clock
clock = pygame.time.Clock()
 
# set font
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    """
    Displays message on the screen
    """
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])
 
 
def game_loop():
    # set game over to False
    game_over = False
 
    # set initial position of snake
    x1 = width / 2
    y1 = height / 2
 
    # set change in position of snake
    x1_change = 0       
    y1_change = 0
 
    # set size of snake
    snake_block = 10
 
    # create food for snake
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
     
    while not game_over:
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the game
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # move snake left
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    # move snake right
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    # move snake up
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    # move snake down
                    y1_change = snake_block
                    x1_change = 0
 
        # check if snake hits the boundary of the screen
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
 
        # update snake's position
        x1 += x1_change
        y1 += y1_change
 
        # fill screen with black color
        screen.fill(black)
 
        # draw food on screen
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
 
        # create snake and draw it on screen
        pygame.draw.rect(screen, white, [x1, y1, snake_block, snake_block])
 
        # update display
        pygame.display.update()
 
        # check if snake eats the food
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
		snake_block += 10
 
        # set clock to 15 FPS
        clock.tick(15)
 
    # quit pygame module
    pygame.quit()
 
    # quit python
    quit()
 
game_loop()
