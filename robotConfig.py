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


import pygame
import outputDevices as oD
import inputSources as iS
from pygame.locals import *

#please only import me once from wpilib, else bad stuff :(




pwmPorts = []
oD.PwmMotorConfig(pwmPorts,1,rd.Spinner())
oD.PwmMotorConfig(pwmPorts,2,rd.Spinner())
oD.PwmMotorConfig(pwmPorts,3,rd.SimpleOutput())


canIds = []

solenoidPorts = []


joysticks = []
iS.JoystickConfig(joysticks, 1, ds.TwoKeySimpleInput(K_w, K_s))


def findPwmByPort(port):
    for each in pwmPorts:
        if each.port == port:
            print("Found PWM device on port: " + str(port))
            return each
    print("No device configured to PWM " + str(port))

    
def findJoystick(joyPort):
    for each in joysticks:
        if each.port == joyPort:
            print("Found joystick on port: " + str(joyPort))
            return each
    print("No joystick configured to joy port " + str(joyPort))
