import pygame
from pygame import mixer
import random
import math


pygame.init()


screen = pygame.display.set_mode((800, 600))


background = icon = pygame.image.load('background.jpg')


mixer.music.load("war.wav")
mixer.music.play(-1)


pygame.display.set_caption("Legendary tank")
icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('tank2.png')
playerX = 370
playerY = 480
playerX_change = 0


planeImg = []
planeX = []
planeY = []
planeX_change = []
planeY_change = []
num_of_plane = 4

for i in range(num_of_plane):
    planeImg.append(pygame.image.load('plane.png'))
    planeX.append(random.randint(0, 800))
    planeY.append(random.randint(50, 150))
    planeX_change.append(4)
    planeY_change.append(40)


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"



pygame.display.update()