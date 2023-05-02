import os
from PIL import Image
import glob
import pygame, sys
import random
import time
import threading
import sys
pygame.init()
# from tkinter import *
# from tkinter import ttk

# #window
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")

# def click():
#     window = Tk()
#     window.title("Новое окно")
#     window.geometry("250x200")
 
# button = ttk.Button(text="Создать окно", command=click)
# button.pack(anchor=CENTER, expand=1)
 
# root.mainloop()

# цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
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

paused = False

zombi1 = pygame.image.load('imag/images/визуальные эффекты/3.png')
zombi2 = pygame.image.load('imag/images/визуальные эффекты/4.png')
zombi3 = pygame.image.load('imag/images/визуальные эффекты/5.png')
zombi4 = pygame.image.load('imag/images/визуальные эффекты/6.png')
zombi5 = pygame.image.load('imag/images/визуальные эффекты/7.png')
zombi6 = pygame.image.load('imag/images/визуальные эффекты/8.png')
zombi7 = pygame.image.load('imag/images/визуальные эффекты/9.png')
zombi8 = pygame.image.load('imag/images/визуальные эффекты/10.png')
zombi9 = pygame.image.load('imag/images/визуальные эффекты/11.png')
zombi10 = pygame.image.load('imag/images/визуальные эффекты/12.png')
zombi11 = pygame.image.load('imag/images/визуальные эффекты/13.png')
zombi12 = pygame.image.load('imag/images/визуальные эффекты/14.png')
zombi13 = pygame.image.load('imag/images/визуальные эффекты/15.png')
zombi14 = pygame.image.load('imag/images/визуальные эффекты/16.png')
zombi15 = pygame.image.load('imag/images/визуальные эффекты/17.png')
zombi16 = pygame.image.load('imag/images/визуальные эффекты/18.png')
zombi17 = pygame.image.load('imag/images/визуальные эффекты/19.png')
zombi18 = pygame.image.load('imag/images/визуальные эффекты/20.png')
zombi18 = pygame.image.load('imag/images/визуальные эффекты/21.png')


zombi1 = pygame.transform.scale(zombi1, (240, 240))
zombi2 = pygame.transform.scale(zombi2, (240, 240))
zombi3 = pygame.transform.scale(zombi3, (240, 240))
zombi4 = pygame.transform.scale(zombi4, (240, 240))
zombi5 = pygame.transform.scale(zombi5, (240, 240))
zombi6 = pygame.transform.scale(zombi6, (240, 240))
zombi7 = pygame.transform.scale(zombi7, (240, 240))
zombi8 = pygame.transform.scale(zombi8, (240, 240))
zombi9 = pygame.transform.scale(zombi9, (240, 240))
zombi10 = pygame.transform.scale(zombi10, (240, 240))
zombi11 = pygame.transform.scale(zombi11, (240, 240))
zombi12 = pygame.transform.scale(zombi12, (240, 240))
zombi13 = pygame.transform.scale(zombi13, (240, 240))
zombi14 = pygame.transform.scale(zombi14, (240, 240))
zombi15 = pygame.transform.scale(zombi15, (240, 240))
zombi16 = pygame.transform.scale(zombi16, (240, 240))
zombi17 = pygame.transform.scale(zombi17, (240, 240))
zombi18 = pygame.transform.scale(zombi18, (240, 240))
zombi18 = pygame.transform.scale(zombi18, (240, 240))

zimages=[]
zimages.append(zombi1)
zimages.append(zombi2)
zimages.append(zombi3)
zimages.append(zombi4)
zimages.append(zombi5)
zimages.append(zombi6)
zimages.append(zombi7)
zimages.append(zombi8)
zimages.append(zombi9)
zimages.append(zombi10)
zimages.append(zombi11)
zimages.append(zombi12)
zimages.append(zombi13)
zimages.append(zombi14)
zimages.append(zombi15)
zimages.append(zombi16)
zimages.append(zombi17)
zimages.append(zombi18)
zimages.append(zombi18)

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
    { 
        'card': p1c, 
        'rect': p1crect, 
        'cost': 100,
        'plant': p1,
        'plantrect': p1.get_rect(topleft = (p1crect.x, p1crect.y))
    }, 
    { 'card': p2c, 'rect': p2crect, 'cost': 200 }, 
    { 'card': potatoc, 'rect': potatocrect, 'cost': 50 }, 
    { 'card': sunflowerc, 'rect': sunflowercrect, 'cost': 50 }, 
    { 'card': cherrycard, 'rect': cherrycardrect, 'cost': 150 }, 
    { 'card': jalapenocard, 'rect': jalapenocardrect, 'cost': 125 }
]

clickedplant = None
clickedplantrect = None

#score
score = 0
q = pygame.font.SysFont('arial', 56)
w =pygame.font.SysFont('bold', 200)

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

pause = False
shop = []
paused = w.render("ПАУЗА", 1, GREEN)

# def menu(SPEEDz, SPEED, changeX, changeXz, changeY):
#     mainScreen.blit(paused, (1600, 0))
#     SPEEDz = 0
#     SPEED = 0
#     changeX = 0
#     changeXz = 0
#     changeY = 0


while runnig:
    # проверяем события, которые произошли (если они были)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        pos = pygame.mouse.get_pos()
        
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
            if event.key == pygame.K_TAB:
                mainScreen.blit(paused, (1600, 0))
                SPEEDz = 0
                SPEED = 0
                changeX = 0
                changeXz = 0
                changeY = 0
                pause = True
            if pause == True:    
                if event.key == pygame.K_TAB:
                    mainScreen.blit(bg, (0, 0))
                    SPEEDz = 1
                    SPEED = 1
                    changeX = 0
                    changeXz = 0
                    changeY = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(sunrect.collidepoint(event.pos), 'gotcha or not')
                if sunrect.collidepoint(event.pos) == True:    
                    score += 50
                    count_sun = 0
                    pygame.time.set_timer(SPAWN_SUN, 10000)
            
            # if card['rect'].collide(event.pos) == True and score >= card['cost']:
            #     mainScreen.blit(card['card'], card['rect'].set_alpha(100))    
            #     clickedplant = 
            

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

    clock.tick(60)

    #card
    for card in alpha_cards:
        if score >= card['cost']:
            card['card'].set_alpha(255)
        else:
            card['card'].set_alpha(100)
        


        mainScreen.blit(card['card'], card['rect'])

    #score
    sc_text = q.render('Счёт: ' + str(score), 1, BLACK)
    mainScreen.blit(sc_text, (1600, 0))   
    
    
    pygame.display.flip()
    clock.tick(FPS)