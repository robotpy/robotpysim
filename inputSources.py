from pygame.locals import *

class PwmMotorConfig:
    def __init__(self, portList, pwmPort, displayType):
        portList.append(self)
        self.port = pwmPort
        self.displayType = displayType
    def Write(self, signal):
        self.displayType.write(signal)
        
class JoystickConfig:
    def __init__(self, portList, joyPort, ySource):
        portList.append(self)
        self.port = joyPort
        self.ySource = ySource
    def getY(self):
        return self.ySource.getValue()
    
class TwoKeySimpleInput:
    def __init__(self, positiveKey, negativeKey):
        self.pKey = positiveKey
        self.nKey = negativeKey
        self.value = 0
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
