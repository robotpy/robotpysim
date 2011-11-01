###################################
####  Configs  ####
###################################
##
##  Configs is a collection of classes for wpilib's simulation of input
##     and output, and also of base classes for each port type.
##
##  The purpose of the configs is to specify what input/output should be
##      connected to what ports
##
##  Each type of port, eg joystick port, CANJaguar, must implement some
##      specific fields/methods. These are delineated in the base classes
##      named after the port: 


import simIO.inputSources as inputSources

#Fake default for when the coder can't be arsed to fill out every joystick butto
fake = inputSources.TwoKeySimpleInput(None, None)


################################
## Generic Output ##
####################
##  A generic output is a generic port that can be written to
##
##  It just needs a way to write to it, and a list of displayDevices it prints to.
################################

class GenericOutput:
    def __init__(self):
        self.displayDevices = []
    def write(self, signal):
        for device in self.displayDevices:
            device.write(signal)
    
###############################
## PwmConfigbase ##
###################
##  A generic thing attached to the digital sidecar main PWM out ports
##
##  It needs the port it's attached to (1-10, to wit), but the slot
##      should be taken care of by the digital sidecar to which it's connected
##  It also needs to be write(value)able.
###############################

class PwmConfigBase (GenericOutput):
    def __init__(self, port):
        super().__init__()
        self.port = port

#A standard motor attached to PWM. Writes to one outputdevice.
class PwmMotor(PwmConfigBase):
    def __init__(self, port, displayDevice):
        super().__init__(port)
        self.displayDevices.append(displayDevice)


##############################
## JoystickConfigBase ##
########################
##  A generic joystick input
##
##  Any joystick must know its port and provide methods to obtain
##      all axes and buttons on the stick
##
##  None of the methods here are actually implemented. Extend if you want the
##      dummy functions anyway
##############################
        

class JoystickConfigBase:
    def __init__(self, port):
        self.port = port
    def GetX(self):
        return 0
    def GetY(self):
        return 0
    def GetZ(self):
        return 0
    def GetThrottle(self):
        return 0
    def GetTrigger(self):
        return 0
    def GetTop(self):
        return 0
    def GetButton(self, buttonEnum):
        return 0
    def GetRawButton(self, buttonNum):
        return 0
class ButtonJoystick(JoystickConfigBase):
    def __init__(self,
                 port,
                 sourceY = fake,
                 sourceX = fake,
                 sourceTrigger = fake,
                 sourceButtons = []
                 ):
        super().__init__(port)
        self.sourceY = sourceY
    def GetY(self):
        return self.sourceY.getValue()
    	



