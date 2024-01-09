#################################################################
#                  Imports and impportant Bools
import pygame #Import game engine
pygame.display.set_caption('Movement Test') #Set the pygame window name
pygame.init() # Initialize pygame
pygame.mixer.init() #Initialize pygame music programs
clock = pygame.time.Clock() #Set up a clock

run = True #Game bool to run game
#################################################################

#################################################################
#                       Screen Variables
#Gets your monitors resolution size so that fullscreen can be complelety accurate
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
fullscreen = True #Defining our full screen bool
#Create the screen surface 
screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)

x, y = 800, 600 #Screen Width(x) and Height (y)

# Function to handle resizing the screen
def resize_screen(x, y):
    # Resize the screen surfaced
    screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)

#Room Number to decide what is rendered

RN = 1 #Room Number

# Max floor and walls

floor_count = 0
wall_count = 0

#################################################################

#################################################################
#                           Colors
black = (0, 0, 0)
white = (255, 255, 255)
#################################################################



#################################################################
#                           Fonts

TutorialFont = pygame.font.Font("./Movement Tests/Hey Comic.ttf", 50)

#################################################################

#################################################################
#                           Images

#Wall Images
wall_img = pygame.image.load("./Movement Tests/models/wall.PNG").convert()

#Floor Images
floor_img = pygame.image.load("./Movement Tests/models/floor.PNG").convert()

Floor = pygame.transform.scale(floor_img, (monitor_size[0], 70))

#Floor rect object
floor_rect = Floor.get_rect(bottom = monitor_size[1])

#Void if you touch you die / respawn
void_image = pygame.image.load("./Movement Tests/models/void.PNG").convert_alpha()
void = pygame.transform.scale(void_image, (monitor_size[0], 90))

#void object
void_rect = void.get_rect(bottom = monitor_size[1])

#Some platform image testing
platform_images = [
    pygame.image.load("./Movement Tests/models/floor.PNG").convert(),  # Floor Image
    pygame.image.load("./Movement Tests/models/wall.PNG").convert(),   # Wall Image
]

#Create sprite groups
f_platforms = pygame.sprite.Group() #Sprite list for floors floors
w_platforms = pygame.sprite.Group() #Sprite list for walls
player_group = pygame.sprite.Group() #Will group all player images together

#Door Images / Interactive Button
door_closed = pygame.image.load("./Movement Tests/models/door_closed.png").convert()
door_opened = pygame.image.load("./Movement Tests/models/door_opened.png").convert()
door_enter = pygame.image.load("./Movement Tests/models/door_enter.png").convert()
door_used = pygame.image.load("./Movement Tests/models/door_used.png").convert()

advance_pu = pygame.image.load("./Movement Tests/models/W_popup.png").convert_alpha()

#Player Images
p_idle = pygame.image.load("./Movement Tests/models/p_idle.png").convert_alpha()

#Walking and running
p_walkL = pygame.image.load("./Movement Tests/models/p_walkL.png").convert_alpha()
p_walkR = pygame.image.load("./Movement Tests/models/p_walkR.png").convert_alpha()

p_runL = pygame.image.load("./Movement Tests/models/p_runL.png").convert_alpha()
p_runR = pygame.image.load("./Movement Tests/models/p_runR.png").convert_alpha()

#Jumping and Landing
p_jump = pygame.image.load("./Movement Tests/models/p_jump.png").convert_alpha()
p_falling = pygame.image.load("./Movement Tests/models/p_falling.png").convert_alpha()

p_jumpRR = pygame.image.load("./Movement Tests/models/p_jumpRR.png").convert_alpha()
p_jumpRL = pygame.image.load("./Movement Tests/models/p_jumpRL.png").convert_alpha()

#landing
p_land = pygame.image.load("./Movement Tests/models/p_lan.png").convert_alpha()
#################################################################


class Player(pygame.sprite.Sprite):
    def __init__ (self, x, y, image):
        super().__init__()
        self.x = int(x)
        self.y = int(y)

        self.image = image  # Use the passed image argument
        self.rect = self.image.get_rect() #Create object
        self.mack = pygame.mask.from_surface(self.image) #Helps with collisions

        #Object Alignments
        self.rect.x = self.x 
        self.rect.y = self.y

        self.velX = 0 #X axis movement Value
        self.velY = 0 #Y axis movement (might remove)

        self.gravity = 0.6
        self.on_wall = False

        #Movement Options
        self.left = False
        self.right = False

        self.running = False
        
        self.jumping = False #Checks if player is ascending
        self.needtoland = True #Checks if the player is falling and needs to land

        self.speed = 4 #How fast player can move
        self.j_force = 12 #player jump force
    
    def draw (self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        dy = 0 #Dummy Y
        dx = 0 #Dummy X

        #Update if player moves horizontally
        if self.left and not self.right:
            if not self.running:
                self.image = p_walkL #Changes animation based on running or walking
            else:
                self.image = p_runL

            self.velX = -self.speed
        
        elif self.right and not self.left:

            
            if not self.running:
                self.image = p_walkR #Changes animation based on running or walking
            else:
                self.image = p_runR

            self.velX = self.speed
        elif not self.left and not self.right and not self.needtoland:

            self.velX = 0 #Stop player if no movements are made
            self.image = p_idle #Changes player image to default

        #Changes Speed due to Sprinting
        if self.running:
            self.speed = 8
        else:
            self.speed = 4

        #Controls Character Run Jump
        if self.jumping:
            if self.velY < 0: #Character is ascending
                if not self.left and not self.right:
                    self.image = p_jump

                elif self.left and not self.right:
                    self.velX = -(2.5 * self.speed) #If Character is walking (Left)
                    self.image = p_jumpRL
                    if self.running:
                        self.velX = -(2.1 * self.speed) #If Character is running (Left)
                        self.image = p_jumpRL

                elif self.right and not self.left:  #If Character is walking (Right)
                    self.velX = (2.5 * self.speed)
                    self.image = p_jumpRR
                    if self.running:                #If Character is running (Right)
                        self.velX = (2.1 * self.speed)
                        self.image = p_jumpRR
            else:
                self.image = p_falling
                self.needtoland = True
                self.jumping = False

        #Gravity for jumping
        self.velY += self.gravity
        if self.velY >= self.gravity:
            self.velY = self.gravity 



        #Collision Check (Floor Platforms)
        if pygame.sprite.spritecollide(self, f_platforms, False): #Rects Collide 
            self.velY = 0
            if self.needtoland:
                self.needtoland = False                                
            #Need X axis collision
        else:
            self.on_ground = False

        if pygame.sprite.spritecollide(self, w_platforms, False):
            self.on_wall = True
        
        #Move the player x value accordingly
        self.rect.x += self.velX
        
        #Move the player object according to the new values
        self.rect = self.image.get_rect().move(self.rect.x, self.rect.y)
    
    #This part propels the character in the air
    def jump(self):
        if self.on_ground:
            if not self.left and not self.right: #If character isn't moving
                self.velY = -(self.j_force * 1.5) #Jumps slightly higher
            else:
                self.velY = -self.j_force
           
            self.jumping = True
            self.needtoland = True
            self.on_ground = False


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(x, y, width, height)
