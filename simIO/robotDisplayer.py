import os
import sys

import pygame
from pygame.locals import *

def SetupDisplayer(theDisplayer):
    print("Setting up global displayer")
    global displayer
    displayer = theDisplayer


#A robot displayer. RobotPySim creates and owns one to print to screen. Make sure
#your output dev
class RobotDisplayer ():

    def __init__(self):
        self.nextDrawSpace = 1
        self.toDraw = []

        pygame.init()
        self.screen = pygame.display.set_mode((600,480))
        pygame.display.set_caption("RobotPySim")

    def addOutputDevice(self, device):
        print("Adding "+device.title+" to displayer")
        device.rect.left = self.nextDrawSpace * 100
        self.nextDrawSpace += 1
        self.toDraw.append(device) 
    def draw(self):
        self.screen.fill((255,255,255))
        for each in self.toDraw:
            each.draw(self.screen)
        pygame.display.flip()
