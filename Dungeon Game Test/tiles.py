import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect().move(pos)

class Door(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size * 3, size))
        self.image.fill('brown')
        self.rect = self.image.get_rect().move(pos)


class SideDoor(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size * 2))
        self.image.fill('brown')
        self.rect = self.image.get_rect().move(pos)


class Wall(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('darkgrey')
        self.rect = self.image.get_rect().move(pos)

class InvWall(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect().move(pos)

class TestDialouge(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.name = "test"
        self.image.fill('green')
        self.rect = self.image.get_rect().move(pos)


        