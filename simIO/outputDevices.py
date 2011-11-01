import threading
import os
import sys
import simIO.robotDisplayer
import pygame
from pygame.locals import *



pygame.font.init()
stdFont = pygame.font.Font(None, 36)




#A generic drawing thingy. You write() it a single value. It displays that number
#when you draw(screen) it. Just override draw() and access self.value if you
#want to subclass it and make simple bustom displays for one variable.
class GenericDisplay():
    def __init__(self):
        self.title = "Generic Display" #For debug purposes- "Added a Generic Display"
        self.rect = pygame.Rect(0,50,100,100)
        #The driving value of the display
        self.value = 0

        #A buffered copy of what this output displays, so we can do other fancy
        #stuff like not freaking redraw it when we don't need to.
        self.image = pygame.Surface((200,50))
        simIO.robotDisplayer.displayer.addOutputDevice(self)

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
class Spinner(GenericDisplay):
    def __init__(self):
        super().__init__()
        self.title = "Spinner Display"
        self.sourceImage = pygame.image.load('simIO/LegoWheel.png')
        self.angle = 0
    def draw(self, screen):
        self.angle += self.value * 2
        self.image = pygame.transform.rotate(self.sourceImage, self.angle)
        self.rect.w = self.image.get_width()
        self.rect.h = self.image.get_height()
        screen.blit(self.image, (self.rect.left-self.rect.w/2, self.rect.top-self.rect.h/2))




