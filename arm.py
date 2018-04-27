import pygame
class Arm:
    MIN_HEIGHT = 3
    MAX_HEIGHT = 20
    MID_HEGIHT = 13
    SPEED = 512
    STOP = 0

    def __init__(self, program, emule=False):
        if emule:
            import ftemule as ftrobopy
        else:
            import ftrobopy
        self.ft = ftrobopy.ftrobopy("192.168.8.2", 65000)
        # motors
        self.m1 = self.ft.motor(1)
        self.m2 = self.ft.motor(2)
        self.m3 = self.ft.motor(3)
        self.m4 = self.ft.motor(4)  # pump
        # buttons
        self.i1 = self.ft.input(1)
        self.i2 = self.ft.input(2)
        self.i3 = self.ft.input(3)
        self.i4 = self.ft.ultrasonic(4)  # ultrasonic
        self.i5 = self.ft.input(5)  # emergency

        self.pressed = False
        self.last_update = 0
        self.come_back = False
        self.program = program


    def __str__(self):
        return """
    distance: %d
    i1 state: %d
    i2 state: %d
    i3 state: %d
        """ %(self.height, self.i1.state(), self.i2.state(), self.i3.state(),)

    def update(self):
        self.arm.m4.setSpeed(512*int(self.arm.pressed)) # if pressed setSpeed(0) else setSpeed(512s)
        self.height = self.i4.distance()

        # come back
        if self.come_back:
            self.m1.setSpeed(self.SPEED)
            if self.height > self.MAX_HEIGHT:   # UP
                self.m1.setSpeed(STOP)
            if self.i2.state():                 # BACK
                self.m2.setSpeed(STOP)
            if self.i2.state() and self.height >= self.MAX_HEIGHT:
                self.come_back = False
        # emergency
        if self.i5.state():
            self.program.playing = False
            self.m1.setSpeed(0)
            self.m2.setSpeed(0)
            self.m3.setSpeed(0)
            self.m4.setSpeed(0)
