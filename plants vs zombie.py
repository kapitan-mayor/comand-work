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
count_sun = 0

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Plants vs zombie")

#visual effects
sun = pygame.image.load('command work/imag/images/визуальные эффекты/sun.png')
fire = pygame.image.load('command work/imag/images/визуальные эффекты/jalapenoFire.gif')
pea = pygame.image.load('command work/imag/images/визуальные эффекты/pea.png')
gaz = pygame.image.load('command work/imag/images/визуальные эффекты/gaz.gif')
gazup = pygame.image.load('command work/imag/images/визуальные эффекты/gazup.gif')

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
bg = pygame.image.load('command work/imag/bg.png')
bg = pygame.transform.scale(bg, (1920, 1080))

#plants
p1 = pygame.image.load('command work/imag/images/растения/p1.gif')
p2 = pygame.image.load('command work/imag/images/растения/p2.gif')
potato = pygame.image.load('command work/imag/images/растения/potato.gif')
sunflower = pygame.image.load('command work/imag/images/растения/sunfl.gif')
p1 = pygame.transform.scale(p1, (130, 160))
p2 = pygame.transform.scale(p1, (130, 160))
potato = pygame.transform.scale(p1, (130, 160))
sunflower = pygame.transform.scale(p1, (130, 160))

p1rect = p1.get_rect()
p2rect = p2.get_rect()
potatorect = potato.get_rect()
sunflowerrect = sunflower.get_rect()

#card
p1c = pygame.image.load('command work/imag/images/карты растений/p1c.png')
p2c = pygame.image.load('command work/imag/images/карты растений/p2c.png')
potatoc =pygame.image.load('command work/imag/images/карты растений/pc.png')
sunflowerc = pygame.image.load('command work/imag/images/карты растений/sc.png')
cherrycard = pygame.image.load('command work/imag/images/карты растений/cherrybombCard.png')
jalapenocard = pygame.image.load('command work/imag/images/карты растений/jalapenoCard.png')

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

alpha_cards = [p1c, p2c, potatoc, sunflowerc, cherrycard, jalapenocard]

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

pygame.time.set_timer(SPAWN_SUN, 10000)

shop = []


while runnig:
    # проверяем события, которые произошли (если они были)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
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
        if card['rect'].collidepoint(event.pos) == True and score >= card['cost']:
            mainScreen.blit(card['card'], card['rect'].set_alpha(100))


        mainScreen.blit(card['card'], card['rect'])

    #score
    sc_text = q.render('Счёт: ' + str(score), 1, BLACK)
    mainScreen.blit(sc_text, (1600, 0))   
    
    
    pygame.display.flip()
    clock.tick(FPS)