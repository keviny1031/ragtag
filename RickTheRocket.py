#RickTheRocket
#Team RagTag's MHV Project


###IMPORTS###
from pygame import *
#Pygame
from math import *
#Math
from random import *
#Random
from rocket import *
#Rocket
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
size=(1000,700)
screen=display.set_mode(size)
fps=time.Clock()
font = font.SysFont('Arial', 30)
display.set_caption("Rick The Rocket")
CHARRAD = 22
GRAVITY = 0.38
sprite = transform.scale(image.load("main1.png"), (40,40))
background = image.load("resizedBack.jpg")
level = 1
##################

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



def game(level):
    running = True
    fps = time.Clock()
    rick = Rocket()
    floors = levels[level - 1]
    buttonVals = floors[-1]
    floors.remove(floors[-1])
    walls = []
    for l in range(len(floors)):
        for i in range(10):
            layer = floors[l][i]
            if layer == "L":
                rick.setPos((i + 1) * 100 - 75, (l + 1) * 100 - 300)
            if layer == "G":
                flag = Rect(i * 100, l * 100 - 300, 100, 100)
            if layer == "@":
                walls.append(Rect(i * 100, l * 100 - 300, 100, 100))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
            elif evnt.type == KEYDOWN:
                if evnt.key == K_SPACE:
                    rick.jump()

        screen.blit(background,(0,-300))
        
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
            
        screen.blit(background,(0,-300))
        ###########################
        
        #Hitbox    
        draw.circle(screen, (0,0,0), (int(rick.xPos), int(rick.yPos)), 22, 1)

        #Points of arc
        draw.circle(screen,(255,0,0),(int(rick.xPos + (22 * cos(rick.ang1))), int(rick.yPos - (22 * sin(rick.ang1)))), 3, 0)
        draw.circle(screen,(255,0,0),(int(rick.xPos + (22 * cos(rick.ang2))), int(rick.yPos - (22 * sin(rick.ang2)))), 3, 0)

        for r in walls:
            draw.rect(screen, (255, 0, 0), r)
        draw.rect(screen, (255, 255, 255), flag)
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
            if level < 6:
                level += 1
            else:
                print("good job bud")
                page = "quit"
                break

quit()
