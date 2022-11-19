import sys, pygame

from src.player import Player


def main ():
    pygame.init()

    size = width, height = 800, 800
    speed = [0, 0]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    player = Player(screen, width, height)
    player1 = Player(screen, width, height)

    while True:
        screen.fill(black)

        player.update(pygame.event.get())
        player1.update(pygame.event.get())

        pygame.display.flip()


if __name__ == "__main__":
    main()
