import pygame as pg


class Log(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(pg.image.load("../assets/log.png"), (50, 50))
        self.rect = self.image.get_rect()

        self.movex = 0
        self.movey = 0

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
