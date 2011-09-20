import robot
import robotDisplayer
import inputer
import wpilib
import threading
import _thread
import pygame

def main():
    run = True
    
    disp = robotDisplayer.RobotDisplayer()
    control = inputer.Inputer()
    
    wpilib.setupFakeWpilib(disp, control)
    
    _thread.start_new_thread(robot.run,())
    #robot.run()

    clock = pygame.time.Clock()
    
    while (run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting")
                run = False
                pygame.quit()
            control.send(event)
        disp.draw()




if __name__ == '__main__':
    main()
