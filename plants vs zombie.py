import pygame
import os
# from PIL import image
import sys
import random
import time
pygame.init()


# цвета
BLACK = (0, 0, 0)
changeX = 0
changeY = 0
SPEED = 1
SPEEDz = 1
changeXz = 0
changeYz = 0
# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Plants vs zombie")
# pygame.time()
# c=pygame.time.get_ticks()
# z = pygame.image.load('imag/images/зомби/зомби.gif')

zimages=[]
zimages.append(pygame.image.load('imag/images/визуальные эффекты/3.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/4.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/5.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/6.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/7.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/8.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/9.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/10.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/11.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/12.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/13.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/14.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/15.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/16.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/17.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/18.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/19.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/20.png'))
zimages.append(pygame.image.load('imag/images/визуальные эффекты/21.png'))

zombieindex = 0 # кадр который рисуется из анимации (zimages)
zombie = zimages[zombieindex]
zombierect = zombie.get_rect()


# # z1=pygame.Surface((150, 180))
# z1=pygame.image.load('imag/images/зомби/normalzombie.gif')
# z1=pygame.transform.scale(z1,(120,180))
# # z2=pygame.Surface((150, 180))
# z2=pygame.image.load('imag/images/зомби/coneheadzombie.gif')
# z2=pygame.transform.scale(z2,(200,200))
# # z3=pygame.Surface((150, 180))
# z3=pygame.image.load('imag/images/зомби/bucketheadzombie.gif')
# z3=pygame.transform.scale(z3,(120,180))
# # z4=pygame.Surface((150, 180))
# z4=pygame.image.load('imag/images/зомби/coneheadzombie.gif')
# z4=pygame.transform.scale(z4,(200,200))

# visual effects
sun = pygame.image.load('imag/images/визуальные эффекты/sun.png')
fire = pygame.image.load('imag/images/визуальные эффекты/jalapenoFire.gif')
pea = pygame.image.load('imag/images/визуальные эффекты/pea.png')
gaz = pygame.image.load('imag/images/визуальные эффекты/gaz.gif')
gazup = pygame.image.load('imag/images/визуальные эффекты/gazup.gif')

# size
sun = pygame.transform.scale(sun, (150, 150))
fire = pygame.transform.scale(fire, (150, 30))
pea = pygame.transform.scale(pea, (30, 30))
gaz = pygame.transform.scale(gaz, (150, 150))
gazup = pygame.transform.scale(gazup, (150, 150))

# rect
sunrect = sun.get_rect()
count_sun = 0
count_z = 0
# img bg
bg = pygame.image.load('imag/images/bg.png')
bg = pygame.transform.scale(bg, (1920, 1080))

# plants
p1 = pygame.image.load('imag/images/растения/p1.gif')
p2 = pygame.image.load('imag/images/растения/p2.gif')
potato = pygame.image.load('imag/images/растения/potato.gif')
sunflower = pygame.image.load('imag/images/растения/sunfl.gif')
p1 = pygame.transform.scale(p1, (130, 160))
p2 = pygame.transform.scale(p1, (130, 160))
potato = pygame.transform.scale(p1, (130, 160))
sunflower = pygame.transform.scale(p1, (130, 160))

# card
p1c = pygame.image.load('imag/images/карты растений/p1c.png')
p2c = pygame.image.load('imag/images/карты растений/p2c.png')
potatoc = pygame.image.load('imag/images/карты растений/pc.png')
sunflowerc = pygame.image.load('imag/images/карты растений/sc.png')
cherrycard = pygame.image.load('imag/images/карты растений/cherrybombCard.png')
jalapenocard = pygame.image.load('imag/images/карты растений/jalapenoCard.png')

# size
p1c = pygame.transform.scale(p1c, (200, 100))
p2c = pygame.transform.scale(p2c, (200, 100))
potatoc = pygame.transform.scale(potatoc, (200, 100))
sunflowerc = pygame.transform.scale(sunflowerc, (200, 100))
cherrycard = pygame.transform.scale(cherrycard, (200, 100))
jalapenocard = pygame.transform.scale(jalapenocard, (200, 100))

# alpha
p1c.set_alpha(100)
p2c.set_alpha(100)
potatoc.set_alpha(100)
sunflowerc.set_alpha(100)
cherrycard.set_alpha(100)
jalapenocard.set_alpha(100)

p1crect = p1c.get_rect()
p2crect = p2c.get_rect(topleft=(0, 100))
potatocrect = potatoc.get_rect(topleft=(0, 200))
sunflowercrect = sunflowerc.get_rect(topleft=(0, 300))
cherrycardrect = cherrycard.get_rect(topleft=(0, 400))
jalapenocardrect = jalapenocard.get_rect(topleft=(0, 500))

# timing = time.time()
# while True:
#     if time.time() - timing > 10.0:
#         timing = time.time()
#         c+=1
#         print(c)

cards = [
    [p1c, p1crect],
    [p2c, p2crect],
    [potatoc, potatocrect],
    [sunflowerc, sunflowercrect],
    [cherrycard, cherrycardrect],
    [jalapenocard, jalapenocardrect],
]

# score
score = 0
f = pygame.font.SysFont('arial', 56)

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

DRAW_ZOMBIE = pygame.USEREVENT + 1

pygame.time.set_timer(DRAW_ZOMBIE, 150)

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == DRAW_ZOMBIE:
            zombie = zimages[zombieindex]
            zombieindex += 1

            if zombieindex >= len(zimages):
                zombieindex = 0
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            sys.exit()

    mainScreen.fill(BLACK)
    mainScreen.blit(bg, (0, 0))
    

    # mainScreen.blit(z4, (1670, 90))
    # clock.tick(60)

    # mainScreen.blit(z, (1670, 250))
    # clock.tick(60)
    # mainScreen.blit(z1, (1670, 430))

    # clock.tick(60)
    # mainScreen.blit(z2, (1670, 590))

    # clock.tick(60)
    # mainScreen.blit(z3, (1670, 790))

    while count_sun != 1:
        sunrect.centerx = random.randint(100, WIDTH)
        sunrect.centery = random.randint(0, 100)
        count_sun += 1

    if count_sun == 1:
        if sunrect.bottom >= HEIGHT:
            sunrect.bottom = HEIGHT
        else:
            
            sunrect.y += changeY
        mainScreen.blit(sun, sunrect)
        

        if count_z!=1:
            zombierect.centerx = random.randint(1750, WIDTH)
            zombierect.centery = random.randint(90, 790)
            count_z += 1

    if count_z == 1:
        if zombierect.bottom >= WIDTH:
            zombierect.bottom = WIDTH
        else:
            changeXz = 0+ SPEEDz
            zombierect.x -= changeXz
        mainScreen.blit(zombie, zombierect)
    if zombierect.centerx <= 420:
        count_z = 0
    

        # mainScreen.blit(z4, (1670, 90))
        # clock.tick(60)

        # mainScreen.blit(z, (1670, 250))
        # clock.tick(60)
        # mainScreen.blit(z1, (1670, 430))

        # clock.tick(60)
        # mainScreen.blit(z2, (1670, 590))

        # clock.tick(60)
        # mainScreen.blit(z3, (1670, 790))

    # bg and card

    for card in cards:
        mainScreen.blit(card[0], card[1])

    sc_text = f.render('Счёт: ' + str(score), 1, BLACK)
    mainScreen.blit(sc_text, (1740, 0))
    
    clock.tick(FPS)
    pygame.display.flip()
    
    