from math import *

class Rocket:
    
    xSpeed = ySpeed = bSpeed = 0
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
    def launchSpeed(self):
        return self.launchSpeed

    def jumpsUp(self):
        self.maxJumps += 1
    
    def jump(self):
        if self.curJumps > 0:
            if round(sin(self.angle + (pi / 2)), 10) > 0:
                self.ySpeed = 0
                self.bSpeed = ySpeed
            self.xSpeed = 0
            self.onGround = False
            self.curJumps -= 1
            self.ySpeed -= self.launchSpeed * round(sin(self.angle + (pi / 2)), 10) #Minus for PyGame heights being inverted
            if round(sin(self.angle + (pi / 2)), 10) > 0:
                self.bSpeed = self.ySpeed
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
    def speed(self):
        return (self.xSpeed ** 2 + self.ySpeed ** 2) ** 0.5
