import wpilib
import math

class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        super().__init__()
        pass
    
    def RobotInit(self):
        pass

    def Disabled(self):
        pass

    def Autonomous(self):
        pass

    def OperatorControl(self):
        motor = wpilib.Jaguar(1)
        #motor2 = wpilib.Jaguar(2)
        #printMotor = wpilib.Jaguar(3)
        joy = wpilib.Joystick(1)
        while self.IsOperatorControl() and self.IsEnabled():
            #printMotor.Set(joy.GetY())
            motor.Set(joy.GetY())
            #motor2.Set(joy.GetY())
            wpilib.Wait(.06)
        print("Exiting operator control")
        pass



def run():
    robot = MyRobot()
    robot.StartCompetition()


