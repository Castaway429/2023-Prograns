import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect().move(pos)

    def update(self,x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift

class KillBlock(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect().move(pos)

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift