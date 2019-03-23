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

def menu():
    running = True
    fps = time.Clock()
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "quit"

    

page = "menu"
while page != "quit":
    if page == "menu":
        page = menu()


quit()
