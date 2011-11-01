from pygame.locals import *
import simIO.inputer

class TwoKeySimpleInput:
    def __init__(self, positiveKey, negativeKey):
        self.title = "TwoKeySimpleInput"
        self.pKey = positiveKey
        self.nKey = negativeKey
        self.value = 0
        simIO.inputer.inputer.addSource(self)
    def send(self, event):
        #We add/subtract our value so holding down both + and - results in net zero.
        #This might cause always on problems should the simulator be started with some keys
        #already pressed or something, but after toggling + and - a couple times should zero
        #itself. Maybe.
        if event.type == KEYDOWN:
            if (event.key == self.pKey):
                self.value += 1
            if (event.key == self.nKey):
                self.value -= 1
        if event.type == KEYUP:
            if (event.key == self.pKey):
                self.value -= 1
            if (event.key == self.nKey):
                self.value += 1

        #Loltastically awesome way to contstrain value to [-1,1]
        if abs(self.value) > 1:
            self.value = abs(self.value) / self.value
    def getValue(self):
        return self.value
