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
#############

levels = []

with open("levels.txt", "r") as file:
    lines = file.read().splitlines()
    level = []
    for line in lines:
        if line.count("#") == 0:
            level.append(line)
        else:
            levels.append(level)
            level = []
###INITIALIZING###
init()
size=(960,720)
screen=display.set_mode(size)
fps=time.Clock()
font = font.SysFont('Arial', 30)
display.set_caption("Rick The Rocket")
CHARRAD = 22
curLevel = 0
level = 1
launchSpeed = 11
GRAVITY = 0.38
sprite = transform.scale(image.load("main1.png"), (40,40))
flagImg = transform.scale(image.load("flag.png"), (100, 100))
buttonImg0 = transform.scale(image.load("buttonImg0.png"), (100,20))
buttonImg1 = transform.scale(image.load("buttonImg1.png"), (100,20))
buttonImg2 = transform.scale(image.load("buttonImg2.png"), (100,20))
buttonImg3 = transform.scale(image.load("buttonImg3.png"), (100,20))
buttonAnim = [buttonImg0, buttonImg1, buttonImg2, buttonImg3, buttonImg2, buttonImg1, buttonImg0]
jumpUpImg = transform.scale(image.load("jumpUp.png"), (20,20))
speedUpImg = transform.scale(image.load("speedUp.png"), (20,20))
##################

class doorButton:
    def __init__(self, bX, bY, dX, dY, speed):
        self.bX = bX
        self.bY = bY
        self.dX = dX
        self.dY = dY
        self.door = Rect(self.dX, self.dY, 100, 100)
        self.but = Rect(self.dX, self.dY, 100, 20)
        self.speed = speed
        self.image = buttonImg0
        
    def pressed(self, rocket):
        if rocket.speed() >= speed:
            del self.door

    def getDoor(self):
        return self.door
    def getBut(self):
        return self.but
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



def game(level):
    print(levels)
    running = True
    fps = time.Clock()
    rick = Rocket()
    floors = levels[level - 1]
    buttonVals = floors[-1]
    floors.remove(floors[-1])
    walls = []
    but = False
    for l in range(len(floors)):
        for i in range(10):
            layer = floors[l][i]
            if layer == "L":
                rick.setPos((i + 1) * 100 - 75, (l + 1) * 100 - 300)
            if layer == "G":
                flag = Rect(i * 100, l * 100 - 300, 100, 100)
            if layer == "@":
                walls.append(Rect(i * 100, l * 100 - 300, 100, 100))
            if layer == "B":
                
                but = True
                bx = i * 100
                by = l * 100 - 300
            if layer == "D":
                dX = i * 100
                dY = i * 100 - 300

    if but:
        button = doorButton(bx, by, dX, dY, buttonVals) 
            
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
            elif evnt.type == KEYDOWN:
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

        for r in walls:
            draw.rect(screen, (255, 0, 0), r)
        screen.blit(flagImg, flag)
        if but:
            screen.blit(button.image, button.getBut())
            draw.rect(screen, (200, 0, 0), button.getDoor())
            
        #Sprite
        screen.blit(rot_center(sprite, degrees(rick.angle)), (rick.xPos - 20, rick.yPos - 22))
        fps.tick(80)
        
        display.flip()


        if flag.collidepoint(rick.xPos, rick.yPos):
            return "game"
        


page = "game"
while page != "quit":
    if page == "game":
        page = game(level)
        if page == "game":
            level += 1

    


quit()
