import sys, pygame
pygame.init()

size = width, height = 1366, 630
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("../assets/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            if event.unicode == "w":
                speed[1] = -1
            elif event.unicode == "a":
                speed[0] = -1
            elif event.unicode == "s":
                speed[1] = 1
            elif event.unicode == "d":
                speed[0] = 1
        elif event.type == pygame.KEYUP:
            if event.unicode == "w" or event.unicode == "s":
                speed[1] = 0
            elif event.unicode == "a" or event.unicode == "d":
                speed[0] = 0
    ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
