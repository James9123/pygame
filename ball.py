import pygame, random

class Ball:
    def __index__(self):
        self.image = pygame.image.load("ball.png")
        scale = random.randint(1, 5) * 10
        self.image = pygame.transform.smoothscale(self.image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(2, 5))

    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > screen_info.current_w:
            speed[0] *= -1
            self.rect.move_ip(speed[0], 0)
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
            speed[1] *= -1
            self.rect.move_ip(0, speed[1])