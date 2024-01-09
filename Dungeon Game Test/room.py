#What our current room is
current_room_index = 0
#What room we came out of. Set to none because at the start of the game we come out of no room we simply spawn in.
prev_room_index = None

import pygame
from player import *
from tiles import *

#Get all out map details
from maps import *


class Room:
     
    def __init__(self,level_data,surface):

        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data) #Level data is from our map.py

        #What type of room where are in and where we're going

    def setup_level(self,layout):
        
        self.dialouge_bar = pygame.sprite.GroupSingle()
        #Entity Sprites
        self.player = pygame.sprite.GroupSingle()
        self.zombie = pygame.sprite.Group()
        #Floor blocks
        self.tiles = pygame.sprite.Group()
        #Door Block
        self.door_blocks = pygame.sprite.Group()
        self.side_door_blocks = pygame.sprite.Group()
        #Wall blocks
        self.wall_blocks = pygame.sprite.Group()
        self.invis_wall_blocks = pygame.sprite.Group()
        #Test block for dialouge
        self.test_blocks = pygame.sprite.Group()

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
                    tile = Tile((x,y),tile_size)

                    self.tiles.add(tile)
                    self.player.add(player_sprite)

                if cell == "W":
                    wall = Wall((x,y), tile_size)
                    self.wall_blocks.add(wall)
                if cell == "D":
                    door = Door((x,y), tile_size)
                    self.door_blocks.add(door)
                if cell == "d":
                    side_door = SideDoor((x,y), tile_size)
                    self.side_door_blocks.add(side_door)
                if cell == "I":
                    invis_wall = InvWall((x,y), tile_size)
                    self.invis_wall_blocks.add(invis_wall)


                    #Test Block
                if cell == "T":
                    test_block = TestDialouge((x,y), tile_size)
                    self.test_blocks.add(test_block)
                
    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed #Player movement
            
        #Wall collision + Invisible wall collision
        for sprite in self.wall_blocks.sprites() + self.invis_wall_blocks.sprites():
            if sprite.rect.colliderect(player.rect): #Collision with a ground object
                print("Colliding with wall!")
                if player.direction.x < 0: #If player is moving left
                    player.rect.left = sprite.rect.right #Puts the player on the left of the object
                elif player.direction.x > 0: #If player is moving right
                    player.rect.right = sprite.rect.left #Puts the player on the right of the object

    def vertical_movement_collision(self):
        player = self.player.sprite

        player.rect.y += player.direction.y * player.speed #Player Movement

        #Wall collision + Invisible wall collision
        for sprite in self.wall_blocks.sprites() + self.invis_wall_blocks.sprites():
            if sprite.rect.colliderect(player.rect): #Collision with a ground object
                print("Colliding with wall!")
                if player.direction.y > 0: #If player is going down
                    player.rect.bottom = sprite.rect.top #Puts the player on the left of the object
                    player.direction.y = 0 #Stops player from moving

                elif player.direction.y < 0: #If player bumping head on something
                    player.rect.top = sprite.rect.bottom #Puts the player on the right of the object
                    player.direction.y = 0 #Stops player from moving

    def door_collision(self):
        #Door Block Collision
        
        #Need like a new type of class that manages all the doors in every place and if you go to a certain place
        #It will take you to a certain screen type of thing
        player = self.player.sprite
        for sprite in self.door_blocks.sprites() + self.side_door_blocks.sprites():
            
            if sprite.rect.colliderect(player.rect):
                sprite.image.fill('black')
                # Create an instance // Routing System for door
                self.changeRoom(sprite.rect.x, sprite.rect.y)
            else:
                sprite.image.fill('brown')

    def player_Dialouge(self):
        player = self.player.sprite

        for sprite in self.test_blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                #Get the sprite name
                name = sprite.name
                
                dialouge = room_dialouge.get(current_room_index, {}).get((name))
                print(dialouge)
                self.dialouge_bar.draw(self.display_surface)
                
    def update_level(self, new_level_data):
        self.level_data = new_level_data
        self.setup_level(new_level_data)

    def changeRoom(self, doorX, doorY):
            #Some testing things
            #print("Changing room")
            #print(f"Door X: {doorX}, Door Y: {doorY}")

            #Checks if there is any room you're coming from
            if (prev_room_index == None):
                print("|| This is the first room you're going to !! ||")
            else:
                print(f"Previous Room: {prev_room_index}")
            
            print("--------------------------------------------------------------")
            print(f"Current room index: {current_room_index}")
            print(f"Door coordinates: ({doorX}, {doorY})")
            print(f"Door mappings for current room: {door_mappings.get(current_room_index, {})}")

            target_room = door_mappings.get(current_room_index, {}).get((doorX, doorY))

            if target_room is not None:
                print(f"Going to room {target_room}")
                #Updates level
                self.update_level(rooms[target_room])
                #Updates the room index
                self.update_room_index(target_room)
                #Update where the player will spawn
                self.set_Player_Spawn()
            else:
                print(f"No room found for door coordinates ({doorX}, {doorY})")

            
            print("--------------------------------------------------------------")
            print("")

    def update_room_index(self, new_room_index):
        #Import our current and prev room index
        global current_room_index, prev_room_index

        #Previous Rooms value is now current room
        prev_room_index = current_room_index
        #Current Rooms Value is now the new room
        current_room_index = new_room_index

    def set_Player_Spawn(self):
        spawn = room_spawns.get(prev_room_index, {}).get((current_room_index))

        if spawn is not None:
            print(f"Your new spawn would be: {spawn}")
            player = self.player.sprite
                
            player.rect.x = spawn[0]
            player.rect.y = spawn[1]
        else:
            print(f"There are no spawn locations for room {current_room_index}")

    def run(self):
        player = self.player.sprite
        #Level Tiles
        self.tiles.draw(self.display_surface) 
        self.wall_blocks.draw(self.display_surface)
        self.invis_wall_blocks.draw(self.display_surface)
        self.door_blocks.draw(self.display_surface)
        self.side_door_blocks.draw(self.display_surface)

        self.test_blocks.draw(self.display_surface)


        #Player Movement / Collisions
        self.player.update() #Update player position
        self.horizontal_movement_collision() #Player movement (x axis) with collisions
        self.vertical_movement_collision() #Player movement (y axis) with collisions
        self.door_collision()#Trying to fix something
        self.player_Dialouge() #See what dialouge something says on collision
        self.player.draw(self.display_surface)
        
        #Enemy functions

        


