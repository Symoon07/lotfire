import os
import random
import pygame as pg

from src.player import Player
from src.log import Log

RED = pg.Color('red')
clock = pg.time.Clock()
FPS = 120


def main ():
    pg.init()

    bg = pg.image.load(os.path.join('../assets', 'bg.png'))
    width, height = bg.get_width(), bg.get_height()

    world = pg.display.set_mode([width, height])

    objects = pg.sprite.Group()

    speed = 5
    player = Player()
    objects.add(player)

    tick = 0
    while True:
        if tick % 500 == 0:
            l = Log()
            l.move(random.randint(0, 894), random.randint(0, 570))
            objects.add(l)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == ord('w'):
                    player.control(0, -speed)
                if event.key == ord('s'):
                    player.control(0, speed)
                if event.key == ord('a'):
                    player.control(-speed, 0)
                if event.key == ord('d'):
                    player.control(speed, 0)
            if event.type == pg.KEYUP:
                if event.key == ord('w'):
                    player.control(0, speed)
                if event.key == ord('s'):
                    player.control(0, -speed)
                if event.key == ord('a'):
                    player.control(speed, 0)
                if event.key == ord('d'):
                    player.control(-speed, 0)

        world.blit(bg, world.get_rect())
        player.update()
        objects.draw(world)
        pg.display.flip()
        clock.tick(FPS)
        tick += 1


if __name__ == "__main__":
    main()

