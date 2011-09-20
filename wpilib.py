import robotConfig
import RobotPySim
import time

def setupFakeWpilib(displayer, inputThing):
    global disp
    disp = displayer
    global inputSource
    inputSource = inputThing
def Wait(lengthMillis):
    time.sleep(lengthMillis / 1000)
class SimpleRobot:

    def __init__(self):
        print("Creating a SimpleRobot")
        self.isOperatorControl = True
        self.isEnabled = True
        
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

class Jaguar:
    def __init__(self, port):
        #Here we store the last value the robot fed to us with write or similar
        #
        #Range -1 to 1
        self.power = 0
        print("Creating a Jaguar")

        #Config we find from the robotConfig file, which holds the positions of
        #all the motors and such and also defines how to display them. We can find
        #which motor output type we wanted this motor to show up as because we
        #look at the ports in config and what this was created as- neat, huh?
        self.config = robotConfig.findPwmByPort(port)
        
        #This is our display type. Once we add it to the roboDisplay, rB will
        #regularly call on it to draw itself. Make sure to keep it fed with your
        #intended output state in to whatever internal state your components
        #might have, so it draws something that makes sense.
        self.display = self.config.displayType
        disp.addToDraw(self.display)

        
    def Set(self, power):
        self.value = power
        self.display.write(power)

class Joystick:
    def __init__(self,port):
        print("creating joystick")
        self.port = port
        self.source = robotConfig.findJoystick(port)

        inputSource.addController(self.source.ySource)
    #We'll put in classes for all of the functions on the joystick. If you don't like how
    #we come up with the values, like, if all you have is a keyboard, just change how to
    #come up with them here! It's totally arbitrary! Though if you do it in a cool way,
    #be sure to make it available for others somewhere.
    def GetY(self):
        return self.source.getY()

