
"""

RobotPySim (RPS) is a graphical cRIO and WPILib simulator for teams using Peter
Johnson's Python interpreter and utilities (github/robotpy) to program robots
for the FIRST Robotics Competiton (FRC). It is designed as a testing tool to
detect runtime errors and ensure correct behavior when deploying to a cRIO is
inconvenient. While it should be suitable for most robots as-is, the greatness
of WPILib and the cRIO is such that the author cannot repreduce it in full.
RPS is designed to be extensible, and teams are encouraged to write their own
implementations of obscure functions and submit them for inclusion in RPS
proper. The user should note that, while the author has tested RPS with real
code from Beach Cities Robotics 294's 2010 and 2011 robots, he does not have
access to a cRIO, and so code written first for RPS should not be trusted to
necessarily open any podbay doors.

The best part? RobotPySim is an in-place replacement of a cRIO. Robot code that
runs in RPS will run on a cRIO, and code that runs on a cRIO will not need to
be changed to run in RPS.






Copyright © 2011 Fintan O'Grady

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import simIO.robotDisplayer
import simIO.inputer
#global displayer
displayer = simIO.robotDisplayer.RobotDisplayer()
#global inputer
inputer = simIO.inputer.Inputer()

simIO.robotDisplayer.SetupDisplayer(displayer)
simIO.inputer.SetupInputer(inputer)


import robot
import simIO.outputDevices
import simIO.inputer
import threading
import _thread
import pygame


    





def main():
    run = True

    

    print("Starting robot thread")
    _thread.start_new_thread(robot.run,())
    #robot.run()

    clock = pygame.time.Clock()
    
    while (run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting")
                run = False
                #theRobot.kill()
                pygame.quit()
            inputer.send(event)
        displayer.draw()




if __name__ == '__main__':
    main()
