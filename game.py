import pygame
from pygame import mixer
import random
import math


pygame.init()


screen = pygame.display.set_mode((800, 600))


background = icon = pygame.image.load('media/background.jpg')


mixer.music.load('audio/war.wav')
mixer.music.play(-1)


pygame.display.set_caption('Legendary tank')
icon = pygame.image.load('media/tank.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('media/tank2.png')
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
    planeImg.append(pygame.image.load('media/plane.png'))
    planeX.append(random.randint(0, 800))
    planeY.append(random.randint(50, 150))
    planeX_change.append(4)
    planeY_change.append(40)


bulletImg = pygame.image.load('media/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def virus(x, y):
    screen.blit(planeImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 50, y + 10))


def iscollision(planex, planey, bulletx, bullety):
    distance1 = math.sqrt(math.pow(planex-bulletx, 2))
    distance2 = + (math.pow(planey-bullety, 2))
    distance = distance1 + distance2
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_Sound = mixer.Sound('audio/tank shoot.wav')
                    bullet_Sound.play()

                    # get the current x coordinate of protective-wear
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_plane):

        if planeY[i] > 440:
            for j in range(num_of_plane):
                planeY[j] = 2000
            game_over_text()
            break

        planeX[i] += planeX_change[i]
        if planeX[i] <= 0:
            planeX_change[i] = 1
            planeY[i] += planeY_change[i]
        elif planeX[i] >= 736:
            planeX_change[i] = - 1
            planeY[i] += planeY_change[i]

        collision = iscollision(planeX[i], planeY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('audio/plane explosion.mp3')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            planeX[i] = random.randint(0, 736)
            planeY[i] = random.randint(50, 150)

        virus(planeX[i], planeY[i], )

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()

pygame.display.update()
