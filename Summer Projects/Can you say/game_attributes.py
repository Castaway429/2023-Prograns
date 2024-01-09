
# Import game engine
import pygame

# Bool to determine if screen should run
run = True

# Establish which screen we are going to be on
game_state = 0

#Define countdown variable for later use ;)
countdown = 3

# Solo Player Select Boolean
soloplay = False

# Multiplayer Select Boolean
multiplay = False

#Boolean to determine what game difficulty there will be

easy = False
normal = False
hard = False
extreme = False

# Initialize pygame
pygame.init()

# Initialize pygame music programs
pygame.mixer.init()

# Define the RGB value for our colors we want
white = (255, 255, 255)
blue = (0, 0, 128)
black = (0, 0, 0)

# Define our colors so that we can have a gradient

#Main Menu Colors for wavy effect

color1 = (73, 232, 255)  # Tealish color
color2 = (255, 186, 255)  # Magenta

#Game Mode Menu Colors
color3 = (188, 210, 255) 
color4 = (121, 255, 152)

# Define the transition duration and total duration
transition_duration = 5000  # Time in milliseconds for each transition
total_duration = 2 * transition_duration  # Total time for the full cycle

# Define the current color and timer variables
current_color = color1
timer = pygame.time.get_ticks()

# Set up the clock
clock = pygame.time.Clock()

# Screen Width and Height variables simplified
X = 800
Y = 600

# Create the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the pygame window name
pygame.display.set_caption('Can You Say...')

# Creates the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Renders main menu music file
MainMenuMusic = pygame.mixer.music.load("./Sounds/Can-You-Say-MainMenu.wav")

# Menu Select SFX
MenuSelect = "./Sounds/MenuSelect.wav"

# Game modes page Music
GameModeSelect = "./Sounds/GameModes.wav"

# Plays Music that's been loaded in, in this case, the MainMenuMusic
pygame.mixer.music.play(-1)

# Create a font object.
# 1st parameter is the font file
# which is present in our project folder.
# 2nd parameter is the size of the font
font = pygame.font.Font("./misc/PublicPixel-z84yD.ttf", 50)

# Creating text objects
# on which text is drawn on it.
text = font.render('Can You Say...', True, black)
Choose_Gamemode = font.render('Choose Gamemode:', True, black)
Choose_Difficulty = font.render('Game Difficulty:', True, black)

# Creating rectangular objects for the
# text surface object
textRect = text.get_rect()
chooseRect = Choose_Gamemode.get_rect()
diffRect = Choose_Difficulty.get_rect()

# Determine where on the screen the text will be
textRect.center = (X // 2, Y // 3)
chooseRect.center = (X // 1.97, Y // 4)
diffRect.center = (X // 1.97, 75)

# Create an object for the Start Button
StartBtn = pygame.image.load("./Images/StartButton.png").convert_alpha()

# Adjust the size of the image
StartBtn = pygame.transform.scale(StartBtn, (240, 100))

#Define the StartBtn rectangle property to detect clicks
StartBtn_rect = StartBtn.get_rect().move(X // 3, Y // 2)

# Start Button When Hovered over
HoveredStartBtn = pygame.transform.scale(StartBtn, (int(StartBtn.get_width() * 1.05), int(StartBtn.get_height() * 1.05)))

# Game Mode Buttons
#Buttons when they are idle
SoloBtn = pygame.image.load("./Images/Solo_Idle.PNG").convert()
MultiBtn = pygame.image.load("./Images/Multi_Idle.PNG").convert()

#Buttons when they are being hovered over
SoloBtn_Hover = pygame.image.load("./Images/Solo_Hover.PNG").convert()
MultiBtn_Hover = pygame.image.load("./Images/Multi_Hover.PNG").convert()

# Adjust the size of the image
SoloBtn = pygame.transform.scale(SoloBtn, (240, 200))
MultiBtn = pygame.transform.scale(MultiBtn, (240, 200))

#Hovered over image sizes
SoloBtn_Hover = pygame.transform.scale(SoloBtn_Hover, (240, 200))
MultiBtn_Hover = pygame.transform.scale(MultiBtn_Hover, (240, 200))

#Define the rectangle property for the player count to detect clicks
Solo_rect = SoloBtn.get_rect().move(X // 7.5, Y // 2.7)
Multi_rect = MultiBtn.get_rect().move(X // 1.8, Y // 2.7)

#Game Mode Difficulty Page Buttons
#If button has 1 that means its the default not being hovered
# if button has 2 that means it is the hover / click
#Whatever i decide

#Fetch the buttons
EasyBtn1 = pygame.image.load("./Images/EasyBtn1.PNG").convert_alpha()
EasyBtn2 = pygame.image.load("./Images/EasyBtn2.PNG").convert_alpha()

NormalBtn1 = pygame.image.load("./Images/Normal1.PNG").convert_alpha()
NormalBtn2 = pygame.image.load("./Images/Normal2.PNG").convert_alpha()

HardBtn1 = pygame.image.load("./Images/Hard1.PNG")
HardBtn2 = pygame.image.load("./Images/Hard2.PNG").convert_alpha()

#Make the gif work properly later 
#They do not work properly

ExtremeBtn1 = pygame.image.load("./Images/ExtremeButton1.gif").convert_alpha()
ExtremeBtn2 = pygame.image.load("./Images/ExtremeBtn2.gif").convert_alpha()

#Scale the buttons down

EasyBtn1 = pygame.transform.scale(EasyBtn1, (280, 150))
EasyBtn2 = pygame.transform.scale(EasyBtn2, (280, 150))

NormalBtn1 = pygame.transform.scale(NormalBtn1, (280, 150))
NormalBtn2 = pygame.transform.scale(NormalBtn2, (280, 150))

HardBtn1 = pygame.transform.scale(HardBtn1, (280, 150))
HardBtn2 = pygame.transform.scale(HardBtn2, (280, 150))

ExtremeBtn1 = pygame.transform.scale(ExtremeBtn1, (280, 150))
ExtremeBtn2 = pygame.transform.scale(ExtremeBtn2, (280, 150))

#Define the rect object for the buttons

Easy_rect = EasyBtn1.get_rect().move(X // 3.1, 130)
Normal_rect = NormalBtn1.get_rect().move(X // 3.1, 230)
Hard_rect = HardBtn1.get_rect().move(X // 3.1, 330)
Extreme_rect = ExtremeBtn1.get_rect().move(X // 3.1, 430)

# Function to check if mouse is hovering over image element
def is_hovering(mouse_pos, button_rect):
    return button_rect.collidepoint(mouse_pos)
