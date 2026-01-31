import pygame
import math
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 707))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
button = 0
# image = pygame.image.load('data/images/autumn.jpg')

bg = pygame.image.load("cover.png")
img = pygame.image.load("x.png")

eg = pygame.image.load("emoji.png")
# Set image as icon
pygame.display.set_icon(img)

# INSIDE OF THE GAME LOOP
# game_running = True


# ----تابع باشه بهتره برای متن
# ، برای هر تکست جدیدی، تو اون مین لوپ فقط تابع رو راخوانی میکنی
# دیگه اینجا هم نمینویسیش
my_font = pygame.font.SysFont("Comic Sans MS", 50)

# (0, 0 , 0)  == black
# white=(255,255,255)
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# If it is set to False, the rendered image is an 8-bit image, and 24-bit if true.
text_surface = my_font.render("Tic Tac Toe", True, (0, 0, 0))
my_font = pygame.font.SysFont("Comic Sans MS", 30)
text_surface2 = my_font.render("Enjoy it!", True, (0, 0, 0))
text1 = my_font.render("[double click to start]", True, (0, 0, 0))
text2 = my_font.render("starter?", True, (0, 0, 0))


def drawIntro(screen):
    # start
    if button == 0:  # == 0
        screen.blit(bg, (0, 0))
        screen.blit(eg, (310, 160))

        screen.blit(text_surface, (110, 40))
        screen.blit(text_surface2, (180, 150))
        screen.blit(text1, (105, 200))

    elif button == 2:  # page1
        screen.blit(bg, (0, 0))
        screen.blit(text2, (180, 150))

    elif button == 3:  # page2
        screen.fill((0, 0, 0))
        text = my_font.render("page 2", True, (255, 255, 255))
        screen.blit(text, (300, 220, 500, 200))

    elif button == 3:  # page3
        screen.fill((0, 0, 0))
        text = my_font.render("page3", True, (255, 255, 255))
        screen.blit(text, (200, 190, 500, 200))


running = True
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:  # Once per click.
            button += 1

    drawIntro(screen)
    pygame.display.flip()

pygame.quit()


# # Main game loop
# while game_running:
#     # Handle events
#     for event in pygame.event.get():
#        if event.type == pygame.KEYDOWN :
#            if event.key == pygame.K_SPACE :
#                print("Pause")
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()

#     screen.blit(bg, (0, 0))
#     screen.blit(eg, (310, 160))

#     screen.blit(text_surface, (110,40))
#     screen.blit(text_surface2, (180,150))

#     # Update the display
#     pygame.display.update()


# pygame.quit()
