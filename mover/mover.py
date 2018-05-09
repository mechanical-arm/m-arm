# First try - skeleton of program name: tombola

import ftrobopy
import pygame
import time
import pygame.camera
from arm import Arm
from setting import *
from actions import Test

class Program:
    def __init__(self):
        pygame.init()
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[1], SIZE)
        self.cam.start()
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.pressed = 0
        self.playing = True
        self.arm = Arm(self)
        self.tester = Test(self)
        self.run()


    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u: self.arm.m1.setSpeed(512)
                elif event.key == pygame.K_j: self.arm.m1.setSpeed(-512)
                elif event.key == pygame.K_UP: self.arm.m2.setSpeed(-512)
                elif event.key == pygame.K_DOWN: self.arm.m2.setSpeed(512)
                elif event.key == pygame.K_RIGHT: self.arm.m3.setSpeed(-512)
                elif event.key == pygame.K_LEFT: self.arm.m3.setSpeed(512)
                elif event.key == pygame.K_p: self.arm.pressed = not self.arm.pressed
                elif event.key == pygame.K_q: self.playing = False
                elif event.key == pygame.K_s: self.arm.goto_back = True
                elif event.key == pygame.K_d: self.arm.catch = True
                elif event.key == pygame.K_g: self.tester.positioning.start()
                elif event.key == pygame.K_f:
                    self.arm.goto_id = True
                    self.arm.last_update = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]: self.arm.m2.setSpeed(0)
                elif event.key in [pygame.K_u or event.key, pygame.K_j]: self.arm.m1.setSpeed(0)
                elif event.key in [pygame.K_RIGHT or event.key, pygame.K_LEFT]: self.arm.m3.setSpeed(0)

    def update(self):
        self.arm.m4.setSpeed(512*int(self.arm.pressed))
        self.arm.update()





    def draw(self):
        print(self.arm)
        self.surface = self.cam.get_image()
        #pygame.draw.line(self.surface, (RED), (SIZE_LEFT), (SIZE_RIGHT), 5)
        #pygame.draw.line(self.surface, (RED), (SIZE_BOTTOM), (SIZE_TOP), 5)
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

p = Program()
