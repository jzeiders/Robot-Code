__author__ = 'Jack'
import wpilib
def calcPower(lStick, rStick):
    sum = (1-abs(lStick))*rStick+rStick
    diff = (1-abs(lStick))*rStick+rStick
    data =[(sum+diff)/2,(sum-diff)/2]
    return data

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        self.motorL1 = wpilib.Talon(0)
        self.motorL2 = wpilib.Talon(0)
        self.motorR1 = wpilib.Talon(0)
        self.motorR2 = wpilib.Talon(0)
        self.strafe = wpilib.Talon(0)
        self.lStick = wpilib.Joystick(0)
        self.rStick = wpilib.Joystick(1)
        self.shiftSolenoid = wpilib.Solenoid(0)
        self.tankSolenoid = wpilib.Solenoid(1)
        self.shiftState = False
        self.shiftPressed = False
        self.tankPressed = False
        self.tankState = False
    def runMotors(self, data, strafe):
        self.motorL1.set(data[0])
        self.motorL2.set(data[0])
        self.motorR1.set(data[1])
        self.motorR2.set(data[1])
        self.strafe.set(strafe)

    def teleopPeriodic(self):

        if self.lStick.getButton(0):
            if not(tankPressed):
                self.tankSolenoid.set(not(self.tankSolenoid.get()))
                self.tankPressed = True
        else:
            self.shiftPressed = False
        if self.rStick.getButton(1):
            if not(shiftPressed):
                self.shiftSolenoid.set(not(self.shiftSolenoid.get()))
                self.shiftPressed = True
        else:
            self.shiftPressed = False

        self.runMotors(calcPower(self.lStick.getX(), self.rStick.getY()),self.rStick.getX())

if __name__ == "__main__":
    wpilib.run(MyRobot)