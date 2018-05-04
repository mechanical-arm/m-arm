from threading import Thread
from time import sleep

class Test:
    def __init__(self, program):
        self.program = program
        self.arm = program.arm
        self.positioning = Thread(target = self._positioning)

    def _positioning(self):
        self.arm.goto_back = True
        sleep(0.3)
        while self.arm.running: pass

        self.arm.catch = True
        sleep(0.3)
        while self.arm.running: pass

        self.arm.goto_id = True
        sleep(0.3)
        while self.arm.running: pass

        print("thread finitor")
