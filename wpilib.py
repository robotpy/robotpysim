import robotConfig
import time

"""
def setupFakeWpilib(displayer, inputThing):
    global disp
    disp = displayer
    global inputSource
    inputSource = inputThing
    global theRobot
"""
def Wait(lengthMillis):
    time.sleep(lengthMillis / 1000)


    
class SimpleRobot:

    def __init__(self):
        print("Creating a SimpleRobot")
        self.isOperatorControl = True
        self.isEnabled = True
        theRobot = self
        
    #This used to do stuff with the FMS in the robot version, here it interfaces
    #with our fake FMS to do the same stuff.
    def StartCompetition(self):
        self.OperatorControl()
        pass
    #What do you think these are?
    def IsOperatorControl(self):
        return self.isOperatorControl
    def IsEnabled(self):
        return self.isEnabled
    def kill(self):
        print("Killing Robot")
        self.isEnabled = False
        self.isOperatorControl = False




class BasicOutputter:
    #Placeholder for expected subclass implementation. You don't have to actually
    #call this
    def __init__(self):
        self.output = None
        self.value = 0
    def Set(self, value):
        self.value = value
        self.output.write(self.value) 


################################################################################
####  MOTOR CONTROLLERS  #####
################################################################################
        


class Jaguar(BasicOutputter):
    def __init__(self, pwmPort):
        print("Creating a Jaguar")
        #This is your code's side of the port- where it puts out values.
        #Next we find and connect it to the simulator output device you made for it
        self.pwmPort = pwmPort
        self.output = robotConfig.config.getPwmPort(1,self.pwmPort)
        
class Victor(BasicOutputter):
    def __init__(self, pwmPort):
        print("Creating a Victor")
        self.pwmPort = pwmPort
        self.output = robotConfig.config.getPwmPort(1,self.pwmPort)

class CANJaguar(Jaguar):
    def __init__(self, canPort):
        print("Creating a CANJaguar")
        self.canPort = canPort
        self.output = robotConfig.config.getCanDevice(self.canPort)

###############################################################################
####  SENSORS ####
###############################################################################
##
## Here starts the classes of all sensory items.
##
## Also SensorBase, the base class for most of them
##
##================================================

#This is both a standard sensor base for rps, but also is WPILib's SensorBase,
#doing double duty.
class SensorBase:
    #Again, no need to actually call. Just make sure these fields exist as named.
    def __init__(self):
        self.source = None
        self.value = 0
"""
class DigitalInput(SensorBase):
    def __init__(self, ):
        self.source = robotConfig.findDigitalSidecarPort(
"""
###############################################################################
####  PNEUMATICS  ####
###############################################################################
##
## A lumping together of everything that uses air.
##
## Includes Solenoid and Compressor
##
##################################################

class Solenoid (BasicOutputter):
    
    defaultSolenoidSlot = 8
    
    def __init__(self, channel, slot):
        print("Creating a Solenoid")
        self.channel = channel
        self.slot = slot
        self.output = robotConfig.findSolenoidOutput(self.channel, self.slot)
        self.value = 0

        self.setupDraw()
    def __init__(self, channel):
        self.__init__(self, channel, Solenoid.defaultSolenoidSlot)


###############################################################################
####  OPERATOR CONTROLS  #####
###############################################################################

class Joystick:
    def __init__(self, port):
        print("creating joystick")
        self.port = port
        self.config = robotConfig.config.getJoystick(self.port)

        
    #We'll put in classes for all of the functions on the joystick. If you don't like how
    #we come up with the values, like, if all you have is a keyboard, just change how to
    #come up with them here! It's totally arbitrary! Though if you do it in a cool way,
    #be sure to make it available for others somewhere.
    def GetY(self):
        return self.config.GetY()

