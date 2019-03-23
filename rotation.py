#rotation.py

from pygame import *
from math import *
init()

size = (800,600)
screen = display.set_mode(size)

display.set_caption("Rotation")
sprite = transform.scale(image.load("main1.png"), (40,40))

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

angle = 0
ang1 = pi/4
ang2 = 3*(pi/4)

px,py = 400,300
running = True

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == KEYDOWN:
            keypress = True

    keys=key.get_pressed()
    screen.fill((255,255,255))

    if keys[K_LEFT] and keypress:
        angle += 0.01
        ang1 += 0.01
        ang2 += 0.01
    elif keys[K_RIGHT] and keypress:
        angle -= 0.01
        ang1 -= 0.01
        ang2 -= 0.01

    #Hitbox    
    draw.circle(screen, (0,0,0), (px+20,py+22), 22, 1)

    #Points of arc
    draw.circle(screen,(255,0,0),(int(px+20+(22*cos(ang1))),int(py+22-(22*sin(ang1)))), 3, 0)
    draw.circle(screen,(255,0,0),(int(px+20+(22*cos(ang2))),int(py+22-(22*sin(ang2)))), 3, 0)

    #Sprite
    screen.blit(rot_center(sprite, degrees(angle)), (px, py))

    #print(str(angle) + " " + str(ang1) + " " + str(ang2))
    display.flip()

quit()
