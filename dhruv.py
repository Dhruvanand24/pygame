import pygame
from time import sleep
import random
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 800
score = -1
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorize Made BY Dhruv Anand")

tile_size = 266
# load images
background = pygame.image.load('./Purple_website.svg.webp')
tileimg = pygame.image.load('./metallic-textured-background_53876-89255.webp')
tileimg = pygame.transform.scale(tileimg, (tile_size, tile_size))
inplist = []
finallist = []
make = []
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
dictx = {
    7: 0,
    8: 266,
    9: 532,
    4: 0,
    5: 266,
    6: 532,
    1: 0,
    2: 266,
    3: 532,
}

dicty = {
    7: 0,
    8: 0,
    9: 0,
    4: 266,
    5: 266,
    6: 266,
    1: 532,
    2: 532,
    3: 532,
}


def draw_grid():
    for line in range(0, 4):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


def stages():
    r = random.randint(1, 9)
    make.append(r)
    sleep(1)
    for k in make:
        screen.blit(tileimg, (dictx[k], dicty[k]))
        pygame.display.update()
        sleep(1)
        screen.blit(background, (0, 0))
        draw_grid()
        pygame.display.update()
    inplist.clear()
    return


def showscore():
    font = pygame.font.Font('freesansbold.ttf', 60)
    text = font.render(str(score), True, green, blue)
    textrect = text.get_rect()
    textrect.center = (screen_height // 2, screen_width // 2)
    while run:
        screen.fill(white)
        screen.blit(text, textrect)
        pygame.display.update()
        sleep(4)
        return
    return

run = True
while run:
    if (len(make) == len(finallist)) and (make != finallist):
        showscore()
        make.clear()
        finallist.clear()
        score = -1
        inplist.clear()

    screen.blit(background, (0, 0))
    draw_grid()
    finallist = inplist
    if make == finallist:
        score += 1
        stages()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP7 or event.key == pygame.K_q:
                inplist.append(7)
            if event.key == pygame.K_KP8 or event.key == pygame.K_w:
                inplist.append(8)
            if event.key == pygame.K_KP9 or event.key == pygame.K_e:
                inplist.append(9)
            if event.key == pygame.K_KP4 or event.key == pygame.K_a:
                inplist.append(4)
            if event.key == pygame.K_KP5 or event.key == pygame.K_s:
                inplist.append(5)
            if event.key == pygame.K_KP6 or event.key == pygame.K_d:
                inplist.append(6)
            if event.key == pygame.K_KP1 or event.key == pygame.K_z:
                inplist.append(1)
            if event.key == pygame.K_KP2 or event.key == pygame.K_x:
                inplist.append(2)
            if event.key == pygame.K_KP3 or event.key == pygame.K_c:
                inplist.append(3)

    pygame.display.update()
pygame.quit()
