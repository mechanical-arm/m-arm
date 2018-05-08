import pygame
class Arm:
    MIN_HEIGHT = 3
    MAX_HEIGHT = 15
    MID_HEGIHT = 13
    CATCH_HEIGHT = 10
    SPEED = 512
    STOP = 0


    def __init__(self, program, emule=False):
        if emule: import ftemule as ftrobopy
        else: import ftrobopy
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
        self.goto_back = False
        self.goto_id = False
        self.catch = False
        self.running = False
        self.last_update = 0
        self.program = program


    def __str__(self):
        return """
    distance: %d
    i1 state: %d
    i2 state: %d
    i3 state: %d
    ____________
    pressed: %d
    catch: %d
    goto_id: %d
    goto_back: %d
    last_update: %d
    ____________
    running: %s
""" %(self.height, self.i1.state(), self.i2.state(), self.i3.state(),
    self.pressed, self.catch, self.goto_id, self.goto_back, self.last_update, self.running)

    def _goto_back(self):
        self.running = True
        if self.height < self.MAX_HEIGHT:
            self.m1.setSpeed(self.SPEED)
        if not self.i2.state():
            self.m2.setSpeed(-self.SPEED)
        if self.height > self.MID_HEGIHT:
            self.m3.setSpeed(self.SPEED)

        if self.height >= self.MAX_HEIGHT:   # UP
            self.m1.setSpeed(self.STOP)
        if self.i2.state():                 # BACK
            self.m2.setSpeed(self.STOP)
        if self.i3.state():
            self.m3.setSpeed(self.STOP)

        if self.i2.state() and self.height >= self.MAX_HEIGHT and self.i3.state():
            self.goto_back = False
            self.running = False

    def _catch(self):
        if self.height > self.CATCH_HEIGHT:
            self.running = True
            self.m1.setSpeed(-self.SPEED)
            self.direction = True

        if self.height <= self.CATCH_HEIGHT:
            self.m1.setSpeed(self.STOP)
            self.pressed = True
            self.m1.setSpeed(self.SPEED)
            self.goto_back = True
            self.catch = False
            #self.running = False

    def _release(self):
        self.pressed = False

    def _goto_id(self):
        self.running = True
        self.m3.setSpeed(-self.SPEED)
        now = pygame.time.get_ticks()
        if now - self.last_update > 5000:
            self.last_update = now
            self.m3.setSpeed(self.STOP)
            self.goto_id = False
            self.running = False

    def update(self):
        self.height = self.i4.distance()

        # goto back
        if self.goto_back:
            self._goto_back()
        elif self.catch and self.i2.state() and self.i3.state():
            self._catch()
        elif self.goto_id:
            self._goto_id()

        # emergency
        if self.i5.state():
            self.program.playing = False
            self.m1.setSpeed(0)
            self.m2.setSpeed(0)
            self.m3.setSpeed(0)
            self.m4.setSpeed(0)
