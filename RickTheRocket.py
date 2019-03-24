#RickTheRocket
#Team RagTag's MHV Project


###IMPORTS###
from pygame import *
#Pygame
from math import *
#Math
from random import *
#Random
from Rocket import *

#from Collide import *
#############


###INITIALIZING###
init()
size=(960,720)
screen=display.set_mode(size)
fps=time.Clock()
font = font.SysFont('Arial', 30)
display.set_caption("Rick The Rocket")
CHARRAD = 22
WHITE = (255,255,255)

launchSpeed = 11
GRAVITY = 0.38
sprite = transform.scale(image.load("main1.png"), (40,40))
buttonImg = transform.scale(image.load("buttonImg.png"), (60,20))
jumpUpImg = transform.scale(image.load("jumpUp.png"), (20,20))
speedUpImg = transform.scale(image.load("speedUp.png"), (20,20))

#WALLS

wallR = Rect(940,0,20,720)
wallL = Rect(0,0,20,720)
floorRect = Rect(0,700,960,20)

lastTime = -1000
##################

class doorButton:
    def __init__(bX, bY, bDir, dX, dY, dW, dH, speed):
        self.bX = bX
        self.bY = bY
        self.bDir = bDir
        self.door = Rect(dX, dY, dW, dH)
        self.speed = speed

    def pressed(rocket):
        if rocket.speed() >= speed:
            del self.door

class powerup:
    def __init__(xPos, yPos, ability):
        hitbox = Rect(xPos, yPos, 20, 20)
        self.ability = ability
        if ability == "jumpUp":
            self.img = jumpUpImg
        elif ability == "speedUp":
            self.img = speedUpImg

    def collected(rocket):
        if ability == "jumpUp":
            rocket.jumpsUp()
        elif ability == "launchUp":
            rocket.changeSpeed(rocket.getLaunchSpeed())
    

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def collision(nibba):
    global wallR, WallL, lastTime
    ang1 = nibba.getang1()
    ang2 = nibba.getang2()
    if nibba.getCentreX() + nibba.getRadius() >= wallR[0] + 2:
        if ang1 > ang2:
            ang1 -= 2*pi

        if ang1 <= 0 and 0 <= ang2:
            bounceX(nibba)

        else:
            nibba.xSpeed = 0
            nibba.xPos = wallR[0] - nibba.getRadius()

    if nibba.getCentreX() - nibba.getRadius() <= wallL[0] + wallL[2] + 2:
        if ang1 > ang2:
            ang1 -= 2*pi

        if ang1 <= pi and pi <= ang2:
            bounceX(nibba)

        else:
            nibba.xPos = 20 + nibba.getRadius()

    if nibba.getCentreY() + nibba.getRadius() >= 700:
        if ang1 > ang2:
            ang1 -= 2*pi

        if ang1 <= (3/2)*pi and (3/2)*pi <= ang2:
            bounceY(nibba)
            lastTime = time.get_ticks()
            
        else:
            nibba.ySpeed = 0
        
              
def bounceX(nibba):
    xSpeed = nibba.getxSpeed()*-1
    nibba.setxSpeed(xSpeed)

def bounceY(nibba):
    ySpeed = nibba.getySpeed()*-1
    nibba.setySpeed(ySpeed)
    nibba.setOnGround(False)

def game():
    running = True
    fps = time.Clock()
    rick = Rocket()
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
            if evnt.type == KEYDOWN:
                if evnt.key == K_SPACE:
                    rick.jump()
        keys = key.get_pressed()
        if keys[K_LEFT]:
            rick.rotL()
        elif keys[K_RIGHT]:
            rick.rotR()
        
        rick.xPos += rick.xSpeed
        rick.yPos += rick.ySpeed
        collision(rick)
        #if rick.onGround:
            #print(0)
        #else:
            #print(1)
        
        if rick.getCentreY() + rick.getRadius() >= 698:
            rick.onGround = True
            if time.get_ticks() - lastTime > 100:
                collision(rick)
            rick.yPos = 700 - rick.getRadius()

        else:
            rick.onGround = False
            
        if rick.onGround:
            rick.refreshJumps()
            rick.xSpeed = 0
            rick.bSpeed = 0
        else:
            rick.ySpeed += GRAVITY

        ###########################
        screen.fill((0, 0, 0)) 
        #Hitbox    
        draw.circle(screen, (0,0,0), (int(rick.xPos), int(rick.yPos)), 22, 1)

        #Points of arc
        draw.circle(screen,(255,0,0), (int(rick.xPos + (22 * cos(rick.ang1))), int(rick.yPos - (22 * sin(rick.ang1)))), 3, 0)
        draw.circle(screen,(255,0,0), (int(rick.xPos + (22 * cos(rick.ang2))), int(rick.yPos - (22 * sin(rick.ang2)))), 3, 0)

        #Sprite
        screen.blit(rot_center(sprite, degrees(rick.angle)), (rick.xPos - 20, rick.yPos - 22))

        #Wall
        draw.rect(screen, WHITE, wallR)
        draw.rect(screen, WHITE, wallL)
        draw.rect(screen, WHITE, floorRect)
        print(rick.ySpeed)
        fps.tick(80)
        display.flip()
    


page = "game"
while page != "quit":
    if page == "game":
        page = game()

    


quit()
