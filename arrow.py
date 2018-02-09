# First try - skeleton of program name: tombola

import ftrobopy
import pygame
import time
import pygame.camera
from settings import *

# Make connection to TXTController
f = ftrobopy.ftrobopy("192.168.8.2", 65000)

# initialize pygame and create window
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[1], (WIDTH, HEIGHT))
cam.start()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_u:
                m1_speed = 512
            if e.key == pygame.K_j:
                m1_speed = -512
            if e.key == pygame.K_UP:
                m2_speed = -512
            if e.key == pygame.K_DOWN:
                m2_speed = 512
            if e.key == pygame.K_RIGHT:
                m3_speed = -512
            if e.key == pygame.K_LEFT:
                m3_speed = 512
            if e.key == pygame.K_p:
                if PRESS:
                    PRESS = False
                else:
                    PRESS = True
            if e.key == pygame.K_q:
                f.play_sound(14, 1)
                time.sleep(1)
                running = False
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                m2_speed = 0
            elif e.key == pygame.K_u or e.key == pygame.K_j:
                m1_speed = 0
            elif e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                m3_speed = 0

    # Update
    surface = cam.get_image()
    M1.setSpeed(m1_speed)
    M2.setSpeed(m2_speed)
    M3.setSpeed(m3_speed)
    if PRESS:
        M3.setSpeed(512)
    else:
        M3.setSpeed(0)

    # Draw /render
    pygame.draw.line(surface, (RED), (SIZE_LEFT), (SIZE_RIGHT), 5)
    pygame.draw.line(surface, (RED), (SIZE_BOTTOM), (SIZE_TOP), 5)
    screen.blit(surface, (0, 0))
    pygame.display.flip()

pygame.quit()
