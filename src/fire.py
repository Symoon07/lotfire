import pygame as pg


class Fire(pg.sprite.Sprite):
    def __int__(self, start_x, start_y):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pg.image.load('../assets/Fire/fire_0.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_1.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_2.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_3.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_4.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_5.png'))
        self.sprites.append(pg.image.load('../assets/Fire/fire_6.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        self.rect.topleft = [start_x, start_y]
