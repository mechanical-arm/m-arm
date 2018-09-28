import pygame.time as time
import sys

class Arm:
    MIN_HEIGHT = 5
    MAX_HEIGHT = 7
    MID_HEGIHT = 6
    CATCH_HEIGHT = 3
    SPEED = 512
    STOP = 0

    FAC_X = 332.5
    FAC_Y = 307.7


    def __init__(self, program, emule=False):
        if emule: import ftemule as ftrobopy
        else: import ftrobopy
        self.program = program
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

        # flag
        self.pressed = False
        self.last_update = 0
        self.goto_back = False
        self.catch = False
        self.release = False
        self.goto_pos = False
        self.goto_x = False
        self.goto_y = False
        self.running = False
        self.last_update = 0

        # loop
        self.clock = time.Clock()
        self.playing = True

    def run(self):
        # loop
        while self.playing:
            self.clock.tick(40)
            self.update()

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
        self.running = True
        self.m1.setSpeed(-self.SPEED)
        if self.height <= self.MIN_HEIGHT:
            self.m1.setSpeed(self.STOP)
            self.pressed = False
            self.release = False
            self.running = False

    def _goto_pos(self, pos):
        x,y = pos
        if self.goto_x:
            self._goto_x(x)
        if self.goto_y:
            self._goto_y(y)
        if not self.goto_x and not self.goto_y:
                self.goto_pos = False
                self.running = False


    def _goto_x(self, x):
        self.running = True
        self.m3.setSpeed(-self.SPEED)
        now = time.get_ticks()
        if now - self.last_update > x*self.FAC_X:
            self.m3.setSpeed(self.STOP)
            self.goto_x = False

    def _goto_y(self, y):
        self.running = True
        self.m2.setSpeed(self.SPEED)
        now = time.get_ticks()
        if now - self.last_update > y*self.FAC_Y:
            self.m2.setSpeed(self.STOP)
            self.goto_y = False

    def play_sound(self, n, s=6):
        self.ft.play_sound(s, repeat=n)

    def update(self):
        self.m4.setSpeed(self.SPEED*int(self.pressed))
        self.height = self.i4.distance()

        # goto back
        if self.goto_back:
            self._goto_back()
        elif self.catch and self.i2.state() and self.i3.state():
            self._catch()
        elif self.release:
            self._release()
        elif self.goto_pos:
            self._goto_pos(self.pos)

        # emergency
        if self.i5.state():
            self.program.playing = False
            self.m1.setSpeed(0)
            self.m2.setSpeed(0)
            self.m3.setSpeed(0)
            self.m4.setSpeed(0)
            sys.exit(0)

    def offset_time(self):
        self.last_update = time.get_ticks()

    def goto_start(self):
        self.goto_pos = True
        self.goto_x = True
        self.goto_y = True



    def __str__(self):
        return """
        distance: %d
        i1 state: %d
        i2 state: %d
        i3 state: %d
        i5 state: %d
        ____________
        pressed: %d
        catch: %d
        release: %d
        goto_back: %d
        goto_pos: %d
            x: %d
            y: %d
        last_update: %d
        ____________
        running: %s
        """ %(self.height, self.i1.state(), self.i2.state(), self.i3.state(), self.i5.state(),
        self.pressed, self.catch, self.release, self.goto_back, self.goto_pos,
         self.goto_x, self.goto_y, self.last_update, self.running)
