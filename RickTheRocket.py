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
midRect = Rect(250, 300, 150, 100)
blocks = [wallR, wallL, floorRect, midRect]

lastTime = -1000
tTime = -1000
intX, intY = 0,0
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

def collision(rleft, rtop, width, height,   # rectangle definition
              center_x, center_y, radius):  # circle definition
    """ Detect collision between a rectangle and circle. """
    global intX, intY

    # complete boundbox of the rectangle
    rright, rbottom = rleft + width, rtop + height

    # bounding box of the circle
    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    # trivial reject if bounding boxes do not intersect
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if hypot(x-center_x, y-center_y) <= radius:
                intX = x
                intY = y
                return True  # collision detected

    # check if center of circle is inside rectangle
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True  # overlaid

    return False  # no collision detected

'''
def collision(nibba):
    global wallR, WallL, lastTime, blocks
    ang1 = nibba.getang1()
    ang2 = nibba.getang2()

    for b in blocks:
        x = nibba.getCentreX()
        y = nibba.getCentreY()
        r = nibba.getRadius()
        #print(x,y,r)

        if x + r >= b[0] + 2 and x + r <= b[0] + b[2] + 2 and y > b[1] and y < b[1] + b[3]:
            if ang1 > ang2:
                ang1 -= 2*pi

            if ang1 <= 0 and 0 <= ang2:
                bounceX(nibba)

            else:
                nibba.xSpeed = 0
                nibba.xPos = b[0] - r

        if x - r <= b[0] + b[2] + 2 and x - r >= b[0] + 2 and y > b[1] and y < b[1] + b[3]:
            if ang1 > ang2:
                ang1 -= 2*pi

            if ang1 <= pi and pi <= ang2:
                bounceX(nibba)

            else:
                nibba.xSpeed = 0
                nibba.xPos = b[0] + b[2] + r

        if y + r >= b[1] and y + r <= b[1] + b[3] and x > b[0] and x < b[0] + b[2]:
            if ang1 > ang2:
                ang1 -= 2*pi

            if ang1 <= (3/2)*pi and (3/2)*pi <= ang2:
                bounceY(nibba)
                lastTime = time.get_ticks()
                
            else:
                nibba.ySpeed = 0

        if y - r >= b[1] + b[3] and y - r <= b[1] and x > b[0] and x < b[0] + b[2]:
            if ang1 > ang2:
                ang1 -= 2*pi

            if ang1 <= (1/2)*pi and (1/2)*pi <= ang2:
                bounceY(nibba)
                lastTime = time.get_ticks()
                
            else:
                nibba.ySpeed = 0
'''   
    
        
              
def bounceX(nibba):
    xSpeed = nibba.getxSpeed()*-1
    nibba.setxSpeed(xSpeed)

def bounceY(nibba):
    nibba.setOnGround(False)
    ySpeed = nibba.getySpeed()*-1
    nibba.setySpeed(ySpeed)
    nibba.setOnGround(False)

def game():
    global tTime, lastTime
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

        for b in blocks:
            if collision(b[0], b[1], b[2], b[3], rick.getCentreX(), rick.getCentreY(), rick.getRadius()):
                if rick.ang1 > rick.ang2:
                    rick.ang1 -= 2*pi

                if (rick.ang1 <= 0 and 0 <= rick.ang2) or (rick.ang1 <= pi and pi <= rick.ang2):
                    bounceX(rick)

                else:
                    rick.xSpeed = 0

                if ((rick.ang1 <= (1/2)*pi and (1/2)*pi <= rick.ang2) or (rick.ang1 <= (3/2)*pi and (3/2)*pi <= rick.ang2)) and time.get_ticks() - lastTime > 100:
                    lastTime = time.get_ticks()
                    bounceY(rick)

                else:
                    rick.YSpeed = 0

                    

        #if rick.onGround:
            #print(0)
        #else:
            #print(1)
        
        if rick.getCentreY() + rick.getRadius() >= 698:
            rick.onGround = True
            
            rick.yPos = 700 - rick.getRadius()

        else:
            rick.onGround = False
            
        if rick.onGround:
            rick.refreshJumps()
            rick.xSpeed = 0
            rick.ySpeed = 0
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
        draw.rect(screen, WHITE, midRect)
        fps.tick(80)
        display.flip()
    


page = "game"
while page != "quit":
    if page == "game":
        page = game()

    


quit()
