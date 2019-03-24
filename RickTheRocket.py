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

launchSpeed = 11
GRAVITY = 0.38
sprite = transform.scale(image.load("main1.png"), (40,40))
##################

class Rocket:
    
    xSpeed = ySpeed = 0
    xPos = 300
    yPos = 698
    onGround = True
    maxJumps = curJumps = 4
    angle = 0
    ang1 = pi/4
    ang2 = 3 * (pi/4)
    launchSpeed = 11

    def changeSpeed(launchSpeed):
        self.launchSpeed = launchSpeed
    
    def jump(self):
        if self.curJumps > 0:
            if round(sin(self.angle + (pi / 2)), 10) > 0:
                self.ySpeed = 0
            self.xSpeed = 0
            self.onGround = False
            self.curJumps -= 1
            self.ySpeed -= self.launchSpeed * round(sin(self.angle + (pi / 2)), 10) #Minus for PyGame heights being inverted
            self.xSpeed += self.launchSpeed * round(cos(self.angle + (pi / 2)), 10)#R 
            
    def rotR(self):
        self.angle -= 0.05
        self.ang1 -= 0.05
        self.ang2 -= 0.05
    def rotL(self):
        self.angle += 0.05
        self.ang1 += 0.05
        self.ang2 += 0.05
    def refreshJumps(self):
        self.curJumps = self.maxJumps
    

    

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



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
        
        if rick.yPos >= 700 - CHARRAD:
            rick.onGround = True
            rick.ySpeed = 0
            rick.yPos = 700 - CHARRAD
            
        if rick.onGround:
            rick.refreshJumps()
            rick.xSpeed = 0
            rick.ySpeed = 0
        else:
            rick.ySpeed += GRAVITY

        ###########################
        screen.fill((0, 0, 0))
        #Hitbox    
        draw.circle(screen, (0,0,0), (int(rick.xPos), int(rick.yPos)), 22, 1)

        #Points of arc
        draw.circle(screen,(255,0,0),(int(rick.xPos + (22 * cos(rick.ang1))), int(rick.yPos - (22 * sin(rick.ang1)))), 3, 0)
        draw.circle(screen,(255,0,0),(int(rick.xPos + (22 * cos(rick.ang2))), int(rick.yPos - (22 * sin(rick.ang2)))), 3, 0)

        #Sprite
        screen.blit(rot_center(sprite, degrees(rick.angle)), (rick.xPos - 20, rick.yPos - 22))


        fps.tick(80)
        display.flip()
    


page = "game"
while page != "quit":
    if page == "game":
        page = game()

    


quit()
