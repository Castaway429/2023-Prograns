import pygame

#A wait function in seconds
def wait(s):
    time = s * 1000
    pygame.time.wait(time)

#Will change to have this fit our screen but we want this up and running
screen_width = 1200
screen_height = 600

#How big our tiles will be
tile_size = 64

rooms = [
[ #Outside Entrance
'WWWWWWWWD  WWWWWWWWW',
'WXXXXXXWXXXWXXXXXXXW',
'WXXXXXXWXXXWXXXXXXXW',
'WXXXXXXWXXXWXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXPXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'IXXXXXXXXXXXXXXXXXXI',
'IIIIIIIIIIIIIIIIIIII',
], 

[ #Main hall
'WWWWWWWWWWWWWWWWWWWW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'dXXXXXXXXTXXXXXXXXXd',
' XXXXXXXXXXXXXXXXXX ',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXPXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WWWWWWWWD  WWWWWWWWW',
],

[ #Second Room
'WWWWWWWWWWWWWWWWWWWW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXd',
'WXXXXXXXXXXXXXXPXXX ',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WWWWWWWWWWWWWWWWWWWW',
],
[ #Third Room (chest room)
'WWWWWWWWWWWWWWWWWWWW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'dXXXXXXXXXXXXXXXXXXW',
' XXPXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WXXXXXXXXXXXXXXXXXXW',
'WWWWWWWWWWWWWWWWWWWW',
],

]

# A Dictionary of what room leads to what new room and loads the map
door_mappings = {
    0:  # Entry Room
    {
        (512, 0): 1        
    },
    
    1:  # Main entry
    {
        (512, 512): 0,
        (0, 192): 2,
        (1216, 192): 3        
    },
    
    2: # Left Room
    {
        (1216, 192): 1
    },

    3: # Right Room
    {
        (0, 192): 1
    },
    # Add more door-room mappings as needed
}

# REMEMBER HOW WE GET X AND Y

# x = col_index * tile_size 
# y = row_index * tile_size

#A dictionary of what room we came out of changes our spawn from where we are coming from
room_spawns = {

    0: #Coming from room 0
    {
        1: (576, 384) #Going to 1 then new spawn is the in the parenthesis
    },

    1: #Coming from room 1
    {
        0:(576, 128), #Going to 0 then new spawn is the in the parenthesis
        2:(1140, 224), #Going to Room 2 then new spawn is the in the parenthesis
        3:(100, 224) #Going to Room 3 then new spawn is the in the parenthesis
    },

    2: #Coming from room 2
    {
        1:(100, 224) #Going to 1 then new spawn is the in the parenthesis
        #This is the coords of the door so lets see
    },

    3: #Coming from room 3
    {
        1:(1140, 224) #Going to 1 then new spawn is the in the parenthesis
    }


}


#If a room has enemies this is how they will be rendered. There will be the name like "Zombie" then the count after.
#Then I want them to randomly on any X tile be spawned.
room_enemy_count = {
    3: # Right Room
    {
        "Zombie": 10
    },
    # Add more door-room mappings as needed
}


#A dictionary of what a character is supposed to say based on what room they are in. Also takes into account their custom name given.
room_dialouge = {

    1: #First room
    {
        "test": "Hello! I'm just a path of grass!"
    }
}