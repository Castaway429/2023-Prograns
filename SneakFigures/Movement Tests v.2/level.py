import pygame
from tiles import Tile, KillBlock
from settings import tile_size, screen_width, screen_height
from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)

        self.world_shift = 0
        self.vertical_shift = 0

        self.playerspawn_x = 0 #Where the player will respawn if they fall and die
        self.playerspawn_y = 0 #Player spawn y axis

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.kill_blocks = pygame.sprite.Group()

        for row_index,row in enumerate(layout): #Gets the rows from the level layout
            # print(row)  ROW DATA          
            # print(row_index) WHERE YOU CAN FIND THE ROW
            for col_index, cell in enumerate(row): #Gets every element in each row
                # print(f'{row_index},{col_index}:{cell}') #See every individual cell
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == "X":
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == "K":
                    kill_block = KillBlock((x,y), tile_size)
                    self.kill_blocks.add(kill_block)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx #Player X coordinate
        direction_x = player.direction.x #What direction player is going to move in

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < screen_height / 4 and direction_y < 0:
            self.vertical_shift = 16 #Player going up
            player.direction.y = 0

        elif player_y > screen_height - (screen_height / 4) and direction_y > 0:
            if player.state != "dead":
                self.vertical_shift = -16 #Player falling down
                player.direction.y = 0

        else:
            self.vertical_shift = 0
            player.speed = 8

#Collision are VERY jank and need fixing
    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed #Player movement

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #Collision with a ground object
                if player.direction.x < 0: #If player is moving left
                    player.rect.left = sprite.rect.right #Puts the player on the left of the object
                elif player.direction.x > 0: #If player is moving right
                    player.rect.right = sprite.rect.left #Puts the player on the right of the object

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect): #Collision with a ground object
                
                if player.direction.y > 0: #If player is falling
                    player.rect.bottom = sprite.rect.top #Puts the player on the left of the object
                    player.direction.y = 0 #Basically player.on_ground = true

                elif player.direction.y < 0: #If player bumping head on something
                    player.rect.top = sprite.rect.bottom #Puts the player on the right of the object
                    player.direction.y = 1 #Basically player.on_ground = true

        for sprite in self.kill_blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                player.death()

    def run(self):
        #Level Tiles
        self.tiles.update(self.world_shift, self.vertical_shift) #This variable changes the level being able to scroll
        self.tiles.draw(self.display_surface)

        self.kill_blocks.update(self.world_shift, self.vertical_shift)
        self.kill_blocks.draw(self.display_surface)

        self.scroll_x() #Helps screen scrolling
        self.scroll_y() #Scrolls up or down

        #Player 
        self.player.update() #Update player position
        self.horizontal_movement_collision() #Player movement
        self.vertical_movement_collision() #Player verical collisions
        self.player.draw(self.display_surface)
        