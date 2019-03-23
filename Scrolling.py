#RickTheRocket
#Team RagTag's MHV Project


###IMPORTS###
from pygame import *
#Pygame
from math import *
#Math
from oauth2client.service_account import ServiceAccountCredentials
import gspread
#for Google Sheets
from random import *
#Random
#############


###INITIALIZING###
init()
size=(960,720)
screen=display.set_mode(size)
fps=time.Clock()
display.set_caption("Rick The Rocket")
##################

###COLOURS###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def menu():
    running = True
    fps = time.Clock()
    charx = 430
    chary = 310

    topLiney = 80
    botLiney = 640

    greeny = 80
    topRedy = -480
    botRedy = 640
    
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"
        
        keys = key.get_pressed()
        if keys[K_UP] and chary > 80:
            chary -= 0.25
        if keys[K_DOWN] and chary < 590:
            chary += 0.25
        if keys[K_RIGHT] and (charx + 50) < 960:
            charx += 0.25
        if keys[K_LEFT] and charx > 0:
            charx -= 0.25
            
        screen.fill(WHITE)
        char = Rect(charx, chary, 50, 50)
        draw.rect(screen, BLACK, char)

        if chary == 80:
            if keys[K_UP]:
                greeny += 0.25
                topRedy += 0.25
                botRedy += 0.25
                topLiney += 0.25
                botLiney += 0.25

        if chary == 590:
            if keys [K_DOWN]:
                greeny -= 0.25
                topRedy -= 0.25
                botRedy -= 0.25
                topLiney -= 0.25
                botLiney -= 0.25

        greenRect = Rect(935, greeny, 25, 560) #x, y, width, length
        topRedRect = Rect(935, topRedy, 25, 560)
        botRedRect = Rect(935, botRedy, 25, 560)
            
        draw.rect(screen, GREEN, greenRect)
        draw.rect(screen, RED, topRedRect)
        draw.rect(screen, RED, botRedRect)

        draw.line(screen, BLACK, (0, topLiney), (960, topLiney))
        draw.line(screen, BLACK , (0, botLiney), (960, botLiney))
        display.flip()

    

page = "menu"
while page != "quit":
    if page == "menu":
        page = menu()


quit()
