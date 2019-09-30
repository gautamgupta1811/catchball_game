import pygame
import random
#import time
pygame.init()

#height = 500
#width = 1000
count = 0
screen = pygame.display.set_mode((width, height))

#white = 255, 255, 255
#black = 0, 0, 0
#red = 255, 0, 0
#blue = 0, 0, 255
#green = 0, 255, 0

def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(count), True, black)
    screen.blit(text, (width-100, 0))


def gameover():
    font = pygame.font.SysFont(None, 100)
    text = font.render("GAME OVER", True, black)
    screen.blit(text, (width / 2 - 200, height / 2 - 50))


basketWidth = 100
basketHeight = 100
basketX = int((width-basketWidth)/2)
basketY = height - basketHeight
movebasketX = 0
movebasketY = 0

ballRadius = 10
ballY = 0
ballX = random.randint(ballRadius * 2, width - (2 * ballRadius))
moveBall = 1

lifeList = []
lifeRadius = 5
for life in range(3):
    lifeList.append(pygame.Rect((10 + lifeRadius) * life, (10 + lifeRadius), 5, lifeRadius))

FPS = 500


while True:

    screen.fill(white)
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movebasketX = -4
            elif event.key == pygame.K_RIGHT:
                movebasketX = 4
        elif event.type == pygame.KEYUP:
            movebasketX = 0
    for i in range(len(lifeList)):
        pygame.draw.circle(screen, red, [(10 + (lifeRadius + 10) * i), 10], lifeRadius)


   #pygame.draw.rect(screen, red, [0, 0, width, 50])
    basket_rect = pygame.draw.rect(screen, red, (basketX, basketY, basketWidth, basketHeight))
    pygame.draw.circle(screen, red, [ballX, ballY], ballRadius)

    ball_rect = pygame.Rect(ballX, ballY, ballRadius*2, ballRadius*2)
    basketX += movebasketX
    ballY += moveBall

    score(count)

    if ball_rect.colliderect(basket_rect):
        ballX = random.randint(ballRadius * 2, width - (2 * ballRadius))
        ballY = 0
        FPS += 20
        count += 1

    elif ballY == height+height:
        ballX = random.randint(ballRadius * 2, width - (2 * ballRadius))
        ballY = 0
        FPS += 20
        del lifeList[-1]
    if len(lifeList) == 0:
        ballY = -ballRadius-10
        moveBall = 0
        movebasketX = 0
        movebasketY = 0
        gameover()

    if basketX > width:
        basketX = -basketWidth
    elif basketX < -basketWidth:
        basketX = width
    clock.tick(FPS)

    pygame.display.update()



