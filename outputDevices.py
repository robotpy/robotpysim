import os
import sys

import pygame
from pygame.locals import *

import threading

pygame.font.init()
stdFont = pygame.font.Font(None, 36)

#A robot displayer. RobotPySim creates and owns one to print to screen. Make sure
#your output dev
class RobotDisplayer ():

    def __init__(self):
        self.nextDrawSpace = 1
        self.toDraw = []

        pygame.init()
        self.screen = pygame.display.set_mode((600,480))
        pygame.display.set_caption("RobotPySim")

    def addToDraw(self, toDraw):
        print("Adding output to draw")
        toDraw.rect.left = self.nextDrawSpace * 100
        self.nextDrawSpace += 1
        self.toDraw.append(toDraw)        
    def draw(self):
        self.screen.fill((255,255,255))
        for each in self.toDraw:
            each.draw(self.screen)
        pygame.display.flip()



class PwmMotorConfig:
    def __init__(self, portList, pwmPort, displayType):
        portList.append(self)
        self.port = pwmPort
        self.displayType = displayType
    def Write(self, signal):
        self.displayType.write(signal)


#A generic output thingy. You write() it a single value. It displays that number
#when you draw(screen) it. Just override draw() and access self.value if you
#want to subclass it and make simple custom displays for one variable.
class SimpleOutput():
    def __init__(self):
        self.rect = pygame.Rect(0,50,100,100)
        #The driving value of the display
        self.value = 0

        #A buffered copy of what this output displays, so we can do other fancy
        #stuff like not freaking redraw it when we don't need to.
        self.image = pygame.Surface((200,50))

    def write(self, value):
        self.value = value

    def draw(self, screen):
        #Heh. This is kinda bad. We shouldn't be creating new images every frame.
        #But I'm trying to keep everything related only to the text display in here
        #so that it's really clean if you override just draw().
        self.image = stdFont.render(str(self.value), False, (0,0,0), (255,255,255))
        screen.blit(self.image, self.rect)
        
#A display type nice for motors. It is a circle. The circle spins. Notice it
#extends SimpleOutput- the only thing different is how it draws itself. So the
#only thing we did was change how it draws itself. Duh.
class Spinner(SimpleOutput):
    def __init__(self):
        super().__init__()
        self.sourceImage = pygame.image.load('LegoWheel.png')
        self.angle = 0
    def draw(self, screen):
        self.angle += self.value * 2
        self.image = pygame.transform.rotate(self.sourceImage, self.angle)
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        screen.blit(self.image, (self.rect.left-self.rect.w/2, self.rect.top-self.rect.h/2))




