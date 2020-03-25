import sys, pygame
import random
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)

ball_image = pygame.image.load("ball.png")
ball_image = pygame.transform.smoothscale(ball_image, (30, 30))
ball_rect = ball_image.get_rect()
ball_rect.center = (width//2, height//2)
speed = pygame.math.Vector2(0, 5)
speed.rotate_ip(random.randint(0, 360))



def main():
    while True:
        clock.tick(60)
        move_ball()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)
        pygame.display.flip()

if __name__ == '__main__':
    main()

