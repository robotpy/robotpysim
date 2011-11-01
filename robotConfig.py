"""
Robot Config

The Robot Config holds the configuration of the physical robot you
are trying to simulate, and the way in which it should be simulated.
Essentially, it defines how motors/outputs should be displayed
in the simulator and how joysticks/inputs should be provided
to your code.

Remember, when real wpilib makes a motor or something for
you, it writes a pwm signal directly to a port, and whatever motor controller
is connected to that port takes the signal and makes hardware do
stuff, and then you notice from hardware the robot is killing someone.
When fake wpilib creates and runs something, instead of dropping
binary output into a port on hardware, it drops it straight into a display
device on software. To figure out what display device should be used
for each new output, it consults this config file. It uses a relevant
find function, like findPwmByPort() for a Victor, which returns the
PwmMotorConfig claiming that port and calls the PwmMotorConfig's Write()
function, and PwmMotorConfig deals with sending the output to the
device you specified when creating it.

A similar thing occurs with input- fake wpilib wants to know what should
be the source of a joystick's inputs, so it looks for the joystick config
configured to the port the joystick was created on in robot.py, then when
you ask your code's joystick for, say, y axis, fake wpilib knows to return
the value from the input device you set to that joystick's y axis. Joysticks
have a lot of buttons, so you pass a lot of input sources to it for all these
buttons. Unless somebody gets actual joysticks going. Then that would be easy.

Thus, each input/output has a port it represents hardware for, and an output
device or input source to get/push its values to/from.

"""

#Only import me once, from wpilib!

import pygame
import simIO.outputDevices as oD
import simIO.inputSources as iS
import simIO.configs as con
from pygame.locals import *




###Todo: Error checking in robotconfig addX() functions to ensure valid objects before they are used. ##

###############################################33
##  One singular robot's config ##
##################################
class RobotConfig:
        def __init__(self):
                #I suppose we could instead have used one general list of stuff, and then used some sort of Portend class which told more
                #specifically what the thing was, but since we essentially know all of the valid stuff types that could be connected, this is easier.
                #I'm going to assume you know what all these things are.
                self.digitalSidecars = []
                self.canDevices = []
                self.joysticks = []
                self.teamNumber = 294
        def addDigitalSidecar(self, sideCar):
                print("Adding a sidecar to slot: "+str(sideCar.slot))
                self.digitalSidecars.append(sideCar)
        def addCanDevice(self, canDevice):
                self.canDevices.append(canDevice)
        def addJoystick(self, joystick):
                self.joysticks.append(joystick)
        #This is mostly for internal getPwmPort use
        def getSidecar(self, slot):
                for car in self.digitalSidecars:
                        if car.slot == slot:
                                return car
                print("Digital sidecar not found on slot: "+str(slot))
        def getCanDevice(self, canID):
                print("Implement getCanDevice!")
                return None
        def getPwmPort(self, slot, port):
                return self.getSidecar(slot).getPwmPort(port)
        def getRelayPort(self, slot, port):
                return self.getSidecar(slot).getRelayPort(port)
        def getJoystick(self, port):
                for stick in self.joysticks:
                        if stick.port == port:
                                return stick
                print("Joystick not found on port: "+str(port))

                

#######################################3#######
##  A single digital sidecar- it has a slot and abilities to access its ports
################################
class DigitalSidecar:
        def __init__(self, slot):
                self.slot = slot             #The slot this is plugged in to on the CRIO
                self.pwmPorts = []           #The pwm output ports on the sidecar, 1-10 IIRC
                self.relayPorts = []         #The relay outputs on the sidecar, 1-8 IIRC
                self.digitalPorts = []       #The general purpose digital ports, I don't even want to remember those.
                self.RSLPort = None          #Robot status light. Blink, blink. That thing is stupid bright.
        def addPwmPort(self, pwmOutputThing):
                print("Adding PwmPort to port: "+str(pwmOutputThing.port)+" in slot: "+str(self.slot))
                self.pwmPorts.append(pwmOutputThing)
        def addRelayPort(self, relayThing):
                self.relayPorts.append(relayThing)
        def addDigitalPort(self, digitalThing):
                self.digitalPorts.append(digitalThing)
        def addRSLPort(self, blinky):
                self.RSLPort = blinky

        def getPwmPort(self, port):
                print("Getting PwmPort from: "+str(port))
                for pwm in self.pwmPorts:
                        if pwm.port == port:
                                return pwm
                print("Pwm output not found on slot: "+str(self.slot)+", port: "+str(port))
        def getRelayPort(self, port):
                print("If you see this message, you need to go implement getRelayPort")
        def getDigitalPort(self, port):
                print("If you see this message, you need to go implement getDigitalPort")


#############################################################################################
### # # # # # # # # # # # # # # # # # # # # #
##### HERES WHERE THE FUN HAPPENS! ##########################################################
## # # # # # # # # # # # # # # # # # # # # #
### # # # # # # # # # # # # # # # # # # # # #################################################
## # # # # # # # # # # # # # # # # # # # # #
### # # # # # # # # # # # # # # # # # # # # #################################################
##
#############################################################################################
##
#############################################################################################
##
#############################################################################################


#Reference this whenevs you want to find a thing.
config = RobotConfig()


#Now add ALL the things to the config!

#Remember, if you want it to work right, every device that your robot expects to use must be added
#properly to the config. This means your sidecar has to be added to the right slot, your pwms
#must be added to the right ports, etc. This is where the magic happens.


#We will keep this reference handy since we'll be adding stuff directly to it
#before adding it to config
sidecar = DigitalSidecar(1)

#Add a thing connected to a PWM port on that one sidecar we made
sidecar.addPwmPort(
        #This thing shall be a PwmMotor! Important: PwmMotor extends PwmConfigBase. Any sort of PwmConfigBase
        #can be added to a PWM port, and the implementation determines what happens when stuff gets written to the port.
        #PwmMotor takes the stuff and passes it along to one DisplayDevice. You might instead make a pwmconfigbase
        #that writes over a network to a VIRSYS simulator, provided you set that up, of course.
        con.PwmMotor(
                1,         #This is the port it's on. Duh. Look in simIO.DisplayDevices.
                oD.Spinner()  #We define the sole display device to be a spinner.Any sort of SimpleDisplay would work here.
                )
        )

#Attach the sidecar to slot one on CRIO!
config.addDigitalSidecar(
        sidecar
        )


#Let's add a joystick mapped to w and s, shall we?
config.addJoystick(
        #We make it a ButtonJoystick. Any sort of JoystickConfigBase, from configs, would have worked
        con.ButtonJoystick(
                1, #joy port 1
                #From inputsources, TKSI makes either -1, 0, or 1 depending on the combo of buttons pressed
                #Check iS.Joystick class.
                iS.TwoKeySimpleInput(
                        K_w,         #Up top me from pygame.locals import *, remember? http://pygame.org/docs/ref/key.html
                        K_s          #w is +, s is -, FYI
                        )
                #Normally we'd define the other axes & stuffs on the joystick, but that's bothersome.
                )
        )







