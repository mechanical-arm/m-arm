
import pygame


class Joystick:
    def __init__(self):
        pygame.joystick.init()
        j = pygame.joystick.Joystick(0)
        s = pygame.display.set_mode((10,10))
        j.init()
        while True:
            for e in pygame.event.get():
                print(j.get_axis(0))
                print(e)
if __name__ == "__main__":
    j = Joystick()
