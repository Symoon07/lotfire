import pygame
import sys

class Player:
    def __init__ (self, screen, height, width):
        self.sprite = pygame.image.load("../assets/intro_ball.gif")
        self.rect = self.sprite.get_rect()
        self.height = height
        self.width = width
        self.speed = [0, 0]
        self.screen = screen

    def update (self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "w":
                    self.speed[1] = -1
                elif event.unicode == "a":
                    self.speed[0] = -1
                elif event.unicode == "s":
                    self.speed[1] = 1
                elif event.unicode == "d":
                    self.speed[0] = 1
            elif event.type == pygame.KEYUP:
                if event.unicode == "w" or event.unicode == "s":
                    self.speed[1] = 0
                elif event.unicode == "a" or event.unicode == "d":
                    self.speed[0] = 0

        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height

        self.screen.blit(self.sprite, self.rect)
