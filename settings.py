# Settings of arrow.py
import ftrobopy

TITLE = "Tombola Robot"
WIDTH = 640
HEIGHT = 480
FPS = 60
SIZE = (WIDTH, HEIGHT)
HEIGHT2 = HEIGHT/2

# Puntator
SIZE_LEFT = (WIDTH/2 - 20, HEIGHT2 + 120)
SIZE_RIGHT = (WIDTH/2 + 20, HEIGHT2 + 120)
SIZE_TOP = (WIDTH/2, HEIGHT2 + 120 - 20)
SIZE_BOTTOM = (WIDTH/2, HEIGHT2 + 120 + 20)

# colors
RED = (255, 0, 0)

PRESS = False

f = ftrobopy.ftrobopy("192.168.8.2", 65000)

M1 = f.motor(1)
M2 = f.motor(2)
M3 = f.motor(3)
M4 = f.motor(4)

I1 = f.input(1)
I2 = f.input(2)
I3 = f.input(3)
I4 = f.input(4)

M1_speed = 0
M2_speed = 0
M3_speed = 0
M4_speed = 0

SD = f.ultrasonic(4)
