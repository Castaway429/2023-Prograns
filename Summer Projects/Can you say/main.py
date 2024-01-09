import pygame
from playsound import playsound
from game_attributes import *

while run:
    if game_state == 0:
        # Get and print the x and y coordinates of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - timer

        # Calculate the progress within the total duration
        progress = (elapsed_time % total_duration) / total_duration

        # Reverse the progress if it's in the second half of the cycle
        if progress >= 0.5:
            progress = 1.0 - progress

        # Interpolate between color1 and color2
        r = int(color1[0] + (color2[0] - color1[0]) * progress)
        g = int(color1[1] + (color2[1] - color1[1]) * progress)
        b = int(color1[2] + (color2[2] - color1[2]) * progress)

        # Set the current color
        current_color = (r, g, b)

        # Fill the screen with the current color
        screen.fill(current_color)

        # Copying the text surface object
        # to the display surface object
        # at the center coordinate.
        screen.blit(text, textRect)

        # Check if the mouse is hovering over the image and resize accordingly
        if is_hovering(mouse_pos, StartBtn_rect):
            current_image = HoveredStartBtn
        else:
            current_image = StartBtn

        # Using blit to copy content from one surface to another
        screen.blit(current_image, (X // 3, Y // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_hovering(mouse_pos, StartBtn_rect):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(GameModeSelect)
                        playsound(MenuSelect)
                        pygame.mixer.music.play(-1)
                        game_state = 1

    if game_state == 1:

        #Define the mouse position on screen
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - timer

        # Calculate the progress within the total duration
        progress = (elapsed_time % total_duration) / total_duration

        # Reverse the progress if it's in the second half of the cycle
        if progress >= 0.5:
            progress = 1.0 - progress

        # Interpolate between color1 and color2
        r = int(color3[0] + (color4[0] - color3[0]) * progress)
        g = int(color3[1] + (color4[1] - color3[1]) * progress)
        b = int(color3[2] + (color4[2] - color3[2]) * progress)

        # Set the current color
        current_color = (r, g, b)

        #Background color of the window
        screen.fill(current_color)

        #Title text for game window
        screen.blit(Choose_Gamemode, chooseRect)

        # Check if the mouse is hovering over the SoloBtn
        if is_hovering(mouse_pos, Solo_rect):
            current_Solo = SoloBtn_Hover
        else:
            current_Solo = SoloBtn

        #Check if the mouse is hovering over the MultiBtn
        if is_hovering(mouse_pos, Multi_rect):
            current_Multi = MultiBtn_Hover
        else:
            current_Multi = MultiBtn

        screen.blit(current_Solo, (X // 7.5, Y // 2.7))
        screen.blit(current_Multi, (X // 1.8, Y // 2.7))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
                    mouse_pos = pygame.mouse.get_pos()

                    # If mouse is hovering over Solo button and clicks on it
                    if is_hovering(mouse_pos, Solo_rect):
                        playsound(MenuSelect)
                        game_state = 2
                        soloplay = True

                    # If mouse is hovering over Multi button and clicks on it
                    if is_hovering(mouse_pos, Multi_rect):
                        playsound(MenuSelect)
                        game_state = 2
                        multiplay = True

    if game_state == 2:

        #Define the mouse position variable
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - timer

        # Calculate the progress within the total duration
        progress = (elapsed_time % total_duration) / total_duration

        # Reverse the progress if it's in the second half of the cycle
        if progress >= 0.5:
            progress = 1.0 - progress

        # Interpolate between color3 and color4
        r = int(color3[0] + (color4[0] - color3[0]) * progress)
        g = int(color3[1] + (color4[1] - color3[1]) * progress)
        b = int(color3[2] + (color4[2] - color3[2]) * progress)

        # Set the current color
        current_color = (r, g, b)

        #Background color of the window
        screen.fill(current_color)

        #Title text 
        screen.blit(Choose_Difficulty, diffRect)

        # Each of these change the image source if hovered over
        if is_hovering(mouse_pos, Easy_rect):
            current1_image = EasyBtn2
        else:
            current1_image = EasyBtn1
        
        if is_hovering(mouse_pos, Normal_rect):
            current2_image = NormalBtn1
        else:
            current2_image = NormalBtn2

        if is_hovering(mouse_pos, Hard_rect):
            current3_image = HardBtn1
        else:
            current3_image = HardBtn2
        
        if is_hovering(mouse_pos, Extreme_rect):
            current4_image = ExtremeBtn1
        else:
            current4_image = ExtremeBtn2

        #Buttons being added to the page      
        screen.blit(current1_image, (X // 3.1, 130))
        screen.blit(current2_image, (X // 3.1, 230))
        screen.blit(current3_image, (X // 3.1, 330))
        screen.blit(current4_image, (X // 3.1, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
                    mouse_pos = pygame.mouse.get_pos()

                if is_hovering(mouse_pos, Easy_rect):
                        playsound(MenuSelect)
                        game_state = 3
                        easy = True
                        pygame.mixer.music.stop()

                if is_hovering(mouse_pos, Normal_rect):
                        playsound(MenuSelect)
                        game_state = 3
                        easy = True
                        pygame.mixer.music.stop()

                if is_hovering(mouse_pos, Hard_rect):
                        playsound(MenuSelect)
                        game_state = 3
                        easy = True
                        pygame.mixer.music.stop()

                if is_hovering(mouse_pos, Extreme_rect):
                        playsound(MenuSelect)
                        game_state = 3
                        easy = True
                        pygame.mixer.music.stop()

    if game_state == 3:
    
        if (soloplay):
            UserScore = 1000 # The individual user score

        #Need to define a function that checks
        #the amount of players in multiplayer
        #then creates there own scores individually
        
        # Defines the mouse position on the screen as a variable
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - timer

        # Calculate the progress within the total duration
        progress = (elapsed_time % total_duration) / total_duration

        # Calculate the progress within the total duration
        if progress >= 0.5:
            progress = 1.0 - progress

        # Interpolate between color3 and color4
        r = int(color3[0] + (color4[0] - color3[0]) * progress)
        g = int(color3[1] + (color4[1] - color3[1]) * progress)
        b = int(color3[2] + (color4[2] - color3[2]) * progress)

        #Set the current color RGB values as r, g, b described above
        current_color = (r, g, b)

        # The color of the screen background
        screen.fill(current_color)
        
        clock.tick(1)  # Delay for 1 second

        #A counter to show on screen
        #for the user to get ready for a challenge

        #move this countdown to later inside the games
        if countdown > 0:

            if countdown == 3:
                state = "Ready..."
            elif countdown == 2:
                state = "Set..."
            elif countdown == 1:
                state = "Go!!"

            countdown -= 1 # Reduces countdown variable every loop


            # Renders all the text after the loop
            #State is defined earlier on and is changed based
            #on the counter
            Display = font.render(state, True, black)
            displayRect = Display.get_rect()
            displayRect.center = (X // 2, Y // 3)
            screen.blit(Display, displayRect)

        pygame.display.update()  # Update the screen
        #Handles all hardware events
        for event in pygame.event.get():
            #Handles if the game detects the X button being pressed
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.quit()
