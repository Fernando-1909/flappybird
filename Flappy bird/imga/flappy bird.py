import random
import pygame
import Itens
from pygame.locals import *

width, height= 800, 600
gover = True
cair = False
game = True

pygame.init()
win = pygame.display.set_mode((width, height))
bird0 = pygame.image.load("img/flp0.png")
bird1 = pygame.image.load("img/flp1.png")
piso = pygame.image.load("img/piso.png")
tubo = pygame.image.load("img/tubo.png")
cena = pygame.image.load("img/fundo.png")

#Objetos
ply = itens.itens(win, 200, height/3, 50, 50, bird0, 0)


def paint():
    pygame.display.update()
    pygame.time.delay(10)
    win.fill(0x3C2EE)

    ply.show()

def control():
    global gover

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            return False
    
    return True

while game:
    paint()
    game = control()