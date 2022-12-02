import random
import pygame
import itens
from pygame.locals import *

width, height= 800, 600
gover = True
cair = False
game = True
cano = []
mover = 1
speed = 4
vel_y = 0
asas = 0

pts = 0
top = 0

pygame.init()
win = pygame.display.set_mode((width, height))
bird0 = pygame.image.load("imga/flp0.png")
bird1 = pygame.image.load("imga/flp1.png")
piso = pygame.image.load("imga/piso.png")
tubo = pygame.image.load("imga/tubo.png")
cena = pygame.image.load("imga/fundo.png")

# Objetos
ply = itens.Itens(win, 200, height / 3, 50, 50, bird0, 0)
fundo0 = itens.Itens(win, 0, 210, 0, 0, cena, 0)
fundo1 = itens.Itens(win, width, 210, 0, 0, cena, 0)
piso0 = itens.Itens(win, 0, 466, 0, 0, cena, 0)
piso1 = itens.Itens(win, width, 466, 0, 0, cena, 0)

for i in range(2):
    cano.append([0] * 4)

for i in range(4):
    cano[0][i] = itens.Itens(win, i * 210, -100, 87, 310, tubo, 0)
    cano[1][i] = itens.Itens(win, i * 210, 400, 87, 310, tubo, 0)

def restart():
    global vel_y, speed, cair, pts

    for i in range(4):
        cano[0][i].x = width + i * 220
        cano[1][i].x = width + i * 220
        visible = random.randint(0, 1)
        cano[0][i].visible = visible
        cano[1][i].visible = visible
        canoy = random.randint(0, 9) * -(cano[0][0].h/10)
        cano[0][i].y = canoy
        cano[1][i].y = canoy + 470
        cano[1][i].r = 180
    
    ply.y = height/3
    vel_y = 0
    cair = False
    pts = 0

#Colisao
def colidir(a, b):
    return a.x + a.w > b.x and a.x < b.x + b.w and a.y + a.h > b.y and a.y < b.y + b.h

def paint():
    global asas
    pygame.display.update()
    pygame.time.delay(10)
    win.fill(0x3C2EE)

    #Movendo o cenario
    if fundo0.x < -width:
        fundo0.x = 0
        fundo1.x = width

    fundo0.x -= mover * 1
    fundo1.x -= mover * 1
    fundo0.show()
    fundo1.show()

    for i in range(4):
        cano[0][i].show()
        cano[1][i].show()
        cano[0][i].x -= mover * speed
        cano[1][i].x -= mover * speed
        if cano[0][i].x < -cano[0][0].w:
            visible = random.randint(0, 1)
            cano[0][i].visible = visible
            cano[1][i].visible = visible
            canoy = random.randint(0, 9) * -(cano[0][0].h/10)
            cano[0][i].y = canoy
            cano[1][i].y = canoy + 470
            cano[0][i].x = width
            cano[1][i].x = width

    if piso0.x < -width:
        piso0.x = 0
        piso1.x = width
    piso0.x -= mover * 5
    piso1.x -= mover * 5
    piso0.show()
    piso1.show()
    ply.show()

    asas += 1
    if asas >10:
        ply.img = bird0
    else:
        ply.img = bird1

    if asas > 20:
        asas = 0

def control():
    global gover, vel_y, mover, cair
    mover = not gover

    vel_y += mover
    ply.y += mover *vel_y
    ply.r = mover * (-vel_y) * 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            return False
        if event.type == KEYDOWN and event.key == K_SPACE and gover:
            gover = False
            restart()
        if event.type == pygame.MOUSEBUTTONDOWN and not cair:
            vel_y = mover * -12
    
    return True

def jogo():
    global gover, mover, pts, asas, cair

    #Perdendo
    for i in range(2):
        for j in range(4):
            if colidir(cano[i][j], ply) and cano[i][j].visible:
                cair = True
            if not i and 200 < cano[i][j].x < 205 and cano[i][j].visible and not gover:
                pts += 1
                if ply.y < cano[i][j].y:
                    cair = True
    if ply.y > piso0.y - ply.h:
        gover = True
        ply.r = -90
        asas = 0
        cair = True

def textos():
    global pts, top
    #recordes
    if pts >top:
        top=pts
    
    if gover and cair:
        font = pygame.font.SysFont("comic sans", 36, 1)
        pygame.draw.rect(win, 0x543847, [300, 100, 190, 200], 10)
        pygame.draw.rect(win, 0xDED895, [305, 104, 180, 190])
        txt = font.render("Pontos", 0, (255, 127, 39))
        win.blit(txt, (310, 110))
        txt = font.render(str(pts), 0, (255, 127, 39))
        win.blit(txt, (380, 146))
        txt = font.render("Ponto max", 0, (255, 127, 39))
        win.blit(txt, (310, 184))
        txt = font.render(str(top), 0, (255, 127, 39))
        win.blit(txt, (380, 220))
        txt = font.render("Aperte espaço", 0, (200, 208, 200), (0, 0, 0))
        win.blit(txt, (350, 530))
    else:
        font = pygame.font.SysFont("arial black", 35)
        txt = font.render(str(pts), 0, (255, 255, 255), 0x11d1E0)
        win.blit(txt, (380, 146))

while game:
    jogo()
    textos()
    paint()
    game = control()