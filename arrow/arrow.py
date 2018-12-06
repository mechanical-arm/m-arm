# First try - skeleton of program name: tombola

import ftrobopy
import pygame
import time
import pygame.camera
from settings import *


class Program:
    def __init__(self):
        emule = True
        joystick = True
        if emule: import ftemule as ftrobopy
        else: import ftrobopy
        pygame.joystick.init()
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()
        self.f = ftrobopy.ftrobopy("192.168.8.2", 65000)
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.speeds = [0,0,0,0]
        self.press = 0

        self.motors = list()
        for n in range(4):
            m = self.f.motor(n+1)
            self.motors.append(m)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            for m in self.motors:
                print(m.speed)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                k = event.key
                if k == pygame.K_u: self.speeds[0] = MAX_SPEED
                if k == pygame.K_j: self.speeds[0] = -MAX_SPEED
                if k == pygame.K_UP: self.speeds[1] = -MAX_SPEED
                if k == pygame.K_DOWN: self.speeds[1] = MAX_SPEED
                if k == pygame.K_RIGHT: self.speeds[2] = -MAX_SPEED
                if k == pygame.K_LEFT: self.speeds[2] = MAX_SPEED
                if k == pygame.K_p: self.press = not self.press
                if k == pygame.K_q: self.running = False
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: self.press = not self.press
                if event.button == 5: self.speeds[0] = MAX_SPEED
                if event.button == 4: self.speeds[0] = -MAX_SPEED
            if event.type == pygame.JOYBUTTONUP :
                if event.button in [4,5]: self.speeds[0] = 0
            if event.type == pygame.JOYHATMOTION:
                x, y = event.value
                self.speeds[2] = x*MAX_SPEED
                self.speeds[1] = y*MAX_SPEED
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]: self.speeds[1] = 0
                elif event.key in [pygame.K_u, pygame.K_j]: self.speeds[0] = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: self.speeds[2] = 0
        for n in range(3):
            self.motors[n].setSpeed(self.speeds[n])
        self.motors[-1].setSpeed(int(self.press)*MAX_SPEED)

if __name__ == "__main__":
    p = Program()
    p.run()
    pygame.quit()
