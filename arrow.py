# First try - skeleton of program name: tombola

import ftrobopy
import pygame
import time
import pygame.camera
from settings import *


class Program:
    def __init__(self):
        # initialize program window, set_caption
        pygame.init()
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[1], SIZE)
        self.cam.start()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.M1_speed = 0
        self.M2_speed = 0
        self.M3_speed = 0
        self.M4_speed = 0
        self.PRESS = 0

    def new(self):
        # start
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - Update
        self.surface = self.cam.get_image()
        print("Button 1", I1.state())
        print("Button 2", I2.state())
        print("Button 3", I3.state())
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.M1 = M1
        self.M2 = M2
        self.M3 = M3
        if PRESS:
            self.M3.setSpeed(512)
        else:
            self.M3.setSpeed(0)

    def events(self):
        # Game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    self.M1_speed = 512
                if event.key == pygame.K_j:
                    self.M1_speed = -512
                if event.key == pygame.K_UP:
                    self.M2_speed = -512
                if event.key == pygame.K_DOWN:
                    self.M2_speed = 512
                if event.key == pygame.K_RIGHT:
                    self.M3_speed = -512
                if event.key == pygame.K_LEFT:
                    self.M3_speed = 512
                if event.key == pygame.K_p:
                    if self.PRESS:
                        self.PRESS = False
                    else:
                        self.PRESS = True
                if event.key == pygame.K_q:
                    self.f = f.play_sound(0, 1)
                    if self.playing:
                        self.playing = False
                    self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.M2_speed = 0
                elif event.key == pygame.K_u or event.key == pygame.K_j:
                    self.M1_speed = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.M3_speed = 0
        M3.setSpeed(self.M3_speed)            
        M1.setSpeed(self.M1_speed)
        M2.setSpeed(self.M2_speed)
        if self.PRESS:
            self.M4 = M4.setSpeed(512)
        else:
            self.M4 = M4.setSpeed(0)

    def draw(self):
        # Game loop - draw
        self.surface = self.cam.get_image()
        pygame.draw.line(self.surface, (RED), (SIZE_LEFT), (SIZE_RIGHT), 5)
        pygame.draw.line(self.surface, (RED), (SIZE_BOTTOM), (SIZE_TOP), 5)
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

    def show_start_screen(self):
        # start show_go_screen
        pass


p = Program()
p.show_start_screen()
while p.running:
    p.run()

pygame.quit()
