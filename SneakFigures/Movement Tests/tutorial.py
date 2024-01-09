import pygame
from attributes import *

pygame.init()

#Initizle what the Player Class is
player = Player(300, 700, p_idle)

#Initilize Platform class
platforms = Platform(0, 0, 0, 0, platform_images[0])

#Find mouse position
m = pygame.mouse.get_pos()

#Add instances to groups
player_group.add(player)

f_platforms.add(platforms)

while run:

    #Game Logic Here

    #initilize single key presses:
    keys = pygame.key.get_pressed()

    #Keep player in the borders of the window on the left side
    if player.rect.x <= -50:
        player.rect.x = -50

    #Floor collison

    #Wall Collision Code Here

    #A grippier variation to climb on.

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #Press X button
            pygame.quit() #Stops pygame
            run = False # Stopes the game

        elif event.type == pygame.KEYDOWN:
            # Toggle full screen on F11 key press
            if event.key == pygame.K_ESCAPE: #Escape key
                pygame.quit() #Stops pygame
                run = False #Stops running loop

            #Might removed Coming out of fullscreen
            elif event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    #Sets to full screen
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    #Sets to a resizeable screen
                    screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)

            #Player Movement
            if event.key == pygame.K_a:
                player.left = True
                
            if event.key == pygame.K_d:
                player.right = True

            if event.key == pygame.K_LSHIFT:
                player.running = not player.running

            if event.key == pygame.K_RSHIFT:
                player.running = not player.running

            if event.key == pygame.K_SPACE:
                player.jump()


        elif event.type == pygame.KEYUP:

            #Player Movement
            if event.key == pygame.K_a:
                player.left = False

            if event.key == pygame.K_d:
                player.right = False

            
        
        #elif event.type == pygame.VIDEORESIZE:
        #    if not fullscreen: #Only activates when the game isn't fullscreen 
        #        # Resize screen on window resize event
        #        x, y = event.w, event.h
        #        resize_screen(x, y)

    if RN == 1:
        # Clear the screen
        screen.fill((white))


        f_platforms.empty() #Clear to stop lag
        
        #Render Floor
        floor_data = [
            (0, monitor_size[1] - 70, monitor_size[0], 600)
        ]
  
        #Renders floors
        for floor in floor_data:
            platform_image = platform_images[0]
            
            # Extract the width and height from the data tuple
            x, y, width, height = floor

            # Scale the platform image based on the width and height
            platform_image = pygame.transform.scale(platform_image, (width, height))
            
            # Create the Platform object with the scaled image and other data
            platform = Platform(x, y, width, height, image=platform_image)
            
            f_platforms.add(platform)

        # Update and draw the platforms
        for platform in f_platforms:
            screen.blit(platform.image, platform.rect.topleft)

        #Add text to the screen
        txt = TutorialFont.render('Use A & D to move and Shift To Toggel Sprint', True, black)
        txtRect = txt.get_rect()

        txtRect.center = (750, 500)

        screen.blit(txt, txtRect)

        #Exit Door rect objects and positon
        door_o_rect = door_opened.get_rect(x=1030, y=654)
        door_e_rect = door_enter.get_rect(x=1030, y=654)

        #Advance Pop Up Rect object
        pu_rect = advance_pu.get_rect(x=(player.rect.x + 10), y=(player.rect.y - 100))

        #Checks if the player is touching the door
        if player.rect.colliderect(door_o_rect):
            doorState = door_enter
            doorStateRect = door_e_rect
            screen.blit(doorState, doorStateRect)
            screen.blit(advance_pu, pu_rect)

             # Check if the "W" key is pressed
            if keys[pygame.K_w]:
                print("Advanced!")
                player.rect.x = 0
                player.rect.y = 400
                player.velY = 0 #So game doesn't think player is still jumping / falling
                RN += 1
                
        else:
            doorState = door_opened
            doorStateRect = door_o_rect
            screen.blit(doorState, doorStateRect)

        # Draw player to the screen
        player.draw(screen)

    elif RN == 2:

        #Screen background
        screen.fill(white)

       # if (530 < player.rect.x < 940):
       #     player.on_ground = False

        #Exit Door rect objects and positon
        door_o_rect = door_opened.get_rect(x=1300, y=360)
        door_e_rect = door_enter.get_rect(x=1300, y=360)

        #Door you entered in
        door_u_rect = door_used.get_rect(x=30, y=360)

        #Advance Pop Up Rect object
        pu_rect = advance_pu.get_rect(x=(player.rect.x + 10), y=(player.rect.y - 100))

        #Add text to the screen
        txt = TutorialFont.render('Press Space to Jump (Using Shift makes jumps longer)', True, black)
        txtRect = txt.get_rect()

        txtRect.center = (800, 300)

        screen.blit(txt, txtRect)

        #Void that if you touch you and fall you go back to the top
        screen.blit(void, void_rect)

        #If player touches the void they are sent back to the beginning
        if player.rect.colliderect(void_rect):
            player.rect.x = 0
            player.rect.y = 405
            player.velY = 0 #So game doesn't think player is still jumping / falling

        f_platforms.empty() #Clear to stop lag

        floor_data = [
            (0, 500, 550, 600),

            (1000, 500, 550, 600),
        ]
  
        #Renders floors
        for floor in floor_data:
            platform_image = platform_images[0]
            
            # Extract the width and height from the data tuple
            x, y, width, height = floor

            # Scale the platform image based on the width and height
            platform_image = pygame.transform.scale(platform_image, (width, height))
            
            # Create the Platform object with the scaled image and other data
            platform = Platform(x, y, width, height, image=platform_image)
            
            f_platforms.add(platform)

        # Update and draw the platforms
        for platform in f_platforms:
            screen.blit(platform.image, platform.rect.topleft)

        #Add doors to the screen
        screen.blit(door_used, door_u_rect)

        #Checks if the player is touching the door
        if player.rect.colliderect(door_o_rect):
            doorState = door_enter
            doorStateRect = door_e_rect
            screen.blit(doorState, doorStateRect)
            screen.blit(advance_pu, pu_rect)

             # Check if the "W" key is pressed
            if keys[pygame.K_w]:
                f_platforms.empty() #Clear to stop lag
                player.rect.x = 0
                player.rect.y = 600
                player.velY = 0
                player.on_ground = False
                RN += 1
                
        else:
            doorState = door_opened
            doorStateRect = door_o_rect
            screen.blit(doorState, doorStateRect)
    
        # Draw the player on screen
        player.draw(screen)

    elif RN == 3:

        #Make screen blank
        screen.fill(white)

        f_platforms.empty() #Stops lag
        w_platforms.empty() 

        #Create some floors
        floor_data = [
            (0, 700, 2000, 300),
           (1000, 400, 700, 300),     
        ]

        wall_data = [
            (1000, 400, 10, 300),    
        ]   


        #Renders floors
        for data in floor_data:
            platform_image = platform_images[0]
            
            # Extract the width and height from the data tuple
            x, y, width, height = data

            # Scale the platform image based on the width and height 
            platform_image = pygame.transform.scale(platform_image, (width, height))
            
            # Create the Platform object with the scaled image and other data
            platform = Platform(x, y, width, height, image=platform_image)
            
            f_platforms.add(platform)

        #Render Walls
        for data in wall_data:
            platform_image = platform_images[1]
            
            # Extract the width and height from the data tuple
            x, y, width, height = data

            # Scale the platform image based on the width and height 
            platform_image = pygame.transform.scale(platform_image, (width, height))
            
            # Create the Platform object with the scaled image and other data
            platform = Platform(x, y, width, height, image=platform_image)
            
            w_platforms.add(platform)

        # Update and draw the platforms
        for platform in f_platforms:
            screen.blit(platform.image, platform.rect.topleft)

        for platform in w_platforms:
            screen.blit(platform.image, platform.rect.topleft)

        #Draws player on the screen
        player.draw(screen)

    #Update game every 60ms
    pygame.display.update()
    player.update()
    clock.tick(60)