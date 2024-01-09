import pygame

#Our player class
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64)) #Size of our player
        self.image.fill('blue') #Player's color
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0) #How the player moves on a coordinate scale
        self.speed = 5 #Multiplies with the direction of the player to give it a sense of moving

        #Will adjust the speeds at a later date

        #Now we need to make some player Stats
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        #Going right to left
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        #Going up or down
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self):
        self.get_input()


#Our Zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64)) #Zombie size
        self.image.fill('green') #Zombie's colors are green
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0) #How the zombie will move on a coordinate
        self.speed = 3 #Multiplies when the direction is moving


        