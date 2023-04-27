import os
from PIL import Image
import glob
import pygame, sys
import random
import time
import threading
pygame.init()


# цвета
BLACK = (0, 0, 0)
changeX = 0
changeY = 0
SPEED = 1
SPEEDz = 1
count_sun = 0
count_z = 0

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Plants vs zombie")


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

#visual effects
sun = pygame.image.load('imag/images/визуальные эффекты/sun.png')
fire = pygame.image.load('imag/images/визуальные эффекты/jalapenoFire.gif')
pea = pygame.image.load('imag/images/визуальные эффекты/pea.png')
gaz = pygame.image.load('imag/images/визуальные эффекты/gaz.gif')
gazup = pygame.image.load('imag/images/визуальные эффекты/gazup.gif')

#size
sun = pygame.transform.scale(sun, (150, 150))
fire = pygame.transform.scale(fire, (150, 30))
pea = pygame.transform.scale(pea, (30, 30))
gaz = pygame.transform.scale(gaz, (150, 150))
gazup = pygame.transform.scale(gazup, (150, 150))

#rect
sunmass = []
sunrect = sun.get_rect()
sunmass.append(sunrect)
start_ticks=pygame.time.get_ticks()

#img bg
bg = pygame.image.load('imag/images/bg.png')
bg = pygame.transform.scale(bg, (1920, 1080))

#plants
p1 = pygame.image.load('imag/images/растения/p1.gif')
p2 = pygame.image.load('imag/images/растения/p2.gif')
potato = pygame.image.load('imag/images/растения/potato.gif')
sunflower = pygame.image.load('imag/images/растения/sunfl.gif')
p1 = pygame.transform.scale(p1, (130, 160))
p2 = pygame.transform.scale(p1, (130, 160))
potato = pygame.transform.scale(p1, (130, 160))
sunflower = pygame.transform.scale(p1, (130, 160))

p1rect = p1.get_rect()
p2rect = p2.get_rect()
potatorect = potato.get_rect()
sunflowerrect = sunflower.get_rect()

#card
p1c = pygame.image.load('imag/images/карты растений/p1c.png')
p2c = pygame.image.load('imag/images/карты растений/p2c.png')
potatoc =pygame.image.load('imag/images/карты растений/pc.png')
sunflowerc = pygame.image.load('imag/images/карты растений/sc.png')
cherrycard = pygame.image.load('imag/images/карты растений/cherrybombCard.png')
jalapenocard = pygame.image.load('imag/images/карты растений/jalapenoCard.png')

#size
p1c = pygame.transform.scale(p1c, (200, 100))
p2c = pygame.transform.scale(p2c, (200, 100))
potatoc = pygame.transform.scale(potatoc, (200, 100))
sunflowerc = pygame.transform.scale(sunflowerc, (200, 100))
cherrycard = pygame.transform.scale(cherrycard, (200, 100))
jalapenocard = pygame.transform.scale(jalapenocard, (200, 100))

#alpha
p1c.set_alpha(100)
p2c.set_alpha(100)
potatoc.set_alpha(100)
sunflowerc.set_alpha(100)
cherrycard.set_alpha(100)
jalapenocard.set_alpha(100)

p1crect = p1c.get_rect()
p2crect = p2c.get_rect(topleft = (0, 100))
potatocrect = potatoc.get_rect(topleft = (0, 200))
sunflowercrect = sunflowerc.get_rect(topleft = (0, 300))
cherrycardrect = cherrycard.get_rect(topleft = (0, 400))
jalapenocardrect = jalapenocard.get_rect(topleft = (0, 500))

alpha_cards = [
    { 'card': p1c, 'rect': p1crect, 'cost': 100 }, 
    { 'card': p2c, 'rect': p2crect, 'cost': 200 }, 
    { 'card': potatoc, 'rect': potatocrect, 'cost': 50 }, 
    { 'card': sunflowerc, 'rect': sunflowercrect, 'cost': 50 }, 
    { 'card': cherrycard, 'rect': cherrycardrect, 'cost': 150 }, 
    { 'card': jalapenocard, 'rect': jalapenocardrect, 'cost': 125 }
]

#score
score = 0
q = pygame.font.SysFont('arial', 56)

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()
runnig = True
counter = 10
  
# custom user event to change color
SPAWN_SUN = pygame.USEREVENT + 1
print('SPAWN_SUN', SPAWN_SUN)

DRAW_ZOMBIE = pygame.USEREVENT + 2

pygame.time.set_timer(SPAWN_SUN, 10000)
pygame.time.set_timer(DRAW_ZOMBIE, 150)

shop = []


while runnig:
    # проверяем события, которые произошли (если они были)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == DRAW_ZOMBIE:
            zombie = zimages[zombieindex]
            zombieindex += 1

            if zombieindex >= len(zimages):
                zombieindex = 0
        if event.type == SPAWN_SUN:
            print('start sun event')
            while count_sun != 1:
                sunrect.centerx = random.randint(100, WIDTH)
                sunrect.centery = random.randint(0, 100)
                count_sun += 1 
                pygame.time.set_timer(SPAWN_SUN, 0)    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("escape pressed")
                pygame.quit()
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(sunrect.collidepoint(event.pos), 'gotcha or not')
                if sunrect.collidepoint(event.pos) == True:    
                    score += 50
                    count_sun = 0
                    pygame.time.set_timer(SPAWN_SUN, 10000)
    print(shop)
    mainScreen.fill(BLACK)
    mainScreen.blit(bg, (0, 0))

    if count_sun == 1:
        print('start blit sun')
        if sunrect.bottom >= HEIGHT:
            sunrect.bottom = HEIGHT
        else:
            changeY += 0.01 * SPEED     
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

        

    # if score >= 50:
    #     if score >= 200:
    #         for i in alpha_cards:
    #             alpha_cards[i] = alpha_cards[i].set_alpha(255)


    clock.tick(60)

    #card
    for card in alpha_cards:
        if score >= card['cost']:
            card['card'].set_alpha(255)
        else:
            card['card'].set_alpha(100)
        # if card['rect'].collidepoint(event.pos) == True and score >= card['cost']:
        #     mainScreen.blit(card['card'], card['rect'].set_alpha(100))


        mainScreen.blit(card['card'], card['rect'])

    #score
    sc_text = q.render('Счёт: ' + str(score), 1, BLACK)
    mainScreen.blit(sc_text, (1600, 0))   
    
    
    pygame.display.flip()
    clock.tick(FPS)