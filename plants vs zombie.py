import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs zombie")


#img bg
bg = pygame.image.load('comand work/imag/bg.png')
bg = pygame.transform.scale(bg, (1920, 1080))

#plants
p1 = pygame.image.load('comand work/imag/images/растения/p1.gif')
p2 = pygame.image.load('comand work/imag/images/растения/p2.gif')
potato = pygame.image.load('comand work/imag/images/растения/potato.gif')
sunflower = pygame.image.load('comand work/imag/images/растения/sunfl.gif')

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # заливаем главный фон черным цветом
    mainScreen.blit(bg, (0, 0))
    pygame.display.update()
    clock.tick(60)    
    

    pygame.display.flip()
    clock.tick(FPS)