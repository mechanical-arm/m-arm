# Settings of arrow.py

TITLE = "Tombola Robot"
WIDTH = 640
HEIGHT = 480
FPS = 60

# Puntator
SIZE_LEFT = (WIDTH - 20, HEIGHT)
SIZE_RIGHT = (WIDTH + 20, HEIGHT)
SIZE_TOP = (WIDTH, HEIGHT + 20)
SIZE_BOTTOM = (WIDTH, HEIGHT - 20)

# colors
RED = (255, 0, 0)

PRESS = False

M1 = f.motor(1)
M2 = f.motor(2)
M3 = f.motor(3)
M4 = f.motor(4)

M1_speed = 0
M2_speed = 0
M4_speed = 0

SD = f.ultrasonic(3)
