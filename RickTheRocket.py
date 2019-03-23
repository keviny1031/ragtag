#RickTheRocket
#Team RagTag's MHV Project


###IMPORTS###
from pygame import *
#Pygame
from math import *
#Math
from random import *
#Random
#############


###INITIALIZING###
init()
size=(960,720)
screen=display.set_mode(size)
fps=time.Clock()
display.set_caption("Rick The Rocket")
xSpeed = 0
ySpeed = 0
angle = 45
launchSpeed = 5
maxJumps = 1
curJumps = maxJumps
onGround = True
GRAVITY = 1
xPos = 0
yPos = 0
##################

def jump():
    #Jumps based on the current angle of the rocket
    global onGround
    global curJumps
    global ySpeed
    global xSpeed
    if curJumps > 0:
        onGround = False
        curJumps -= 1
        ySpeed -= launchSpeed * 10 * round(sin(angle + (pi / 2)), 10) #Minus for PyGame heights being inverted
        xSpeed += launchSpeed * round(cos(angle + (pi / 2)), 10)

def menu():
    global xPos
    global yPos
    global xSpeed
    global ySpeed
    global onGround
    global launchSpeed
    running = True
    fps = time.Clock()
    
    while running:
        print(round(sin(angle + (pi / 2)), 10), xPos, yPos)
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
            if evnt.type == KEYDOWN:
                if evnt.key == K_SPACE:
                    jump()
        
        keys = key.get_pressed()
        if keys[K_UP]:
            chary -= 0.25
        if keys[K_DOWN]:
            chary += 0.25
        if keys[K_RIGHT] and (charx + 50) < 960:
            charx += 0.25
        if keys[K_LEFT] and charx > 0:
            charx -= 0.25

        xPos += xSpeed
        yPos += ySpeed
        
        if yPos >= 0:
            onGround = True
            ySpeed = 0
            yPos = 0
            
        if onGround:
            refreshJumps()
            xSpeed = 0
            ySpeed = 0
        else:
            ySpeed += GRAVITY
    
def refreshJumps():
    global maxJumps
    global curJumps
    curJumps = maxJumps
    

page = "menu"
while page != "quit":
    if page == "menu":
        page = menu()

    


quit()
