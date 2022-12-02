import pygame

class Itens:
    def __init__(self, win, x, y, w, h, img, r):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.visible = True
        self.img = img
        self.win = win

    def show(self):
        image = pygame.transform.rotate(self.img, self.r)
        if self.visible:
            self.win.blit(image, (self.x, self.y))
