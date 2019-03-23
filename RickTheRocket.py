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
font = font.SysFont('Arial', 30)
display.set_caption("Rick The Rocket")
CHARRAD = 22
angle = 0
ang1 = pi/4
ang2 = 3 * pi / 4
launchSpeed = 11
maxJumps = 4
curJumps = maxJumps
onGround = True
GRAVITY = 0.38
xSpeed = 0
ySpeed = 0
xPos = 0
yPos = 720 - CHARRAD
sprite = transform.scale(image.load("main1.png"), (40,40))
##################

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def jump():
    #Jumps based on the current angle of the rocket
    global onGround
    global curJumps
    global ySpeed
    global xSpeed
    if curJumps > 0:
        if round(sin(angle + (pi / 2)), 10) > 0:
            ySpeed = 0
        xSpeed = 0
        onGround = False
        curJumps -= 1
        ySpeed -= launchSpeed * round(sin(angle + (pi / 2)), 10) #Minus for PyGame heights being inverted
        xSpeed += launchSpeed * round(cos(angle + (pi / 2)), 10)#Rounds to avoid a pi decimal error



def game():
    global xPos
    global yPos
    global xSpeed
    global ySpeed
    global onGround
    global launchSpeed
    global angle
    global ang1
    global ang2
    running = True
    fps = time.Clock()
    
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
            if evnt.type == KEYDOWN:
                if evnt.key == K_SPACE:
                    jump()
        print(xPos, yPos)
        keys = key.get_pressed()
        if keys[K_LEFT]:
            angle += 0.05
            ang1 += 0.05
            ang2 += 0.05
        elif keys[K_RIGHT]:
            angle -= 0.05
            ang1 -= 0.05
            ang2 -= 0.05
        
        xPos += xSpeed
        yPos += ySpeed
        
        if yPos >= 700 - CHARRAD:
            onGround = True
            ySpeed = 0
            yPos = 700 - CHARRAD
            
        if onGround:
            refreshJumps()
            xSpeed = 0
            ySpeed = 0
        else:
            ySpeed += GRAVITY

        ###########################
        screen.fill((0, 0, 0))
        #Hitbox    
        draw.circle(screen, (0,0,0), (int(xPos), int(yPos)), 22, 1)

        #Points of arc
        draw.circle(screen,(255,0,0),(int(xPos + (22 * cos(ang1))), int(yPos - (22 * sin(ang1)))), 3, 0)
        draw.circle(screen,(255,0,0),(int(xPos + (22 * cos(ang2))), int(yPos - (22 * sin(ang2)))), 3, 0)

        #Sprite
        screen.blit(rot_center(sprite, degrees(angle)), (xPos - 20, yPos - 22))



        display.flip()
    
def refreshJumps():
    global maxJumps
    global curJumps
    curJumps = maxJumps
    

page = "game"
while page != "quit":
    if page == "game":
        page = game()

    


quit()
